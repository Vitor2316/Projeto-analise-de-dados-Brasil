"""
================================================================================
SIMULADOR AVANÇADO DE CENÁRIOS ECONÔMICOS
Análise de Sensibilidade + Monte Carlo + Stress Testing
================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuração
np.random.seed(42)
plt.style.use('seaborn-v0_8-whitegrid')

# ============================================================================
# PARÂMETROS DO MODELO
# ============================================================================

print("="*80)
print("SIMULADOR AVANÇADO: ANÁLISE DE SENSIBILIDADE")
print("="*80)

# Base
salario_base_2024 = 930

# Elasticidades (baseadas na análise de regressão)
ELASTICIDADE_DESEMPREGO = -2.0  # Cada 1pp desemprego → -2% salário
ELASTICIDADE_PIB = 0.3          # Cada 1% PIB → +0.3% salário
ELASTICIDADE_SM = 0.4           # SM explica 40% do movimento de P50
ELASTICIDADE_INFLACAO = -0.5    # Inflação acima meta corrói ganhos

# ============================================================================
# FUNÇÃO: SIMULAR SALÁRIO 2026
# ============================================================================

def simular_salario_2026(desemprego, pib, inflacao, sm_real, base=salario_base_2024):
    """
    Simula salário 2026 baseado em drivers macroeconômicos
    
    Parâmetros:
    -----------
    desemprego : float - Taxa de desemprego (%)
    pib : float - Crescimento PIB (%)
    inflacao : float - Inflação anual (%)
    sm_real : float - Ganho real salário mínimo (%)
    base : float - Salário base 2024
    
    Retorna:
    --------
    float - Salário projetado 2026
    """
    
    # Impactos
    impacto_desemp = ELASTICIDADE_DESEMPREGO * (desemprego - 6.6)
    impacto_pib = ELASTICIDADE_PIB * pib
    impacto_sm = ELASTICIDADE_SM * sm_real
    impacto_inflacao = ELASTICIDADE_INFLACAO * (inflacao - 3.0)
    
    # Total
    impacto_total = impacto_desemp + impacto_pib + impacto_sm + impacto_inflacao
    
    return base * (1 + impacto_total/100)

# ============================================================================
# 1. ANÁLISE DE SENSIBILIDADE: UM FATOR POR VEZ
# ============================================================================

print("\n1. ANÁLISE DE SENSIBILIDADE (Ceteris Paribus)")
print("-" * 60)

# Cenário base
desemp_base = 7.0
pib_base = 2.0
infl_base = 5.5
sm_base = 2.0

# Testar desemprego
desemp_range = np.linspace(5, 12, 50)
salarios_desemp = [simular_salario_2026(d, pib_base, infl_base, sm_base) 
                   for d in desemp_range]

# Testar PIB
pib_range = np.linspace(-1, 4, 50)
salarios_pib = [simular_salario_2026(desemp_base, p, infl_base, sm_base) 
                for p in pib_range]

# Testar inflação
infl_range = np.linspace(3, 8, 50)
salarios_infl = [simular_salario_2026(desemp_base, pib_base, i, sm_base) 
                 for i in infl_range]

# Testar SM
sm_range = np.linspace(0, 4, 50)
salarios_sm = [simular_salario_2026(desemp_base, pib_base, infl_base, s) 
               for s in sm_range]

# Gráfico de sensibilidade
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].plot(desemp_range, salarios_desemp, linewidth=2, color='#E74C3C')
axes[0, 0].axhline(salario_base_2024, linestyle='--', color='gray', alpha=0.5)
axes[0, 0].axvline(desemp_base, linestyle=':', color='black', alpha=0.3)
axes[0, 0].set_xlabel('Taxa de Desemprego (%)', fontweight='bold')
axes[0, 0].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[0, 0].set_title('Sensibilidade ao Desemprego', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(pib_range, salarios_pib, linewidth=2, color='#2ECC71')
axes[0, 1].axhline(salario_base_2024, linestyle='--', color='gray', alpha=0.5)
axes[0, 1].axvline(pib_base, linestyle=':', color='black', alpha=0.3)
axes[0, 1].set_xlabel('Crescimento PIB (%)', fontweight='bold')
axes[0, 1].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[0, 1].set_title('Sensibilidade ao PIB', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].plot(infl_range, salarios_infl, linewidth=2, color='#F39C12')
axes[1, 0].axhline(salario_base_2024, linestyle='--', color='gray', alpha=0.5)
axes[1, 0].axvline(infl_base, linestyle=':', color='black', alpha=0.3)
axes[1, 0].set_xlabel('Inflação (%)', fontweight='bold')
axes[1, 0].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[1, 0].set_title('Sensibilidade à Inflação', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].plot(sm_range, salarios_sm, linewidth=2, color='#3498DB')
axes[1, 1].axhline(salario_base_2024, linestyle='--', color='gray', alpha=0.5)
axes[1, 1].axvline(sm_base, linestyle=':', color='black', alpha=0.3)
axes[1, 1].set_xlabel('Ganho Real Salário Mínimo (%)', fontweight='bold')
axes[1, 1].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[1, 1].set_title('Sensibilidade ao Salário Mínimo', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../graficos/12_analise_sensibilidade.png', dpi=300, 
            bbox_inches='tight', facecolor='white')
plt.close()

print("✅ Gráfico de sensibilidade gerado: 12_analise_sensibilidade.png")

# Calcular sensibilidade numérica
print("\nSensibilidade Numérica:")
print(f"  Desemprego: Variação de 5% → 12% causa R${salarios_desemp[-1] - salarios_desemp[0]:.0f} de queda")
print(f"  PIB: Variação de -1% → +4% causa R${salarios_pib[-1] - salarios_pib[0]:.0f} de ganho")
print(f"  Inflação: Variação de 3% → 8% causa R${salarios_infl[-1] - salarios_infl[0]:.0f} de perda")
print(f"  SM: Variação de 0% → 4% causa R${salarios_sm[-1] - salarios_sm[0]:.0f} de ganho")

# ============================================================================
# 2. SIMULAÇÃO MONTE CARLO: 10.000 CENÁRIOS
# ============================================================================

print("\n" + "="*80)
print("2. SIMULAÇÃO MONTE CARLO (10.000 Cenários)")
print("="*80)

n_simulacoes = 10000

# Distribuições dos parâmetros (baseado em ranges plausíveis)
desemp_sim = np.random.normal(7.5, 1.5, n_simulacoes)  # média 7.5%, sd 1.5%
pib_sim = np.random.normal(2.0, 1.0, n_simulacoes)     # média 2%, sd 1%
infl_sim = np.random.normal(5.5, 1.0, n_simulacoes)    # média 5.5%, sd 1%
sm_sim = np.random.normal(2.0, 0.8, n_simulacoes)      # média 2%, sd 0.8%

# Truncar valores irrealistas
desemp_sim = np.clip(desemp_sim, 5, 15)
pib_sim = np.clip(pib_sim, -2, 5)
infl_sim = np.clip(infl_sim, 3, 10)
sm_sim = np.clip(sm_sim, 0, 5)

# Simular salários
salarios_simulados = []
for i in range(n_simulacoes):
    sal = simular_salario_2026(desemp_sim[i], pib_sim[i], infl_sim[i], sm_sim[i])
    salarios_simulados.append(sal)

salarios_simulados = np.array(salarios_simulados)

# Estatísticas
media = np.mean(salarios_simulados)
mediana = np.median(salarios_simulados)
std = np.std(salarios_simulados)
p5 = np.percentile(salarios_simulados, 5)
p95 = np.percentile(salarios_simulados, 95)

print(f"\nDistribuição de Resultados (10.000 simulações):")
print(f"  Média: R${media:.0f}")
print(f"  Mediana: R${mediana:.0f}")
print(f"  Desvio Padrão: R${std:.0f}")
print(f"  Intervalo 90% (P5-P95): R${p5:.0f} - R${p95:.0f}")

# Probabilidades
prob_queda = (salarios_simulados < salario_base_2024).sum() / n_simulacoes * 100
prob_ganho = (salarios_simulados > salario_base_2024).sum() / n_simulacoes * 100
prob_queda_forte = (salarios_simulados < salario_base_2024 * 0.95).sum() / n_simulacoes * 100

print(f"\nProbabilidades:")
print(f"  Queda vs 2024: {prob_queda:.1f}%")
print(f"  Ganho vs 2024: {prob_ganho:.1f}%")
print(f"  Queda >5%: {prob_queda_forte:.1f}%")

# Histograma
fig, ax = plt.subplots(figsize=(12, 7))

ax.hist(salarios_simulados, bins=50, color='#3498DB', alpha=0.7, edgecolor='black')
ax.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Média: R${media:.0f}')
ax.axvline(p5, color='orange', linestyle=':', linewidth=2, label=f'P5: R${p5:.0f}')
ax.axvline(p95, color='orange', linestyle=':', linewidth=2, label=f'P95: R${p95:.0f}')
ax.axvline(salario_base_2024, color='green', linestyle='-', linewidth=2, 
           label=f'Base 2024: R${salario_base_2024}')

ax.set_xlabel('Salário Real 2026 (R$)', fontweight='bold', fontsize=12)
ax.set_ylabel('Frequência', fontweight='bold', fontsize=12)
ax.set_title('Distribuição de Resultados - Monte Carlo (10.000 Simulações)', 
             fontweight='bold', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../graficos/13_monte_carlo.png', dpi=300, 
            bbox_inches='tight', facecolor='white')
plt.close()

print("\n✅ Gráfico Monte Carlo gerado: 13_monte_carlo.png")

# ============================================================================
# 3. STRESS TEST: CENÁRIOS EXTREMOS
# ============================================================================

print("\n" + "="*80)
print("3. STRESS TEST: Cenários Extremos")
print("="*80)

stress_scenarios = {
    'Crise Severa': {
        'desemprego': 12.0,
        'pib': -2.0,
        'inflacao': 8.0,
        'sm_real': 0.0
    },
    'Estagflação': {
        'desemprego': 10.0,
        'pib': 0.0,
        'inflacao': 7.0,
        'sm_real': 1.0
    },
    'Boom Insustentável': {
        'desemprego': 5.0,
        'pib': 4.0,
        'inflacao': 6.0,
        'sm_real': 3.0
    },
    'Ajuste Recessivo': {
        'desemprego': 9.0,
        'pib': 0.5,
        'inflacao': 5.0,
        'sm_real': 1.5
    }
}

print("\nResultados Stress Test:")
stress_results = []

for nome, params in stress_scenarios.items():
    sal = simular_salario_2026(
        params['desemprego'],
        params['pib'],
        params['inflacao'],
        params['sm_real']
    )
    var = ((sal / salario_base_2024) - 1) * 100
    
    stress_results.append({
        'Cenário': nome,
        'Salário': sal,
        'Variação (%)': var,
        'Desemprego': params['desemprego'],
        'PIB': params['pib'],
        'Inflação': params['inflacao']
    })
    
    print(f"\n  {nome}:")
    print(f"    Salário 2026: R${sal:.0f} ({var:+.1f}%)")
    print(f"    Premissas: Desemp {params['desemprego']}% | PIB {params['pib']:+.1f}% | " 
          f"Infl {params['inflacao']}%")

df_stress = pd.DataFrame(stress_results)
df_stress.to_csv('../dados/stress_test_resultados.csv', index=False)

# ============================================================================
# 4. MATRIZ DE CENÁRIOS: DESEMPREGO vs INFLAÇÃO
# ============================================================================

print("\n" + "="*80)
print("4. MATRIZ DE CENÁRIOS: Desemprego vs Inflação")
print("="*80)

# Grid
desemp_grid = [6, 7, 8, 9, 10]
infl_grid = [4, 5, 6, 7, 8]

matriz = np.zeros((len(infl_grid), len(desemp_grid)))

for i, infl in enumerate(infl_grid):
    for j, desemp in enumerate(desemp_grid):
        matriz[i, j] = simular_salario_2026(desemp, pib_base, infl, sm_base)

# Heatmap
fig, ax = plt.subplots(figsize=(10, 8))

im = ax.imshow(matriz, cmap='RdYlGn', aspect='auto')

# Configurar eixos
ax.set_xticks(np.arange(len(desemp_grid)))
ax.set_yticks(np.arange(len(infl_grid)))
ax.set_xticklabels([f'{d}%' for d in desemp_grid])
ax.set_yticklabels([f'{i}%' for i in infl_grid])

ax.set_xlabel('Taxa de Desemprego', fontweight='bold', fontsize=12)
ax.set_ylabel('Inflação Anual', fontweight='bold', fontsize=12)
ax.set_title('Matriz de Cenários: Salário Real 2026 (R$)', 
             fontweight='bold', fontsize=14, pad=20)

# Adicionar valores
for i in range(len(infl_grid)):
    for j in range(len(desemp_grid)):
        text = ax.text(j, i, f'R${matriz[i, j]:.0f}',
                      ha="center", va="center", color="black", fontweight='bold')

# Colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Salário Real (R$)', fontweight='bold')

plt.tight_layout()
plt.savefig('../graficos/14_matriz_cenarios.png', dpi=300, 
            bbox_inches='tight', facecolor='white')
plt.close()

print("\n✅ Matriz de cenários gerada: 14_matriz_cenarios.png")

# ============================================================================
# SALVAR RESULTADOS
# ============================================================================

# Salvar simulação Monte Carlo
df_monte_carlo = pd.DataFrame({
    'desemprego': desemp_sim,
    'pib': pib_sim,
    'inflacao': infl_sim,
    'sm_real': sm_sim,
    'salario_2026': salarios_simulados
})

df_monte_carlo.to_csv('../dados/monte_carlo_10k.csv', index=False)

# Resumo estatístico
resumo = {
    'estatistica': ['Média', 'Mediana', 'Desvio Padrão', 'P5', 'P95', 
                    'Prob. Queda', 'Prob. Ganho', 'Prob. Queda >5%'],
    'valor': [media, mediana, std, p5, p95, prob_queda, prob_ganho, prob_queda_forte]
}

df_resumo = pd.DataFrame(resumo)
df_resumo.to_csv('../dados/monte_carlo_resumo.csv', index=False)

print("\n" + "="*80)
print("✅ SIMULAÇÃO COMPLETA!")
print("="*80)
print("\nArquivos gerados:")
print("  - 12_analise_sensibilidade.png")
print("  - 13_monte_carlo.png")
print("  - 14_matriz_cenarios.png")
print("  - monte_carlo_10k.csv")
print("  - monte_carlo_resumo.csv")
print("  - stress_test_resultados.csv")

