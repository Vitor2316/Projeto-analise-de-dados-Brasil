# Real Wages in Brazil, 2012–2025: A Structural and Cyclical Decomposition

[![Status](https://img.shields.io/badge/Status-Complete-success)](https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0+-blue)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Version 3.0** · Author: Vitor Ramos dos Santos · Last updated: February 2026

*[Leia em português](README_PT.md)*

---

## Overview

Between 2012 and 2024, the real median wage of Brazilian formal workers rose 15.6% (PNAD Contínua). This project decomposes that gain into components more tied to policy and structural change, and components more tied to the labor market cycle — and checks the result against employment data through December 2025.

**Main finding:** an estimated 58% of the gain is associated with structural factors (chiefly minimum wage policy and a shift in labor's share of GDP) likely to persist; an estimated 42% is associated with cyclical conditions (historically low unemployment, recovery from the 2015–2021 downturn) that are more sensitive to the business cycle. This decomposition relies on calibrated assumptions rather than a statistically significant regression coefficient — see [Methodology](METHODOLOGY.md) for the full derivation and that caveat in detail.

**Start here:** [Executive Summary](EXECUTIVE_SUMMARY.md) (5 min) · [Full Methodology](METHODOLOGY.md) · [Charts](graficos/)

---

## Key figures

| Metric | 2012 | 2024 | Change |
|---|---|---|---|
| Real median wage (P50) | R$805 | R$930 | +15.6% |
| Labor's share of GDP | 68.1% | 73.7% | +5.6pp |
| Gini index (labor income) | 0.504 | 0.488 | -0.016 |
| Unemployment rate | 7.4% | 6.6% | -0.8pp |

December 2025 (most recent CAGED release): -618,000 net formal jobs, concentrated in services (-281,000). This is discussed in Section 5 of the [Executive Summary](EXECUTIVE_SUMMARY.md) as a data point consistent with — but not sufficient on its own to confirm — a reversal of the cyclical component described above.

---

## Charts

### Wage trajectory and distribution

**Typical worker trajectory, 2012–2025**
![Trajectory](graficos/01_trajetoria_trabalhador_tipico.png)
Ten years (2012–2021) with essentially no net gain, followed by a concentrated recovery in 2022–2024.

**Decomposition of the +15.6% gain: structural vs. cyclical**
![Decomposition](graficos/02_decomposicao_estrutural_conjuntural.png)
An estimated 58% of the gain is structural (minimum wage policy, redistribution); 42% is cyclical (low unemployment, recovery effect). See the calibration caveat in [Methodology](METHODOLOGY.md), Section 9.1.

**Gains by percentile (P10, P50, P90)**
![Progressive](graficos/03_ganhos_progressivos_percentis.png)
Lower percentiles grew faster than higher ones (+16.7% vs. +10.3%), consistent with the minimum wage policy as a contributing factor.

### Labor share and the business cycle

**Labor's share of GDP, 2012–2024**
![GDP share](graficos/04_participacao_trabalho_pib.png)
Labor's share rose from 68.1% to 73.7%, with capital's share falling correspondingly — roughly R$655 billion/year in 2024 terms.

**Wage mass vs. GDP (indexed, 2012 = 100)**
![Wage mass vs GDP](graficos/06_massa_salarial_vs_pib.png)
Real wage mass grew faster than GDP over the period, consistent with the labor-share shift above.

**Unemployment and real wages**
![Unemployment](graficos/05_desemprego_vs_salario.png)
Descriptive series shown side by side. Note: the formal regression of wages on unemployment across the full sample was not statistically significant (R² = 0.037, p = 0.493) — see Methodology, Section 7.1.

**Hours worked vs. earnings per hour**
![Hours vs productivity](graficos/09_horas_vs_produtividade.png)
Average hours worked declined slightly while earnings per hour rose 21%. This is an apparent-productivity proxy, not a direct productivity measure — three plausible explanations are discussed in the Executive Summary, Section 4.

### Employment data (CAGED)

**December 2025: net job losses by sector**
![CAGED reversal](graficos/07_caged_reversao_dez2025.png)
-618,000 net formal jobs in December 2025, led by services (-281,000), industry (-135,000), and construction (-104,000).

**Job creation, 2020–2025**
![Job creation deceleration](graficos/08_criacao_empregos_desaceleracao.png)
Net job creation has slowed relative to the 2021 peak.

### Forecasting and uncertainty

**2026 scenarios (illustrative)**
![2026 projections](graficos/10_projecoes_2026.png)

**2026–2030 forecast, multiple models**
![2026-2030 forecast](graficos/11_previsao_2026_2030.png)
Linear trend, recent-trend, and scenario-based projections shown together with a 95% confidence band around the linear trend. The scenario-based lines use the calibrated elasticities described in Methodology, Section 9.1, not statistically fitted coefficients.

**Sensitivity analysis**
![Sensitivity analysis](graficos/12_analise_sensibilidade.png)
Projected 2026 wage as a function of unemployment, GDP growth, inflation, and minimum wage policy, holding other factors fixed.

**Monte Carlo simulation (10,000 draws)**
![Monte Carlo](graficos/13_monte_carlo.png)
Distribution of 2026 wage outcomes under randomized macro assumptions. Expected value ≈ R$914, with a 90% interval of roughly R$870–960.

**Scenario matrix: unemployment × inflation**
![Scenario matrix](graficos/14_matriz_cenarios.png)

### International comparison

**PPP-adjusted GDP per capita, Brazil vs. peers**
![PPP GDP](graficos/15_pib_ppc_internacional.png)

**Labor share of GDP, international comparison**
![Labor share international](graficos/16_labor_share_internacional.png)

**GDP per capita vs. labor share, 2024**
![Scatter](graficos/17_scatter_pib_labor.png)
Used to check whether Brazil's labor-share level is an outlier relative to comparable economies (Chile, Mexico, Colombia, Turkey, Argentina), as a sanity check on the redistribution finding above.

---

## Methodology summary

- **Primary data:** IBGE PNAD Contínua (2012–2024, national household survey)
- **Validation:** CAGED employment data, National Accounts, minimum wage records, international comparators
- **Statistical methods:** linear regression, structural break testing, Monte Carlo simulation, sensitivity analysis
- **Known limitation:** the only formally tested regression (wage vs. unemployment, full sample) was not statistically significant. Elasticities used in the scenario simulator are calibrated assumptions informed by sub-period patterns and labor-economics literature, not fitted coefficients. This is stated explicitly wherever those figures are used — see [Methodology](METHODOLOGY.md), Sections 7.1, 9.1, and 12.3.
- **Coverage limitation:** PNAD Contínua covers formal workers only; roughly 39% of the Brazilian workforce is informal and outside this analysis.

Full derivation, hypothesis tests, and all limitations: [METHODOLOGY.md](METHODOLOGY.md).

---

## Repository structure

```
├── README.md                    # This file
├── README_PT.md                 # Portuguese version
├── EXECUTIVE_SUMMARY.md          # 5-minute summary of findings
├── METHODOLOGY.md               # Full methodology, tests, limitations
├── graficos/                    # 17 charts (300 DPI), referenced above
├── dados/                       # Source and derived CSVs
├── scripts/                     # Python and R, fully reproducible
└── LICENSE                      # MIT
```

## Reproducing the analysis

```bash
git clone https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil
cd Projeto-analise-de-dados-Brasil
pip install -r requirements.txt   # numpy, pandas, matplotlib, seaborn, scikit-learn, scipy
python scripts/gerar_graficos_v3.py
```

All data sources are public (IBGE SIDRA, Brazilian Ministry of Labor). No proprietary or restricted data is used.

---

## Author

Vitor Ramos dos Santos — technical high school student in computer science. This research was conducted independently using public data sources.

**Contact:** vitorramossantos8@gmail.com
**LinkedIn:** www.linkedin.com/in/vitor-ramos2132

## License

MIT — see [LICENSE](LICENSE).

**Disclaimer:** This analysis reflects the author's interpretation of publicly available data. It does not constitute financial, legal, or investment advice.
