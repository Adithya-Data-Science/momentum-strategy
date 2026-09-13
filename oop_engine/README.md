# Object-Oriented Python Trading Analytics Engine

A testable quantitative research application demonstrating object-oriented Python design, strategy abstraction, transaction-cost-aware backtesting and risk analytics.

## Architecture
- `PricePanel` validates a multi-asset price matrix and exposes returns.
- `Strategy` defines an interchangeable strategy interface.
- `MomentumStrategy` implements lagged cross-sectional ranking and scheduled rebalancing.
- `BacktestEngine` applies prior-day holdings, turnover and proportional transaction costs without look-ahead.
- `RiskEngine` reports annualized return/volatility, Sharpe ratio, max drawdown and historical 95% daily VaR.

## Reproduce
```bash
python -m venv .venv
pip install -r oop_engine/requirements.txt
python -m oop_engine.run_demo
pytest -q oop_engine/tests
```

## Start-to-finish workflow
1. Generate a validated multi-asset price panel.
2. Calculate lagged momentum signals through a `Strategy` implementation.
3. Convert signals into target portfolio weights at scheduled rebalance dates.
4. Apply yesterday's holdings to today's returns to avoid look-ahead.
5. Measure turnover and deduct transaction costs.
6. Compute risk and performance metrics.
7. Save reproducible output metrics and verify behavior with pytest.
8. Swap in another strategy class without changing the backtest/risk engine.

The demo uses deterministic synthetic data so it can be reproduced without credentials. It is an engineering demonstration, not evidence of live alpha.
