"""
================================================================================
GRÁFICOS AVANÇADOS (11-14) - ANÁLISE SALÁRIOS BRASIL
Complemento ao gerar_graficos_v3.py
================================================================================
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import os

# Criar diretório se não existir
os.makedirs('../graficos', exist_ok=True)

# Configuração
plt.style.use('seaborn-v0_8-whitegrid')

CORES = {
    'verde': '#2ECC71',
    'vermelho': '#E74C3C',
    'azul': '#3498DB',
    'amarelo': '#F39C12',
    'cinza': '#95A5A6'
}

# Dados
anos_hist = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
p50_hist = np.array([805, 829, 865, 834, 836, 851, 863, 852, 880, 810, 831, 872, 930])

# ============================================================================
# GRÁFICO 11: PREVISÃO 2026-2030 (MÚLTIPLOS MODELOS)
# ============================================================================

print("Gerando gráfico 11: Previsão 2026-2030...")

anos_fut = np.array([2025, 2026, 2027, 2028, 2029, 2030])

# Cenários
pessimista = np.array([911, 874, 856, 846, 846, 856])
base = np.array([930, 911, 902, 911, 921, 930])
otimista = np.array([949, 976, 1004, 1032, 1060, 1088])

fig, ax = plt.subplots(figsize=(14, 8))

# Histórico
ax.plot(anos_hist, p50_hist, 'o-', linewidth=3, markersize=8, 
        label='Histórico (2012-2024)', color=CORES['azul'], zorder=5)

# Cenários
ax.plot(anos_fut, pessimista, 'v-', linewidth=2, label='Pessimista (30%)', 
        color=CORES['vermelho'])
ax.plot(anos_fut, base, 's-', linewidth=2, label='Base (50%)', 
        color=CORES['amarelo'])
ax.plot(anos_fut, otimista, '^-', linewidth=2, label='Otimista (20%)', 
        color=CORES['verde'])

# Linha divisória
ax.axvline(2024.5, color='red', linestyle=':', linewidth=2, alpha=0.5)
ax.text(2024.5, 750, 'Previsão →', ha='center', fontsize=11, 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

ax.set_xlabel('Ano', fontsize=13, fontweight='bold')
ax.set_ylabel('Salário Real Mediana (R$ de 2012)', fontsize=13, fontweight='bold')
ax.set_title('Previsão Salário Real 2026-2030: Múltiplos Cenários', 
             fontsize=16, fontweight='bold', pad=20)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_ylim(750, 1100)

plt.tight_layout()
plt.savefig('../graficos/11_previsao_2026_2030.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Gráfico 11 criado")

# ============================================================================
# GRÁFICO 12: ANÁLISE DE SENSIBILIDADE
# ============================================================================

print("Gerando gráfico 12: Análise de sensibilidade...")

BASE = 930

def calc_salario(desemp, pib, infl, sm):
    impacto = -2.0*(desemp-6.6) + 0.3*pib + 0.4*sm - 0.5*(infl-3.0)
    return BASE * (1 + impacto/100)

# Ranges
desemp_range = np.linspace(5, 12, 50)
pib_range = np.linspace(-1, 4, 50)
infl_range = np.linspace(3, 8, 50)
sm_range = np.linspace(0, 4, 50)

# Calcular impactos
sal_desemp = [calc_salario(d, 2.0, 5.5, 2.0) for d in desemp_range]
sal_pib = [calc_salario(7.0, p, 5.5, 2.0) for p in pib_range]
sal_infl = [calc_salario(7.0, 2.0, i, 2.0) for i in infl_range]
sal_sm = [calc_salario(7.0, 2.0, 5.5, s) for s in sm_range]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].plot(desemp_range, sal_desemp, linewidth=2, color=CORES['vermelho'])
axes[0, 0].axhline(BASE, linestyle='--', color='gray', alpha=0.5)
axes[0, 0].axvline(7.0, linestyle=':', color='black', alpha=0.3)
axes[0, 0].set_xlabel('Taxa de Desemprego (%)', fontweight='bold')
axes[0, 0].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[0, 0].set_title('Sensibilidade ao Desemprego', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(pib_range, sal_pib, linewidth=2, color=CORES['verde'])
axes[0, 1].axhline(BASE, linestyle='--', color='gray', alpha=0.5)
axes[0, 1].axvline(2.0, linestyle=':', color='black', alpha=0.3)
axes[0, 1].set_xlabel('Crescimento PIB (%)', fontweight='bold')
axes[0, 1].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[0, 1].set_title('Sensibilidade ao PIB', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].plot(infl_range, sal_infl, linewidth=2, color=CORES['amarelo'])
axes[1, 0].axhline(BASE, linestyle='--', color='gray', alpha=0.5)
axes[1, 0].axvline(5.5, linestyle=':', color='black', alpha=0.3)
axes[1, 0].set_xlabel('Inflação (%)', fontweight='bold')
axes[1, 0].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[1, 0].set_title('Sensibilidade à Inflação', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].plot(sm_range, sal_sm, linewidth=2, color=CORES['azul'])
axes[1, 1].axhline(BASE, linestyle='--', color='gray', alpha=0.5)
axes[1, 1].axvline(2.0, linestyle=':', color='black', alpha=0.3)
axes[1, 1].set_xlabel('Ganho Real Salário Mínimo (%)', fontweight='bold')
axes[1, 1].set_ylabel('Salário Real 2026 (R$)', fontweight='bold')
axes[1, 1].set_title('Sensibilidade ao Salário Mínimo', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../graficos/12_analise_sensibilidade.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Gráfico 12 criado")

# ============================================================================
# GRÁFICO 13: MONTE CARLO (HISTOGRAMA)
# ============================================================================

print("Gerando gráfico 13: Monte Carlo...")

# Simulação simplificada
np.random.seed(42)
n = 10000

desemp = np.clip(np.random.normal(7.5, 1.5, n), 5, 15)
pib = np.clip(np.random.normal(2.0, 1.0, n), -2, 5)
infl = np.clip(np.random.normal(5.5, 1.0, n), 3, 10)
sm = np.clip(np.random.normal(2.0, 0.8, n), 0, 5)

salarios = [calc_salario(desemp[i], pib[i], infl[i], sm[i]) for i in range(n)]
salarios = np.array(salarios)

fig, ax = plt.subplots(figsize=(12, 7))

ax.hist(salarios, bins=50, color=CORES['azul'], alpha=0.7, edgecolor='black')
ax.axvline(np.mean(salarios), color='red', linestyle='--', linewidth=2, 
           label=f'Média: R${np.mean(salarios):.0f}')
ax.axvline(np.percentile(salarios, 5), color='orange', linestyle=':', linewidth=2, 
           label=f'P5: R${np.percentile(salarios, 5):.0f}')
ax.axvline(np.percentile(salarios, 95), color='orange', linestyle=':', linewidth=2, 
           label=f'P95: R${np.percentile(salarios, 95):.0f}')
ax.axvline(BASE, color='green', linestyle='-', linewidth=2, 
           label=f'Base 2024: R${BASE}')

ax.set_xlabel('Salário Real 2026 (R$)', fontweight='bold', fontsize=12)
ax.set_ylabel('Frequência', fontweight='bold', fontsize=12)
ax.set_title('Distribuição de Resultados - Monte Carlo (10.000 Simulações)', 
             fontweight='bold', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../graficos/13_monte_carlo.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Gráfico 13 criado")

# ============================================================================
# GRÁFICO 14: MATRIZ DE CENÁRIOS (HEATMAP)
# ============================================================================

print("Gerando gráfico 14: Matriz de cenários...")

desemp_grid = [6, 7, 8, 9, 10]
infl_grid = [4, 5, 6, 7, 8]

matriz = np.zeros((len(infl_grid), len(desemp_grid)))

for i, infl in enumerate(infl_grid):
    for j, desemp in enumerate(desemp_grid):
        matriz[i, j] = calc_salario(desemp, 2.0, infl, 2.0)

fig, ax = plt.subplots(figsize=(10, 8))

im = ax.imshow(matriz, cmap='RdYlGn', aspect='auto')

ax.set_xticks(np.arange(len(desemp_grid)))
ax.set_yticks(np.arange(len(infl_grid)))
ax.set_xticklabels([f'{d}%' for d in desemp_grid])
ax.set_yticklabels([f'{i}%' for i in infl_grid])

ax.set_xlabel('Taxa de Desemprego', fontweight='bold', fontsize=12)
ax.set_ylabel('Inflação Anual', fontweight='bold', fontsize=12)
ax.set_title('Matriz de Cenários: Salário Real 2026 (R$)', 
             fontweight='bold', fontsize=14, pad=20)

# Valores nas células
for i in range(len(infl_grid)):
    for j in range(len(desemp_grid)):
        text = ax.text(j, i, f'R${matriz[i, j]:.0f}',
                      ha="center", va="center", color="black", fontweight='bold')

# Colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Salário Real (R$)', fontweight='bold')

plt.tight_layout()
plt.savefig('../graficos/14_matriz_cenarios.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Gráfico 14 criado")

print("\n" + "="*70)
print("✓ TODOS OS 4 GRÁFICOS AVANÇADOS CRIADOS COM SUCESSO!")
print("="*70)
print("\nArquivos gerados:")
print("  - 11_previsao_2026_2030.png")
print("  - 12_analise_sensibilidade.png")
print("  - 13_monte_carlo.png")
print("  - 14_matriz_cenarios.png")

