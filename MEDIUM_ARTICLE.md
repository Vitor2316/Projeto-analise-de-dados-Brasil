# Brazilian Wage Gains Were Built on Squeezed Profits — And the Reversal Has Begun

## A data-driven investigation reveals the uncomfortable truth behind Brazil's 2022-2024 "wage boom"

Published: February 2026  
Author: Vitor Ramos dos Santos  
Reading time: 12 minutes

---

## The Headline Everyone Celebrated

"Brazilian workers saw real wage gains of +15.6% between 2012-2024, with inequality falling."

Politicians from across the spectrum claimed credit. Economists praised the recovery. Headlines celebrated the return of purchasing power.

But when you decompose the data, a different picture emerges.

## The Uncomfortable Discovery

After analyzing 14 years of wage data from Brazil's National Household Survey (PNAD Contínua), cross-validating with employment statistics (CAGED), and building econometric models, I found something that contradicts the prevailing narrative:

**The wage gains of 2022-2024 were financed not by productivity growth, but by compressing corporate profit margins. And December 2025 data confirms the reversal has already begun.**

## The Evidence

### 1. Labor Captured 5.6 Percentage Points of GDP

Between 2012 and 2024, labor's share of GDP rose from 68.1% to 73.7% — an increase of 5.6 percentage points.

In a R$11.7 trillion economy, that's approximately R$655 billion per year that shifted from capital (corporate profits) to labor (wages).

This wasn't organic growth. This was redistribution.

### 2. The "Boom" Was Really a Recovery

Looking at the median worker (P50):
- 2012: R$805 (base)
- 2021: R$810 (same as 2012 after 9 years!)
- 2024: R$930 (+15.6% vs 2012)

Translation: Workers spent 10 years recovering from the 2015-2021 crisis, then gained 14.8% in just 3 years.

Half the "gain" was just getting back to where they should have been.

### 3. December 2025: The Prediction Validated

In my analysis (completed before December 2025 data was released), I wrote:

> "If unemployment rises and the economy decelerates, companies will restore margins by cutting jobs. The cyclical component (42% of gains) will reverse."

December 2025 employment data: **-618,000 jobs**

Services sector (which drove 2022-2024 growth): **-281,000 jobs**

The reversal has begun.

## The Decomposition

I broke down the +15.6% gain into structural (permanent) and cyclical (reversible) components:

**Structural (58% — will persist):**
- Real minimum wage policy: +6.2pp (formula: inflation + past GDP growth)
- Redistribution: +3.0pp (labor captured more of GDP)

**Cyclical (42% — now reversing):**
- Historic low unemployment: +3.0pp (6.6% is unsustainable)
- Base effect: +5.0pp (recovery from 2021 crisis)

## Why This Matters

### For Workers
The gains were real, but fragile. Approximately 42% depends on maintaining:
- Unemployment at 6.6% (a historical minimum)
- Compressed profit margins (unsustainable long-term)

If unemployment rises to 8-10%, workers lose roughly 7 percentage points but keep the 9pp structural gains.

Bottom line: Median wage likely falls from R$930 to ~R$870-880 (still +8-9% above 2012).

### For Companies
Profit margins were squeezed by 5.6pp of GDP to finance wage growth. Facing:
- High labor costs (wages growing faster than productivity)
- High credit costs (Selic at 14.75%)
- Slowing demand

December 2025 shows companies making their move: cutting headcount to restore margins.

### For Policy Makers
The minimum wage formula worked — it created a structural floor. But the cyclical gains (pleno emprego effect) are reversing. The question becomes: can policy interventions stabilize employment without reigniting inflation?

## The Methodology

This analysis uses:
- **Primary data:** IBGE PNAD Contínua (13 years, national household survey)
- **Validation:** CAGED employment data, National Accounts, minimum wage records
- **Statistical methods:** Linear regression, Monte Carlo simulation (10,000 scenarios), sensitivity analysis
- **Transparency:** All code and data publicly available on GitHub

Key findings survived:
- 6 hypothesis tests
- 4 independent data validations  
- Structural break analysis (pre/post-2021)
- Real-time prediction validation (December 2025 confirmed forecast)

## The Monte Carlo Simulation

To quantify uncertainty, I ran 10,000 simulations varying:
- Unemployment rate (5-15%)
- GDP growth (-2% to +5%)
- Inflation (3-10%)
- Real minimum wage gains (0-5%)

Results:
- Expected 2026 median wage: R$914 (range: R$870-960)
- Probability of decline vs 2024: 47%
- Probability of decline >5%: 18%

Translation: Roughly even odds of small decline, but structural gains prevent catastrophic falls.

## The Stress Tests

I tested four extreme scenarios:

**1. Severe Crisis (Unemployment 12%, GDP -2%, Inflation 8%)**
Result: Wage falls to R$827 (-11.1%)

**2. Stagflation (Unemployment 10%, GDP 0%, Inflation 7%)**
Result: Wage falls to R$869 (-6.6%)

**3. Unsustainable Boom (Unemployment 5%, GDP 4%, Inflation 6%)**
Result: Wage rises to R$975 (+4.8%)

**4. Recessionary Adjustment (Unemployment 9%, GDP 0.5%, Inflation 5%)**
Result: Wage falls to R$902 (-3.0%)

December 2025 data suggests we're entering scenario 2 or 4.

## The Dashboard

I built an interactive dashboard where you can simulate your own scenarios:

[Link to Streamlit Dashboard]

Adjust sliders for:
- Unemployment rate
- GDP growth
- Inflation
- Minimum wage policy

See real-time impact on projected wages, with decomposition showing contribution of each factor.

## The Uncomfortable Conclusion

Most analysts will say: "Wages rose +15.6%!"

The data says: "Wages rose +15.6%, but 42% of that gain came from squeezing profits at unsustainable low unemployment. December 2025 shows the reversal beginning. Structural gains (~9%) will persist, but cyclical gains (~7%) are evaporating."

This doesn't fit neat political narratives. It's not "workers winning" or "workers losing" — it's a complex redistribution under specific conditions that are now changing.

## What's Next

I'll be monitoring:
- Monthly CAGED data (employment by sector)
- PNAD quarterly releases (wage evolution)
- Central Bank signals (Selic trajectory)
- Government response (will minimum wage formula hold?)

The model predicts median wage stabilizing around R$870-880 by 2027 if unemployment normalizes to 8-9%. Let's see if the data confirms.

## Explore Further

- **Full Report (52 pages):** [Link to GitHub]
- **Interactive Dashboard:** [Link to Streamlit]
- **Complete Methodology:** [Link to GitHub]
- **Source Code:** [Link to GitHub]
- **Raw Data:** All publicly available (IBGE SIDRA, Ministry of Labor)

---

**About the Author**

Vitor Ramos dos Santos is a student in a technical high school program in computer science. This research was conducted independently using public data sources. All code and methodology are open source.

**Contact:** vitorramossantos8@gmail.com  
**LinkedIn:** www.linkedin.com/in/vitor-ramos2132  
**GitHub:** https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil

---

**Acknowledgments**

Data sources: IBGE (PNAD Contínua, National Accounts), Brazilian Ministry of Labor (CAGED), OECD Labour Productivity Database.

**Disclaimer**

This analysis represents the author's interpretation of publicly available data. It does not constitute financial, legal, or investment advice. Economic projections involve uncertainty; actual outcomes may differ.

---

**If you found this analysis valuable, please share it and follow for updates as the economic situation evolves.**

