from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]

def stats(r):
    r = r.dropna()
    wealth = (1 + r).cumprod()
    years = len(r) / 52
    cagr = wealth.iloc[-1] ** (1 / years) - 1 if years > 0 else np.nan
    sharpe = np.sqrt(52) * r.mean() / r.std(ddof=1) if r.std(ddof=1) else np.nan
    drawdown = wealth / wealth.cummax() - 1
    return {"cagr": float(cagr), "sharpe": float(sharpe),
            "max_drawdown": float(drawdown.min())}

def backtest(prices, lookback, top_n, cost_bps):
    weekly = prices.resample("W-FRI").last().dropna(how="all")
    returns = weekly.pct_change()
    signal = weekly.pct_change(lookback).shift(1)
    ranks = signal.rank(axis=1, ascending=False, method="first")
    weights = (ranks <= top_n).astype(float)
    weights = weights.div(weights.sum(axis=1), axis=0).fillna(0)
    gross = (weights * returns).sum(axis=1)
    turnover = weights.diff().abs().sum(axis=1) / 2
    net = gross - turnover * cost_bps / 10000
    benchmark = returns.mean(axis=1)
    return pd.DataFrame({"strategy_net": net, "equal_weight": benchmark,
                         "turnover": turnover})

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="2006-01-01")
    p.add_argument("--end", default="2023-01-01")
    p.add_argument("--top-n", type=int, default=3)
    p.add_argument("--cost-bps", type=float, default=10)
    args = p.parse_args()
    tickers = pd.read_csv(ROOT / "data/universe.csv")["ticker"].tolist()
    raw = yf.download(tickers, start=args.start, end=args.end, auto_adjust=True,
                      progress=False)["Close"]
    out = ROOT / "outputs"; out.mkdir(exist_ok=True)
    all_metrics = {}
    for lookback in (4, 12, 26, 52):
        result = backtest(raw, lookback, args.top_n, args.cost_bps)
        result.to_csv(out / f"backtest_{lookback}w.csv")
        all_metrics[f"{lookback}w"] = {
            "strategy": stats(result["strategy_net"]),
            "equal_weight": stats(result["equal_weight"]),
            "average_turnover": float(result["turnover"].mean())
        }
    (out / "metrics.json").write_text(json.dumps(all_metrics, indent=2))
    print(json.dumps(all_metrics, indent=2))

if __name__ == "__main__":
    main()
