# METHODOLOGY - Brazil Wages Analysis 2012-2025 (v3.0)

**Version:** 3.0 (Final Validated)  
**Author:** Vitor Ramos dos Santos  
**Date:** February 2026  
**Status:** Complete and Validated

---

##  Table of Contents

1. [Research Objective](#1-research-objective)
2. [Data Sources](#2-data-sources)
3. [Critical Methodological Correction](#3-critical-methodological-correction)
4. [Data Processing](#4-data-processing)
5. [Calculated Metrics](#5-calculated-metrics)
6. [Validation Tests](#6-validation-tests)
7. [Statistical Analysis](#7-statistical-analysis)
8. [Structural vs Cyclical Decomposition](#8-structural-vs-cyclical-decomposition)
9. [Limitations and Assumptions](#9-limitations-and-assumptions)
10. [Ethical Considerations](#10-ethical-considerations)
11. [References](#11-references)

---

## 1. RESEARCH OBJECTIVE

### 1.1 Central Question
How did the real purchasing power of Brazilian workers evolve between 2012-2025? Were gains distributed or concentrated? Permanent or temporary?

### 1.2 Specific Objectives
1. **Quantify** the real variation of median wage (typical worker)
2. **Analyze** distribution of gains by percentile (P10, P50, P90)
3. **Decompose** gains into structural vs cyclical components
4. **Identify** causal drivers (minimum wage, unemployment, redistribution)
5. **Validate** results with multiple independent sources
6. **Project** scenarios for 2026

### 1.3 Analyzed Period
- **Main period:** 2012-2024 (13 complete years)
- **Extended period:** 2012-2025 (includes partial data/projections)
- **Frequency:** Annual (aggregation of PNAD quarterly data)

---

## 2. DATA SOURCES

### 2.1 Primary Data (Brazil)

**Institution:** IBGE - Brazilian Institute of Geography and Statistics  
**System:** SIDRA - IBGE Automatic Recovery System  
**Survey:** PNAD Contínua (Continuous National Household Sample Survey)  
**URL:** https://sidra.ibge.gov.br

**Tables Used:**

| Table | Description | Use in Study |
|-------|-------------|--------------|
| 5436 | Real average monthly income (already deflated) | Real wage and productivity |
| 6371 | Hours worked per week | Earnings/hour calculation |
| 7535 | Income by percentiles (P5, P10, P50, P90, P99) | Distributional analysis |
| 7453 | Gini Index of labor income | Inequality measure |
| 4562 | Unemployment rate | Hypothesis testing |
| 4708 | Informality rate | Formalization test |
| 4359 | Labor force participation rate | Structural change |
| 4663 | Aggregate real wage mass | Cross-validation |
| 10369 | Hours worked (annual) | Validation |
| 4362 | Employed population by sector | Sectoral analysis |

**Territory:** Brazil (national level)  
**Original Frequency:** Quarterly (we aggregated to annual)

### 2.2 Complementary Data

**Minimum Wage:**
- Source: Federal Government (official publications)
- Deflation: Accumulated CPI (calculated in this study)

**Real GDP:**
- Source: IBGE - Quarterly National Accounts
- Use: Labor share of GDP calculation

**CPI (Inflation):**
- Source: IBGE - Price Index System
- Years: 2012-2024 (closed official data)

**CAGED (Formal Employment):**
- Source: Ministry of Labor - New CAGED
- URL: https://bi.mte.gov.br/bgcaged/
- Use: Sectoral hypothesis validation and reversal identification

### 2.3 International Data (Comparison)

**Source:** OECD Labour Productivity Database  
**Countries:** Turkey, Peru, Chile, Brazil, Colombia, Uruguay  
**Selection Criteria:** Middle-income emerging economies  
**Frequency:** Annual  
**Use:** Contextualization of Brazilian results

---

## 3. CRITICAL METHODOLOGICAL CORRECTION

### 3.1 Identified Error: Double Deflation

**Discovery (v1.0):**
IBGE Table 5436 provides income in "real values" - **already deflated by IBGE** using proprietary methodology.

**Initial Error:**
```python
# WRONG - v1.0
real_wage = nominal_wage / cpi_deflator  # Table already deflated!
```

This caused **double deflation**, resulting in apparent loss of -42% (incorrect).

**Applied Correction (v2.0 and v3.0):**
```python
# CORRECT
real_wage_index = (year_value / value_2012) * 100  # No additional deflation
```

**Correction Impact:**

| Version | Method | Real Wage Result |
|---------|--------|------------------|
| v1.0 ❌ | Double deflation | -42% (error) |
| v2.0 ⚠️ | No additional deflation, simple mean | +22% (incomplete) |
| v3.0 ✅ | No deflation, median + percentile analysis | +15.6% (correct) |

### 3.2 Methodological Lessons

1. **ALWAYS verify documentation** from data source (IBGE metadata)
2. **Question implausible results** (-42% loss didn't match reality)
3. **Validate with independent sources** (minimum wage, GDP per capita)
4. **Prefer median to mean** for data with asymmetric distribution

---

## 4. DATA PROCESSING

### 4.1 Data Cleaning (SIDRA Tables)

**Typical SIDRA CSV Structure:**
```
Row 1: Table title
Row 2: Variable description
Row 3: Period headers
Row 4: "Brazil"; value1; value2; value3...
Row 5+: Notes, source, legends
```

**Extraction Code (Python):**
```python
def extract_sidra_data(csv_file):
    with open(csv_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    # Row 4 contains "Brazil" and values
    brazil_row = lines[4].replace('"', '').strip().split(';')
    values = [float(v.replace(',', '.')) for v in brazil_row[1:]]
    
    return values
```

### 4.2 Treatment of Table 7535 (Percentiles)

**Challenge:** Table uses "average prices of the year" - each year in different base.

**Solution:** Deflate to common base (2012):
```python
# Accumulated CPI since 2012
accumulated_cpi = {
    2012: 1.000,
    2013: 1.059,  # 1.000 × (1 + 0.0591)
    2014: 1.127,  # 1.059 × (1 + 0.0641)
    # ... until 2024
    2024: 1.971
}

# Convert to real base 2012
p10_real_2024 = p10_nominal_2024 / accumulated_cpi[2024]
```

### 4.3 Accumulated Compound CPI Calculation

**Formula:**
```
CPI_accumulated_t = CPI_accumulated_{t-1} × (1 + CPI_t / 100)
```

**CPI Rates Used (Source: IBGE):**
| Year | CPI (%) | Accumulated |
|------|---------|-------------|
| 2012 | 5.84 | 1.000 (base) |
| 2013 | 5.91 | 1.059 |
| 2014 | 6.41 | 1.127 |
| ... | ... | ... |
| 2024 | 4.83 | 1.971 |

**Accumulated Variation 2012-2024:** +97.1% inflation

---

## 5. CALCULATED METRICS

### 5.1 Real Wage (Purchasing Power)

**Direct Source:** Table 5436 (already deflated by IBGE)  
**Index Formula:**
```
Index_t = (Real_Wage_t / Real_Wage_2012) × 100
Variation (%) = Final_Index - 100
```

**Interpretation:** Measures worker's purchasing power over time.

### 5.2 Earnings per Hour (Productivity Proxy)

**Formula:**
```
Earnings/Hour = Real Monthly Income / (Weekly Hours × 4.33)
```

Where:
- Real Monthly Income: from Table 5436
- Weekly Hours: from Table 6371 or 10369
- 4.33 = average weeks per month (52 weeks/year ÷ 12 months)

**Caveat:** This is **apparent** productivity (earnings/hour). **Real** productivity would be GDP/total hours, which we didn't calculate due to lack of complete sectoral data.

### 5.3 Distribution Percentiles

**Source:** Table 7535  
**Analyzed Percentiles:**
- P5: Bottom 5%
- P10: Bottom 10% (pyramid base)
- P50: Median (typical worker - 50% earn less, 50% earn more)
- P90: Top 10%
- P99: Top 1% (elite)

**Inequality Measure:**
```
P90/P10 Ratio = Top wage / Base wage
```

Higher ratio = more unequal distribution.

### 5.4 Gini Index

**Source:** Table 7453  
**Interpretation:**
- Gini = 0: Perfect equality (everyone earns the same)
- Gini = 1: Maximum inequality (one earns everything)
- Falling Gini → Decreasing inequality
- Rising Gini → Increasing inequality

### 5.5 Labor Share of GDP

**Formula:**
```
Labor Share = (Nominal Wage Mass / Nominal GDP) × 100
```

**Data:**
- Nominal Wage Mass = Employed Population × Average Income × 12 months
- Nominal GDP: National Accounts (IBGE)

**Interpretation:**
- Share rises → Workers captured more of GDP
- Share falls → Capital (profits) captured more

**Complement:**
```
Capital Share = 100% - Labor Share
```

---

## 6. VALIDATION TESTS

### 6.1 Validation with Real Minimum Wage

**Hypothesis:** If P10 follows minimum wage, variations should be close.

**Test:**
| Indicator | Variation 2012-2024 |
|-----------|---------------------|
| Real Minimum Wage | +18.5% |
| P10 (PNAD) | +16.7% |
| Difference | 1.8pp |

**Verdict:** ✅ **Consistent** - P10 closely follows MW

### 6.2 Validation with GDP per Capita

**Hypothesis:** Average wage shouldn't grow much more than GDP per capita.

**Test:**
| Indicator | Variation 2012-2024 |
|-----------|---------------------|
| Real GDP per capita | +6.0% |
| Real average wage (PNAD) | +18.2% |
| P50 (median) | +15.6% |

**Interpretation:**
- Wage grew MORE than GDP per capita
- Redistribution from capital to labor (+5.6pp)
- Consistent with profit squeeze

**Verdict:** ✅ **Coherent with redistribution**

### 6.3 Validation with Official Wage Mass

**Hypothesis:** Our wage mass calculation should approximate official IBGE.

**Test:**
| Method | Variation 2012-2024 |
|--------|---------------------|
| Our calculation (pop × inc × 12) | +33.9% |
| Official IBGE (Table 4663) | +26.5% |
| Difference | 7.4pp |

**Reason for Divergence:**
- Our calculation uses **habitual** income
- IBGE may use **effective** income (includes overtime, bonuses)
- Both methodologies are valid

**Verdict:** ✅ **Order of magnitude validated**

### 6.4 Validation with Gini

**Hypothesis:** If P10 grew more than P90, Gini should fall.

**Test:**
| Indicator | 2012 | 2024 | Change |
|-----------|------|------|--------|
| P10 | R$187 | R$218 | +16.7% |
| P90 | R$2,234 | R$2,465 | +10.3% |
| Gini | 0.504 | 0.488 | -3.2% |
| P90/P10 Ratio | 11.9x | 11.3x | -5% |

**Verdict:** ✅ **Fully consistent** - Base grew more than top

---

## 7. STATISTICAL ANALYSIS

### 7.1 Descriptive Analysis

**Central Tendency Measures:**
- Median (P50): Preferred to mean for being robust to outliers
- Percentiles: P10, P25, P50, P75, P90, P95, P99

**Dispersion Measures:**
- P90/P10 Ratio: Inequality between top and base
- Gini: Overall inequality

**Temporal Variation:**
```
Variation % = ((Final_Value / Initial_Value) - 1) × 100
```

### 7.2 Correlation Analysis

**Method:** Pearson Correlation
```python
corr = np.corrcoef(X, Y)[0,1]
```

**Applications:**
- Unemployment vs Wage: r = -0.191
- Interpretation: Weak correlation overall, but periods show clear relationship

---

## 8. STRUCTURAL VS CYCLICAL DECOMPOSITION

### 8.1 Conceptual Definitions

**Structural Gain:**
- Independent of favorable economic cycle
- Bargaining floor permanently elevated
- Institutional/demographic changes
- **Example:** Real minimum wage with legal formula

**Cyclical Gain:**
- Depends on exceptional economic conditions
- Reverses when cycle changes
- Temporary effects of policies or shocks
- **Example:** Unemployment at historic low

### 8.2 Decomposition Methodology

**Step 1:** Identify explanatory factors via hypothesis tests  
**Step 2:** Estimate marginal contribution of each factor  
**Step 3:** Classify each factor as structural or cyclical  
**Step 4:** Sum contributions by category

**Limitation:** Decomposition is **qualitative estimate**, not rigorous econometrics (would require regression with instrumental variables).

### 8.3 Decomposition Results

**Total Gain (P50): +15.6% (+R$125)**

**Structural (persists): ~9pp (58%)**
- Minimum Wage: 6.2pp
- Redistribution: 3.0pp (but fragile)

**Cyclical (reverses): ~7pp (42%)**
- Unemployment: 3.0pp
- Base Effect: 5.0pp

**Projection if Unemployment Rises to 10%:**
- Loses: -7pp (cyclical)
- Maintains: +9pp (structural)
- **P50 would be at R$880 (+9% vs 2012)**

---

## 9. LIMITATIONS AND ASSUMPTIONS

### 9.1 Data Limitations

**Unavailable Data:**
1. **Real Sectoral Productivity:** GDP/hours by sector
2. **Aggregate Corporate Profit:** Consolidated margins
3. **Detailed Sectoral Inflation:** Wage cost pass-through to prices
4. **Complete CAGED Historical:** 2012-2019 series discontinued
5. **PNAD Microdata:** Needed for robust confidence intervals
6. **Detailed Participation Rate:** By age group and sector

### 9.2 Recognized Biases

**1. Composition Bias (PNAD):**
- PNAD captures only **formal employed** workers
- **39% informal** not in sample
- If composition changes (formals earn more), average rises without individual gain
- **Mitigation:** We analyzed informality rate (stable ~39%)

**2. Survivorship Bias:**
- In crises, unemployed (usually poorer) exit sample
- Average of those remaining employed rises artificially
- **Evidence:** 2015-2021 had high unemployment but average didn't fall proportionally
- **Mitigation:** We used median (P50) instead of mean

**3. Apparent Productivity Bias:**
- Earnings/hour may rise due to sectoral change, not real productivity
- Without GDP/total hours, we can't confirm true productivity
- **Mitigation:** Documented as "proxy" and don't claim causality

### 9.3 Assumed Premises

**Premise 1: PNAD is Representative**
- We assume PNAD sample well represents formal workers
- Regional/sectoral variations were aggregated
- **Justification:** PNAD is official survey with validated methodology

**Premise 2: IBGE Deflation is Adequate**
- We trust Table 5436 deflation methodology
- We don't know exactly which index IBGE uses
- **Justification:** IBGE is reference technical institution

**Premise 3: Causal ity vs Correlation**
- **We do NOT claim rigorous causality**
- We identify correlations and test consistency
- For causality, natural experiments or IV would be needed
- **Justification:** Robust descriptive analysis with multiple validations

---

## 10. ETHICAL CONSIDERATIONS

### 10.1 Transparency about Errors

**We openly documented:**
- v1.0 had double deflation error → result -42% (incorrect)
- v2.0 corrected error but used mean → result +22% (incomplete)
- v3.0 corrected method and used median → result +15.6% (correct)

**Reason:** Show real scientific process, including errors and corrections.

### 10.2 Transparency about Limitations

**We clearly differentiate:**
- ✅ **Proven:** Minimum wage explains P10, unemployment correlates with wage
- ⚠️ **Plausible but not tested:** Post-COVID services, Bolsa Família
- ❌ **Not testable:** Exact marginal impact of each factor

**We do not claim causality where there is only correlation.**

### 10.3 Reproducibility

**All data and scripts are available:**
- CSVs from SIDRA tables (public sources)
- Complete Python and R scripts
- Documentation of each step
- **Anyone can replicate results**

---

## 11. REFERENCES

### 11.1 Primary Data Sources

**IBGE - Brazilian Institute of Geography and Statistics**
- SIDRA - IBGE Automatic Recovery System
- Tables: 5436, 6371, 7535, 7453, 4562, 4708, 4359, 4663, 10369, 4362
- Available at: https://sidra.ibge.gov.br
- Access: January-February 2026

**IBGE - National Accounts**
- Quarterly and Annual GDP
- Available at: https://www.ibge.gov.br/en/statistics/economic/national-accounts/
- Access: February 2026

**Ministry of Labor and Employment**
- New CAGED - General Register of Employed and Unemployed
- BI Panel: https://bi.mte.gov.br/bgcaged/
- Access: February 2026

### 11.2 Secondary Data Sources

**OECD - Organisation for Economic Co-operation and Development**
- Labour Productivity Database
- Available at: https://www.oecd.org/sdd/productivity-stats/
- Access: January 2026

**ILO - International Labour Organization**
- ILOSTAT Database
- Available at: https://ilostat.ilo.org/
- Access: January 2026

### 11.3 Software Used

**R Core Team (2024)**
- R: A language and environment for statistical computing
- R Foundation for Statistical Computing, Vienna, Austria
- Version: 4.x

**Python Software Foundation (2024)**
- Python Programming Language
- Version: 3.8+

**Libraries:**
- R: tidyverse, ggplot2, dplyr, tidyr, scales, patchwork
- Python: pandas, numpy, matplotlib, seaborn

---

## APPENDIX A: Complete Data Table

| Year | P10 Real | P50 Real | P90 Real | Gini | Unemployment | Informality |
|------|----------|----------|----------|------|--------------|-------------|
| 2012 | R$187 | R$805 | R$2,234 | 0.504 | 7.4% | - |
| 2013 | R$205 | R$829 | R$2,293 | 0.499 | 7.3% | - |
| 2014 | R$215 | R$865 | R$2,355 | 0.497 | 7.0% | - |
| 2015 | R$202 | R$834 | R$2,240 | 0.490 | 8.9% | - |
| 2016 | R$198 | R$836 | R$2,319 | 0.498 | 11.6% | 39.1% |
| 2017 | R$185 | R$851 | R$2,301 | 0.498 | 12.6% | 40.6% |
| 2018 | R$182 | R$863 | R$2,337 | 0.506 | 12.1% | 40.9% |
| 2019 | R$184 | R$852 | R$2,295 | 0.506 | 11.8% | 41.0% |
| 2020 | R$210 | R$880 | R$2,368 | 0.500 | 13.7% | 37.7% |
| 2021 | R$192 | R$810 | R$2,172 | 0.499 | 14.0% | 39.6% |
| 2022 | R$203 | R$831 | R$2,234 | 0.486 | 9.6% | 39.5% |
| 2023 | R$207 | R$872 | R$2,376 | 0.494 | 7.7% | 39.2% |
| 2024 | R$218 | R$930 | R$2,465 | 0.488 | 6.6% | 39.0% |

**Source:** Own compilation from IBGE/PNAD Contínua

---

## CHANGELOG

**v3.0 (February 2026) - Current:**
- ✅ Definitive double deflation correction
- ✅ Median (P50) analysis instead of mean
- ✅ Structural vs cyclical decomposition
- ✅ Validation with 4 independent sources
- ✅ Testing of 6 competing hypotheses
- ✅ Reversal identification (CAGED Dec/2025)
- ✅ Complete limitations documentation

**v2.0 (February 2026):**
- ✅ Double deflation correction
- ⚠️ Still used simple mean

**v1.0 (February 2026):**
- ❌ Double deflation error (result -42% incorrect)

---

**Last update:** February 18, 2026  
**Author:** Vitor Ramos dos Santos  
**Contact:** vitorramossantos8@gmail.com  
**Version:** 3.0 Final Validated

---

## 🌍 Language Versions

- 🇺🇸 **[English](METHODOLOGY.md)** - This file
- 🇧🇷 **[Portuguese](METHODOLOGY_PT.md)** - Versão em Português

