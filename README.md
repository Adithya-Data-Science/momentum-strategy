# Weekly Cross-Sectional Momentum Strategy

A transparent backtest of a weekly long-only momentum strategy on a deliberately small seven-stock technology universe.

## Design

- Universe: AAPL, MSFT, AMZN, GOOGL, META, NVDA, NFLX
- Data: adjusted daily prices downloaded at runtime with `yfinance`
- Rebalancing: weekly
- Signal: lagged lookback return
- Portfolio: equal weight among the top-ranked assets
- Benchmark: equal-weight universe
- Costs: proportional cost applied to one-way turnover
- Robustness: multiple lookback windows

The signal is shifted one week before portfolio returns are calculated. This prevents using the same period's return to choose that period's holdings.

## Resume reference result

The earlier 2006-2022 experiment reported 22.5% net CAGR and 0.93 Sharpe, versus 17.2% and 0.88 for equal weight. Because the universe is small and technology-heavy, those figures are narrow-universe evidence, not a general performance claim. The script reports fresh results from the selected retrieval period.

## Run

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/backtest.py --start 2006-01-01 --end 2023-01-01
```

Outputs are written to `outputs/`. Downloaded market data and outputs are excluded from Git because vendor data can change and may carry redistribution restrictions.

## Limitations

Small selected universe, survivorship bias, no capacity model, simplified transaction costs, and no taxes or market-impact model. Results are research demonstrations, not investment advice.