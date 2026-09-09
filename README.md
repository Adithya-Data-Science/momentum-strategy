# Systematic Trading Signals & Walk-Forward Backtesting

A transparent quantitative strategy research project that tests cross-sectional momentum signals with explicit lagging, turnover, transaction costs and robustness checks. The project is designed to demonstrate how trading signals should be researched without look-ahead bias.

## Research question

Can lagged cross-sectional momentum signals improve portfolio outcomes relative to an equal-weight benchmark after accounting for turnover and simple transaction costs?

## Skills demonstrated

- Systematic trading-signal design
- Cross-sectional ranking
- Portfolio formation and rebalancing
- Backtesting and transaction-cost modeling
- Walk-forward / out-of-sample research discipline
- CAGR, Sharpe ratio, drawdown and turnover analysis
- Python, Pandas, NumPy and yfinance
- Robustness testing and limitations reporting

## Universe

A deliberately small seven-stock technology universe:

AAPL, MSFT, AMZN, GOOGL, META, NVDA and NFLX.

The narrow universe keeps the mechanics auditable; it is not meant to represent a diversified institutional investment universe.

## Start-to-finish workflow

1. Download adjusted daily prices at runtime.
2. Resample prices to Friday weekly observations.
3. Calculate weekly returns.
4. Construct trailing momentum signals over 4-, 12-, 26- and 52-week windows.
5. Shift the signal by one week before portfolio returns are calculated to prevent look-ahead bias.
6. Rank securities cross-sectionally each rebalance date.
7. Equal-weight the top-ranked securities.
8. Calculate one-way turnover from changes in portfolio weights.
9. Deduct proportional transaction costs from gross strategy returns.
10. Compare the net strategy with an equal-weight universe benchmark.
11. Evaluate CAGR, Sharpe ratio, maximum drawdown and average turnover.
12. Run multiple lookback windows instead of reporting only the most favorable specification.
13. Treat the results as a research demonstration rather than evidence of a production-ready alpha strategy.

## Backtest mechanics

The signal used for week `t` is formed only with data available before the week-t return. Portfolio costs are applied as:

`net return = gross return - turnover x cost rate`

The code reports both net strategy results and the equal-weight benchmark for every lookback specification.

## Historical reference result

An earlier 2006-2022 experiment reported **22.5% net CAGR and 0.93 Sharpe**, versus **17.2% CAGR and 0.88 Sharpe** for equal weight. Because this is a small, technology-heavy and survivorship-biased universe, those figures are narrow-universe historical evidence rather than a general investment claim.

The pipeline reports fresh results from the selected retrieval period.

## Run

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/backtest.py --start 2006-01-01 --end 2023-01-01 --top-n 3 --cost-bps 10
```

Generated files are written to `outputs/` for each signal horizon, plus a combined `metrics.json` summary.

## Why this matters for quantitative research

The project demonstrates that a trading signal is not just a formula: timing, lagging, portfolio formation, turnover, costs, benchmark choice and robustness all affect the validity of the result. Those implementation controls are central to separating an appealing backtest from defensible quantitative research.

## Limitations

The universe is selected, small and sector-concentrated; survivorship bias is present; capacity and market impact are not modeled; taxes are ignored; and simplified transaction costs do not represent institutional execution.

## Resume-ready description

**Systematic Trading Signals & Walk-Forward Backtesting | Python, Pandas, NumPy**

Designed lagged cross-sectional momentum signals across multiple lookback horizons, formed weekly ranked portfolios and deducted turnover-based transaction costs before comparing performance with an equal-weight benchmark. Evaluated CAGR, Sharpe ratio, drawdown and turnover while explicitly documenting look-ahead, survivorship, concentration and execution limitations.
