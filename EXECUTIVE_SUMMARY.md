# Executive Summary — Brazilian Real Wage Analysis, 2012–2025

**Version:** 3.0
**Author:** Vitor Ramos dos Santos
**Date:** February 2026

---

## Summary

Between 2012 and 2024, the real median wage of Brazilian formal workers (P50, PNAD Contínua) rose 15.6%. This document summarizes the main finding of the analysis: a meaningful share of that gain appears to be associated with a compositional shift in national income — labor's share of GDP rose from 68.1% to 73.7% (+5.6 percentage points) while capital's share fell correspondingly — alongside a period of historically low unemployment. Employment data from December 2025 (-618,000 net jobs, concentrated in services) is consistent with, though does not by itself confirm, a reversal of the cyclical component of these gains.

This is an observational, exploratory analysis based on public data. It does not establish causality, and several of the figures below are calibrated assumptions rather than statistically estimated parameters — this is stated explicitly wherever it applies. Readers should weight the conclusions accordingly.

---

## 1. Wage growth was concentrated in a short recovery period

| Period | Real median wage change | Note |
|---|---|---|
| 2012–2014 | +7.5% | Growth |
| 2015–2021 | -5.3% | Recession + pandemic |
| 2021 | — | Level similar to 2012 |
| 2022–2024 | +14.8% | Recovery |
| **2012–2024 (net)** | **+15.6%** | |

A substantial part of the 2012–2024 change consists of recovering ground lost during 2015–2021, rather than growth beyond the 2012 baseline. This does not diminish the 2022–2024 gains, but it is relevant context for interpreting the headline +15.6% figure.

---

## 2. Gains were progressive across the wage distribution

| Percentile | Real gain, 2012–2024 |
|---|---|
| P10 (bottom decile) | +16.7% |
| P50 (median) | +15.6% |
| P90 (top decile) | +10.3% |

The Gini index for labor income fell from 0.504 to 0.488 over the same period. Lower percentiles grew faster than higher ones, consistent with the real minimum wage policy (which sets a binding floor concentrated at the lower end of the distribution) as a contributing factor.

---

## 3. A structural/cyclical decomposition of the +15.6% gain

The analysis splits the total gain into components judged to be more persistent ("structural") and more sensitive to the business cycle ("cyclical"):

**Structural (approx. 58% of the gain):**
- Real minimum wage policy (INPC + lagged GDP growth formula): ~6.2pp
- Labor's increased share of GDP: ~3.0pp

**Cyclical (approx. 42% of the gain):**
- Historically low unemployment (6.6%, likely below a sustainable rate): ~3.0pp
- Base effect from the 2015–2021 recession: ~5.0pp

**Caveat on these figures:** the boundary between "structural" and "cyclical" is a judgment call, not a statistically derived split, and the percentages should be read as approximate. The unemployment-sensitivity assumption used to project a reversal scenario is a calibrated value informed by sub-period patterns and general labor-economics literature — it is *not* a statistically significant coefficient. The one regression tested on this dataset (real wage on unemployment, full sample, 2012–2024) returned R² = 0.037 and p = 0.493, i.e., not distinguishable from no relationship at the 5% level. Full detail in [METHODOLOGY.md](METHODOLOGY.md), Sections 7.1 and 9.1.

**Illustrative scenario (not a forecast):** if unemployment were to rise to around 10%, the model's cyclical component would be expected to reverse (~-7pp), while the structural component would be expected to hold (~+9pp), implying a median wage in the neighborhood of R$880 — still above the 2012 level, but below 2024. This is a scenario built on calibrated assumptions, not a statistical projection with a defined confidence interval.

---

## 4. Productivity: an open question

Apparent labor productivity (earnings per hour) rose 21.1% over 2012–2024. This is measured as earnings/hour from survey data, not GDP per hour worked, and the two are not the same thing. Three explanations are plausible and cannot be fully distinguished with the data available:

1. A genuine increase in worker productivity.
2. Composition effects (shifts between informal and formal work, or between sectors, can move the average without any individual becoming more productive).
3. Measurement or survey-methodology artifacts.

What can be stated with more confidence: nominal wage mass grew 26.5% (IBGE) against GDP growth of 11.2% over the same period — a gap of roughly 15 percentage points, consistent with the labor-share shift described in Section 3.

---

## 5. December 2025 employment data

Before December 2025 data was released, the analysis noted that a deceleration in growth combined with rising unemployment would be expected to reverse the cyclical component of wage gains, as firms typically respond to margin pressure by reducing headcount.

December 2025 CAGED data reported a net loss of 618,164 formal jobs, with services (-280,810), industry (-135,087), and construction (-104,077) showing the largest declines. This single data point is directionally consistent with the anticipated mechanism, but one month of data is not sufficient to confirm a sustained trend, and alternative explanations (seasonal effects, one-off shocks) have not been ruled out. This should be treated as an observation to monitor, not as validation of the thesis.

---

## 6. Uncertainty quantification

To characterize uncertainty around a 2026 projection, a Monte Carlo simulation (10,000 draws) varied unemployment, GDP growth, inflation, and minimum-wage policy within plausible ranges, using the calibrated elasticities described in Section 3. Results:

- Expected median wage, 2026: ~R$914 (range: R$870–960)
- Probability of decline vs. 2024: ~47%
- Probability of decline greater than 5%: ~18%

These figures reflect the sensitivity of the model to its input assumptions, not an independent statistical forecast. They should be read as "what the model implies under these assumed sensitivities."

---

## 7. Methodology notes and limitations

**What strengthens confidence in the findings:**
- An earlier version of the analysis contained a double-deflation error, which was identified and corrected (v1.0 estimate of -42% real change corrected to +15.6% in v3.0).
- Findings were cross-checked against four independent data sources (minimum wage records, GDP accounts, wage mass, Gini index), which were broadly consistent with each other.
- A structural break test (pre/post-2021) was used to separate trend regimes rather than assuming one continuous trend.

**Limitations, stated directly:**
- PNAD Contínua covers formal workers; roughly 39% of the Brazilian workforce is informal and excluded from this analysis.
- "Productivity" here is a proxy (earnings/hour), not a direct productivity measure.
- The analysis is correlational. The one regression formally tested (wage vs. unemployment) was not statistically significant; elasticities used in the scenario simulator are calibrated assumptions, not fitted coefficients, and this is stated wherever those figures are used.
- The structural/cyclical decomposition percentages are estimates based on judgment, not a precise statistical decomposition.

---

## Further reading

- **[Methodology](METHODOLOGY.md):** full derivation, hypothesis tests, and limitations.
- **[Charts](graficos/):** supporting visualizations.
- **[Scripts](scripts/):** Python and R code, reproducible from public data.
- **[Data](dados/):** source CSVs, all sources documented.

---

**Last updated:** February 19, 2026
**Author:** Vitor Ramos dos Santos
**Contact:** vitorramossantos8@gmail.com
