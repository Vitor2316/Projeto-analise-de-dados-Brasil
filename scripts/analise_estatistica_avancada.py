"""
================================================================================
ANÁLISE ESTATÍSTICA AVANÇADA - SALÁRIOS BRASIL 2012-2025
Regressão, Intervalos de Confiança, Feature Engineering
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Configuração
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# DADOS
# ============================================================================

anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                 2020, 2021, 2022, 2023, 2024])

p50_real = np.array([805, 829, 865, 834, 836, 851, 863, 852, 
                     880, 810, 831, 872, 930])

desemprego = np.array([7.4, 7.3, 7.0, 8.9, 11.6, 12.6, 12.1, 11.8, 
                       13.7, 14.0, 9.6, 7.7, 6.6])

part_trabalho = np.array([68.1, 67.8, 65.9, 70.2, 71.6, 71.6, 71.4, 74.2, 
                          67.1, 66.6, 69.4, 70.4, 73.7])

pib_real_indice = np.array([100, 103.0, 103.5, 99.8, 96.5, 97.7, 99.5, 100.7, 
                            96.8, 101.7, 104.8, 107.8, 111.2])

# ============================================================================
# 1. REGRESSÃO LINEAR: DESEMPREGO vs SALÁRIO
# ============================================================================

print("="*80)
print("1. REGRESSÃO: DESEMPREGO → SALÁRIO")
print("="*80)

# Preparar dados
X = desemprego.reshape(-1, 1)
y = p50_real

# Ajustar modelo
model_desemp = LinearRegression()
model_desemp.fit(X, y)

# Predições
y_pred = model_desemp.predict(X)

# Métricas
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Coeficientes
coef = model_desemp.coef_[0]
intercept = model_desemp.intercept_

# Intervalo de confiança (95%)
n = len(y)
residuos = y - y_pred
std_residuos = np.std(residuos)
t_crit = stats.t.ppf(0.975, n-2)  # 95% confiança, n-2 graus liberdade

# IC para coeficiente
x_mean = np.mean(X)
x_var = np.sum((X - x_mean)**2)
se_coef = std_residuos / np.sqrt(x_var)
ic_coef = (coef - t_crit*se_coef, coef + t_crit*se_coef)

print(f"\nModelo: Salário = {intercept:.2f} + {coef:.2f} × Desemprego")
print(f"\nR² = {r2:.3f}")
print(f"RMSE = R${rmse:.2f}")
print(f"\nCoeficiente: {coef:.2f}")
print(f"Intervalo Confiança 95%: [{ic_coef[0]:.2f}, {ic_coef[1]:.2f}]")
print(f"\nInterpretação:")
print(f"  Cada 1pp de AUMENTO no desemprego → R${abs(coef):.2f} de QUEDA no salário")
print(f"  Com 95% de confiança, o impacto está entre R${abs(ic_coef[1]):.2f} e R${abs(ic_coef[0]):.2f}")

# Teste de significância (p-valor)
t_stat = coef / se_coef
p_valor = 2 * (1 - stats.t.cdf(abs(t_stat), n-2))
print(f"\np-valor: {p_valor:.4f}")
if p_valor < 0.05:
    print(f"  → ESTATISTICAMENTE SIGNIFICATIVO (p < 0.05)")
else:
    print(f"  → NÃO significativo (p >= 0.05)")

# ============================================================================
# 2. QUEBRA ESTRUTURAL: ANTES vs DEPOIS DE 2021
# ============================================================================

print("\n" + "="*80)
print("2. TESTE DE QUEBRA ESTRUTURAL (2012-2021 vs 2022-2024)")
print("="*80)

# Dividir períodos
periodo1_anos = anos[anos <= 2021]
periodo1_salario = p50_real[anos <= 2021]

periodo2_anos = anos[anos >= 2022]
periodo2_salario = p50_real[anos >= 2022]

# Regressão período 1
X1 = periodo1_anos.reshape(-1, 1)
y1 = periodo1_salario
model1 = LinearRegression().fit(X1, y1)
tendencia1 = model1.coef_[0]

# Regressão período 2
X2 = periodo2_anos.reshape(-1, 1)
y2 = periodo2_salario
model2 = LinearRegression().fit(X2, y2)
tendencia2 = model2.coef_[0]

print(f"\nPeríodo 2012-2021:")
print(f"  Tendência: R${tendencia1:+.2f}/ano")
print(f"  Crescimento total: {((periodo1_salario[-1]/periodo1_salario[0])-1)*100:.1f}%")

print(f"\nPeríodo 2022-2024:")
print(f"  Tendência: R${tendencia2:+.2f}/ano")
print(f"  Crescimento total: {((periodo2_salario[-1]/periodo2_salario[0])-1)*100:.1f}%")

print(f"\nDiferença de tendência: R${abs(tendencia2 - tendencia1):.2f}/ano")
print(f"Aceleração: {(tendencia2/tendencia1):.1f}x mais rápida no período recente")

# ============================================================================
# 3. FEATURE ENGINEERING: VOLATILIDADE
# ============================================================================

print("\n" + "="*80)
print("3. FEATURE ENGINEERING: VOLATILIDADE SALARIAL")
print("="*80)

# Variação ano a ano
variacao_anual = np.diff(p50_real) / p50_real[:-1] * 100

# Volatilidade (desvio padrão das variações)
volatilidade_total = np.std(variacao_anual)

# Volatilidade por período
vol_2012_2019 = np.std(variacao_anual[:7])
vol_2020_2024 = np.std(variacao_anual[7:])

print(f"\nVolatilidade geral: {volatilidade_total:.2f}%")
print(f"\nPor período:")
print(f"  2012-2019: {vol_2012_2019:.2f}%")
print(f"  2020-2024: {vol_2020_2024:.2f}%")
print(f"  Aumento: {((vol_2020_2024/vol_2012_2019)-1)*100:+.1f}%")

print(f"\nInterpretação:")
if vol_2020_2024 > vol_2012_2019:
    print(f"  Mercado de trabalho ficou MAIS INSTÁVEL pós-COVID")
else:
    print(f"  Mercado de trabalho ficou MAIS ESTÁVEL pós-COVID")

# Anos de maior queda/crescimento
idx_maior_queda = np.argmin(variacao_anual)
idx_maior_crescimento = np.argmax(variacao_anual)

print(f"\nExtremos:")
print(f"  Maior queda: {anos[idx_maior_queda]+1} ({variacao_anual[idx_maior_queda]:.1f}%)")
print(f"  Maior crescimento: {anos[idx_maior_crescimento]+1} ({variacao_anual[idx_maior_crescimento]:.1f}%)")

# ============================================================================
# 4. CORRELAÇÃO MULTIVARIADA
# ============================================================================

print("\n" + "="*80)
print("4. MATRIZ DE CORRELAÇÃO")
print("="*80)

# Criar DataFrame
df_corr = pd.DataFrame({
    'Salário': p50_real,
    'Desemprego': desemprego,
    'Part.Trabalho': part_trabalho,
    'PIB': pib_real_indice
})

# Matriz de correlação
corr_matrix = df_corr.corr()

print("\nCorrelações:")
print(corr_matrix)

print(f"\nInterpretações principais:")
print(f"  Salário vs Desemprego: {corr_matrix.loc['Salário', 'Desemprego']:.3f}")
print(f"    → Correlação NEGATIVA {'forte' if abs(corr_matrix.loc['Salário', 'Desemprego']) > 0.5 else 'moderada'}")

print(f"\n  Salário vs Part.Trabalho: {corr_matrix.loc['Salário', 'Part.Trabalho']:.3f}")
print(f"    → Correlação {'POSITIVA' if corr_matrix.loc['Salário', 'Part.Trabalho'] > 0 else 'NEGATIVA'}")

print(f"\n  Salário vs PIB: {corr_matrix.loc['Salário', 'PIB']:.3f}")
print(f"    → Correlação {'forte' if abs(corr_matrix.loc['Salário', 'PIB']) > 0.7 else 'moderada'}")

# ============================================================================
# 5. SALVAR ANÁLISES
# ============================================================================

# Salvar resultados
resultados = {
    'regressao_desemprego': {
        'coeficiente': coef,
        'intercept': intercept,
        'r2': r2,
        'p_valor': p_valor,
        'ic_95': ic_coef
    },
    'quebra_estrutural': {
        'tendencia_2012_2021': tendencia1,
        'tendencia_2022_2024': tendencia2,
        'aceleracao': tendencia2/tendencia1
    },
    'volatilidade': {
        'geral': volatilidade_total,
        '2012_2019': vol_2012_2019,
        '2020_2024': vol_2020_2024
    }
}

# DataFrame para exportar
df_export = pd.DataFrame({
    'ano': anos,
    'p50_real': p50_real,
    'desemprego': desemprego,
    'variacao_anual_%': np.concatenate([[np.nan], variacao_anual])
})

df_export.to_csv('../dados/analise_estatistica_avancada.csv', index=False)

print("\n" + "="*80)
print("✅ ANÁLISE COMPLETA!")
print("="*80)
print("\nArquivo gerado: analise_estatistica_avancada.csv")
print("\nPróximo passo: Previsão 2026-2030")

