# Systematic Trading Signals & Walk-Forward Backtesting

A transparent quantitative strategy study of cross-sectional momentum with explicit signal lagging, turnover, transaction costs and multi-horizon robustness checks.

## Result snapshot

| Metric | Net momentum strategy | Equal-weight benchmark |
| --- | ---: | ---: |
| CAGR, 2006-2022 historical reference | 22.5% | 17.2% |
| Sharpe ratio | 0.93 | 0.88 |

The reference run used a seven-stock technology universe and 10-basis-point turnover costs. It is evidence that the pipeline and hypothesis are worth broader testing, **not** a claim of production-ready alpha. Read the [client-style research brief](RESEARCH_BRIEF.md).

## Research question

Can lagged cross-sectional momentum signals improve portfolio outcomes relative to an equal-weight benchmark after accounting for turnover and simple transaction costs?

## Method

- Adjusted daily prices resampled to Friday observations
- 4-, 12-, 26- and 52-week momentum specifications
- One-week signal lag before return calculation
- Weekly top-ranked, equal-weight portfolio
- One-way turnover and proportional trading costs
- Equal-weight universe benchmark
- CAGR, Sharpe ratio, maximum drawdown and average turnover

## Reproduce

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/backtest.py --start 2006-01-01 --end 2023-01-01 --top-n 3 --cost-bps 10
```

Fresh runs write one backtest CSV per signal horizon plus `outputs/metrics.json`. The committed `outputs/reference_metrics.json` keeps the historical reference evidence distinct from refreshed market data.

## Start-to-finish workflow

1. Download adjusted prices and validate the fixed universe.
2. Resample to weekly observations and calculate returns.
3. Build each trailing momentum signal and lag it by one week.
4. Rank stocks cross-sectionally and equal-weight the top selections.
5. calculate one-way turnover and deduct transaction costs.
6. Compare net results with the equal-weight benchmark.
7. Report all specified horizons rather than selecting only the best result.
8. Interpret performance alongside concentration, survivorship and execution limitations.

## Repository map

- `src/backtest.py` - research and backtest pipeline
- `data/universe.csv` - auditable seven-stock universe
- `outputs/reference_metrics.json` - historical reference evidence
- `RESEARCH_BRIEF.md` - executive interpretation and next tests
- `requirements.txt` - reproducible dependencies

## Limitations

The selected universe is small, sector-concentrated and survivorship-biased. Capacity, market impact, taxes and delistings are not fully modeled. The simplified cost assumption is not institutional execution evidence.
