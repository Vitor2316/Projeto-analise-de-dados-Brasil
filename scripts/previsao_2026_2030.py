"""
================================================================================
PREVISÃO SALÁRIOS BRASIL 2026-2030
Múltiplos modelos + Cenários + Intervalos de confiança
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# DADOS HISTÓRICOS
# ============================================================================

anos_historico = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                           2020, 2021, 2022, 2023, 2024])

p50_historico = np.array([805, 829, 865, 834, 836, 851, 863, 852, 
                          880, 810, 831, 872, 930])

# ============================================================================
# MODELO 1: TENDÊNCIA LINEAR (2012-2024)
# ============================================================================

print("="*80)
print("PREVISÃO 2026-2030: MÚLTIPLOS MODELOS")
print("="*80)

# Anos para prever
anos_futuros = np.array([2025, 2026, 2027, 2028, 2029, 2030])

# Modelo linear completo
X_hist = anos_historico.reshape(-1, 1)
y_hist = p50_historico

model_total = LinearRegression()
model_total.fit(X_hist, y_hist)

# Previsão
X_fut = anos_futuros.reshape(-1, 1)
previsao_linear = model_total.predict(X_fut)

# Intervalo de confiança
n = len(y_hist)
y_pred_hist = model_total.predict(X_hist)
residuos = y_hist - y_pred_hist
std_residuos = np.std(residuos)

# IC 95%
t_crit = stats.t.ppf(0.975, n-2)
margem_erro = t_crit * std_residuos * np.sqrt(1 + 1/n + (X_fut - X_hist.mean())**2 / ((X_hist - X_hist.mean())**2).sum())

ic_lower = previsao_linear - margem_erro.flatten()
ic_upper = previsao_linear + margem_erro.flatten()

print("\n1. MODELO LINEAR (TENDÊNCIA 2012-2024)")
print("-" * 60)
print(f"Crescimento médio: R${model_total.coef_[0]:.2f}/ano")
print(f"\nPrevisões:")
for i, ano in enumerate(anos_futuros):
    print(f"  {ano}: R${previsao_linear[i]:.0f} (IC 95%: R${ic_lower[i]:.0f} - R${ic_upper[i]:.0f})")

# ============================================================================
# MODELO 2: TENDÊNCIA RECENTE (2022-2024)
# ============================================================================

# Usar apenas período recente
anos_recente = anos_historico[-3:]
p50_recente = p50_historico[-3:]

X_rec = anos_recente.reshape(-1, 1)
y_rec = p50_recente

model_recente = LinearRegression()
model_recente.fit(X_rec, y_rec)

previsao_recente = model_recente.predict(X_fut)

print("\n2. MODELO RECENTE (TENDÊNCIA 2022-2024)")
print("-" * 60)
print(f"Crescimento médio: R${model_recente.coef_[0]:.2f}/ano")
print(f"\nPrevisões:")
for i, ano in enumerate(anos_futuros):
    print(f"  {ano}: R${previsao_recente[i]:.0f}")

# ============================================================================
# MODELO 3: CENÁRIOS BASEADOS EM DRIVERS ECONÔMICOS
# ============================================================================

print("\n3. CENÁRIOS MACROECONÔMICOS")
print("-" * 60)

# Base: 2024
base_2024 = 930

# Cenário Pessimista
# Premissas: desemprego sobe para 10%, inflação 7%, PIB +0.5%
# Impacto: perde ~7pp (componente conjuntural)
cenario_pessimista = {
    2025: base_2024 * 0.98,  # -2%
    2026: base_2024 * 0.94,  # -6%
    2027: base_2024 * 0.92,  # -8%
    2028: base_2024 * 0.91,  # -9%
    2029: base_2024 * 0.91,  # -9%
    2030: base_2024 * 0.92,  # -8% (leve recuperação)
}

# Cenário Base
# Premissas: desemprego 7-8%, inflação 5.5%, PIB +2%
# Impacto: queda moderada, depois estabiliza
cenario_base = {
    2025: base_2024 * 1.00,  # estável
    2026: base_2024 * 0.98,  # -2%
    2027: base_2024 * 0.97,  # -3%
    2028: base_2024 * 0.98,  # -2%
    2029: base_2024 * 0.99,  # -1%
    2030: base_2024 * 1.00,  # volta ao nível
}

# Cenário Otimista
# Premissas: desemprego 5.5%, inflação 4%, PIB +3%
# Impacto: crescimento retoma
cenario_otimista = {
    2025: base_2024 * 1.02,  # +2%
    2026: base_2024 * 1.05,  # +5%
    2027: base_2024 * 1.08,  # +8%
    2028: base_2024 * 1.11,  # +11%
    2029: base_2024 * 1.14,  # +14%
    2030: base_2024 * 1.17,  # +17%
}

print("\nCenário PESSIMISTA (Prob: 30%)")
print("  Premissas: Desemprego 10%, Inflação 7%, PIB +0.5%")
for ano in anos_futuros:
    var = ((cenario_pessimista[ano]/base_2024) - 1) * 100
    print(f"  {ano}: R${cenario_pessimista[ano]:.0f} ({var:+.1f}% vs 2024)")

print("\nCenário BASE (Prob: 50%)")
print("  Premissas: Desemprego 7-8%, Inflação 5.5%, PIB +2%")
for ano in anos_futuros:
    var = ((cenario_base[ano]/base_2024) - 1) * 100
    print(f"  {ano}: R${cenario_base[ano]:.0f} ({var:+.1f}% vs 2024)")

print("\nCenário OTIMISTA (Prob: 20%)")
print("  Premissas: Desemprego 5.5%, Inflação 4%, PIB +3%")
for ano in anos_futuros:
    var = ((cenario_otimista[ano]/base_2024) - 1) * 100
    print(f"  {ano}: R${cenario_otimista[ano]:.0f} ({var:+.1f}% vs 2024)")

# ============================================================================
# PREVISÃO ESPERADA (MÉDIA PONDERADA)
# ============================================================================

print("\n4. PREVISÃO ESPERADA (Média Ponderada por Probabilidade)")
print("-" * 60)

previsao_esperada = {}
for ano in anos_futuros:
    esperado = (0.30 * cenario_pessimista[ano] + 
                0.50 * cenario_base[ano] + 
                0.20 * cenario_otimista[ano])
    previsao_esperada[ano] = esperado
    var = ((esperado/base_2024) - 1) * 100
    print(f"  {ano}: R${esperado:.0f} ({var:+.1f}% vs 2024)")

# ============================================================================
# SALVAR PREVISÕES
# ============================================================================

df_previsoes = pd.DataFrame({
    'ano': anos_futuros,
    'linear_total': previsao_linear.flatten(),
    'linear_recente': previsao_recente.flatten(),
    'ic_95_lower': ic_lower,
    'ic_95_upper': ic_upper,
    'pessimista': [cenario_pessimista[a] for a in anos_futuros],
    'base': [cenario_base[a] for a in anos_futuros],
    'otimista': [cenario_otimista[a] for a in anos_futuros],
    'esperado': [previsao_esperada[a] for a in anos_futuros]
})

df_previsoes.to_csv('../dados/previsoes_2026_2030.csv', index=False)

# ============================================================================
# GRÁFICO DE PREVISÃO
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))

# Histórico
ax.plot(anos_historico, p50_historico, 'o-', linewidth=3, markersize=8, 
        label='Histórico (2012-2024)', color='#2E86C1', zorder=5)

# Modelo linear
ax.plot(anos_futuros, previsao_linear, '--', linewidth=2, 
        label='Tendência Linear (2012-2024)', color='gray', alpha=0.7)

# IC
ax.fill_between(anos_futuros, ic_lower, ic_upper, alpha=0.2, color='gray', 
                label='Intervalo Confiança 95%')

# Cenários
ax.plot(anos_futuros, [cenario_pessimista[a] for a in anos_futuros], 
        'v-', linewidth=2, label='Pessimista (30%)', color='#E74C3C')
ax.plot(anos_futuros, [cenario_base[a] for a in anos_futuros], 
        's-', linewidth=2, label='Base (50%)', color='#F39C12')
ax.plot(anos_futuros, [cenario_otimista[a] for a in anos_futuros], 
        '^-', linewidth=2, label='Otimista (20%)', color='#2ECC71')

# Esperado
ax.plot(anos_futuros, [previsao_esperada[a] for a in anos_futuros], 
        'D-', linewidth=3, markersize=8, label='Esperado (ponderado)', 
        color='#9B59B6', zorder=4)

# Linha divisória
ax.axvline(2024.5, color='red', linestyle=':', linewidth=2, alpha=0.5)
ax.text(2024.5, 750, 'Previsão →', ha='center', fontsize=11, 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

ax.set_xlabel('Ano', fontsize=13, fontweight='bold')
ax.set_ylabel('Salário Real Mediana (R$ de 2012)', fontsize=13, fontweight='bold')
ax.set_title('Previsão Salário Real 2026-2030: Múltiplos Cenários', 
             fontsize=16, fontweight='bold', pad=20)
ax.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_ylim(750, 1100)

plt.tight_layout()
plt.savefig('../graficos/11_previsao_2026_2030.png', dpi=300, bbox_inches='tight', 
            facecolor='white')
plt.close()

print("\n" + "="*80)
print("✅ PREVISÕES COMPLETAS!")
print("="*80)
print("\nArquivos gerados:")
print("  - previsoes_2026_2030.csv")
print("  - 11_previsao_2026_2030.png")
print("\nPróximo: Dashboard Streamlit interativo")

