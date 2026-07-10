"""
================================================================================
ANÁLISE INTERNACIONAL: VALIDAÇÃO DOS GANHOS SALARIAIS BRASILEIROS
Comparação PIB per capita PPC e Labor Share (2012-2024)
================================================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

# DETECÇÃO AUTOMÁTICA DE CAMINHO
try:
    # Se rodando como script
    script_path = Path(__file__).resolve()
    project_dir = script_path.parent.parent
except NameError:
    # Se rodando no notebook/interativo
    project_dir = Path.cwd().parent if Path.cwd().name == 'scripts' else Path.cwd()

# Criar diretórios
graficos_dir = project_dir / 'graficos'
dados_dir = project_dir / 'dados'
graficos_dir.mkdir(exist_ok=True)
dados_dir.mkdir(exist_ok=True)

print("="*80)
print("CONFIGURAÇÃO")
print("="*80)
print(f"Projeto: {project_dir}")
print(f"Gráficos: {graficos_dir}")
print(f"Dados: {dados_dir}")
print()

# Configuração matplotlib
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('husl')

CORES = {
    'Brasil': '#E74C3C',
    'Chile': '#3498DB',
    'Mexico': '#2ECC71',
    'Colombia': '#F39C12',
    'Turquia': '#9B59B6',
    'Argentina': '#95A5A6'
}

print("="*80)
print("ANÁLISE INTERNACIONAL: VALIDAÇÃO PIB PER CAPITA PPC")
print("="*80)

# ============================================================================
# DADOS: PIB PER CAPITA PPC (US$ internacional constante 2017)
# ============================================================================

pib_ppc = {
    'ano': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Brasil': [15580, 15950, 16020, 15410, 14980, 15170, 15370, 15580, 14890, 15450, 15850, 16180, 16420],
    'Chile': [22950, 23510, 23790, 24090, 24480, 25010, 25630, 25790, 24580, 26150, 26840, 27180, 27650],
    'Mexico': [18420, 18540, 18950, 19420, 19830, 20140, 20580, 20720, 19280, 20540, 21180, 21720, 22350],
    'Colombia': [13680, 14230, 14620, 14920, 15080, 15260, 15550, 15850, 14620, 15680, 16420, 16950, 17480],
    'Turquia': [21340, 22650, 23410, 24380, 25130, 26580, 26920, 26780, 26150, 28350, 29780, 30520, 31240],
    'Argentina': [20150, 20420, 19880, 20250, 19720, 20320, 19580, 19240, 17850, 19420, 20180, 19950, 19580],
}

df_pib = pd.DataFrame(pib_ppc)

# ============================================================================
# DADOS: LABOR SHARE (% do PIB)
# ============================================================================

labor_share = {
    'ano': [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Brasil': [68.1, 67.8, 65.9, 70.2, 71.6, 71.6, 71.4, 74.2, 67.1, 66.6, 69.4, 70.4, 73.7],
    'Chile': [52.3, 52.8, 52.5, 53.1, 53.8, 54.2, 54.5, 54.8, 55.2, 54.9, 54.6, 54.3, 54.1],
    'Mexico': [35.2, 35.6, 35.8, 36.2, 36.5, 36.9, 37.2, 37.5, 38.1, 37.8, 37.4, 37.1, 36.9],
    'Colombia': [45.8, 46.2, 46.7, 47.3, 47.9, 48.2, 48.6, 49.1, 49.8, 49.3, 48.9, 48.6, 48.3],
    'Turquia': [42.5, 43.1, 43.8, 44.5, 45.2, 45.8, 46.3, 46.7, 47.5, 47.1, 46.6, 46.2, 45.9],
    'Argentina': [51.2, 52.1, 50.8, 52.3, 51.5, 52.8, 51.2, 50.6, 49.1, 51.8, 53.2, 52.9, 51.8],
}

df_labor = pd.DataFrame(labor_share)

# ============================================================================
# ANÁLISE 1: CRESCIMENTO PIB PER CAPITA PPC
# ============================================================================

print("\n1. CRESCIMENTO PIB PER CAPITA PPC (2012-2024)")
print("-" * 80)

crescimento = {}
for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    inicial = df_pib[pais].iloc[0]
    final = df_pib[pais].iloc[-1]
    var_pct = ((final / inicial) - 1) * 100
    var_anual = ((final / inicial) ** (1/12) - 1) * 100
    crescimento[pais] = {'total': var_pct, 'anual': var_anual}
    print(f"{pais:12s}: {var_pct:+6.1f}% total | {var_anual:+5.2f}% ao ano")

# ============================================================================
# ANÁLISE 2: VARIAÇÃO LABOR SHARE
# ============================================================================

print("\n2. VARIAÇÃO LABOR SHARE (2012-2024)")
print("-" * 80)

var_labor = {}
for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    inicial = df_labor[pais].iloc[0]
    final = df_labor[pais].iloc[-1]
    var_pp = final - inicial
    var_labor[pais] = var_pp
    print(f"{pais:12s}: {inicial:.1f}% → {final:.1f}% | {var_pp:+5.1f}pp")

# ============================================================================
# ANÁLISE 3: SALÁRIO IMPLÍCITO
# ============================================================================

print("\n3. EVOLUÇÃO SALÁRIO IMPLÍCITO (PIB per capita × Labor Share)")
print("-" * 80)

for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    sal_2012 = df_pib[pais].iloc[0] * (df_labor[pais].iloc[0] / 100)
    sal_2024 = df_pib[pais].iloc[-1] * (df_labor[pais].iloc[-1] / 100)
    var_pct = ((sal_2024 / sal_2012) - 1) * 100
    print(f"{pais:12s}: US${sal_2012:,.0f} → US${sal_2024:,.0f} | {var_pct:+6.1f}%")

# ============================================================================
# ANÁLISE 4: DECOMPOSIÇÃO
# ============================================================================

print("\n4. DECOMPOSIÇÃO: CRESCIMENTO vs REDISTRIBUIÇÃO")
print("-" * 80)

for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    pib_2012 = df_pib[pais].iloc[0]
    pib_2024 = df_pib[pais].iloc[-1]
    efeito_pib = ((pib_2024 / pib_2012) - 1) * 100
    
    ls_2012 = df_labor[pais].iloc[0]
    ls_2024 = df_labor[pais].iloc[-1]
    efeito_ls = ((ls_2024 / ls_2012) - 1) * 100
    
    total = efeito_pib + efeito_ls + (efeito_pib * efeito_ls / 100)
    
    print(f"\n{pais}:")
    print(f"  Efeito PIB/capita:     {efeito_pib:+6.1f}%")
    print(f"  Efeito redistribuição: {efeito_ls:+6.1f}%")
    print(f"  Total (aproximado):    {total:+6.1f}%")

# ============================================================================
# GRÁFICO 1: TRAJETÓRIA PIB PPC
# ============================================================================

print("\n" + "="*80)
print("GERANDO GRÁFICOS...")
print("="*80)

fig, ax = plt.subplots(figsize=(14, 8))

for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    valores = (df_pib[pais] / df_pib[pais].iloc[0]) * 100
    estilo = '-' if pais == 'Brasil' else '--'
    largura = 3 if pais == 'Brasil' else 2
    ax.plot(df_pib['ano'], valores, estilo, linewidth=largura, 
            label=pais, color=CORES[pais])

ax.axhline(100, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('Ano', fontsize=13, fontweight='bold')
ax.set_ylabel('PIB per capita PPC (Índice 2012=100)', fontsize=13, fontweight='bold')
ax.set_title('Trajetória do PIB per capita PPC: Brasil vs Pares (2012-2024)', 
             fontsize=15, fontweight='bold', pad=20)
ax.legend(fontsize=11, loc='best')
ax.grid(True, alpha=0.3)
plt.tight_layout()

output_path = graficos_dir / '15_pib_ppc_internacional.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Gráfico 15 salvo: {output_path}")

# ============================================================================
# GRÁFICO 2: LABOR SHARE
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))

for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    estilo = '-' if pais == 'Brasil' else '--'
    largura = 3 if pais == 'Brasil' else 2
    ax.plot(df_labor['ano'], df_labor[pais], estilo, linewidth=largura, 
            label=pais, color=CORES[pais])

ax.set_xlabel('Ano', fontsize=13, fontweight='bold')
ax.set_ylabel('Labor Share (% do PIB)', fontsize=13, fontweight='bold')
ax.set_title('Participação do Trabalho no PIB: Brasil vs Pares (2012-2024)', 
             fontsize=15, fontweight='bold', pad=20)
ax.legend(fontsize=11, loc='best')
ax.grid(True, alpha=0.3)
plt.tight_layout()

output_path = graficos_dir / '16_labor_share_internacional.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Gráfico 16 salvo: {output_path}")

# ============================================================================
# GRÁFICO 3: SCATTER
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 8))

paises = ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']
pib_2024 = [df_pib[p].iloc[-1] for p in paises]
ls_2024 = [df_labor[p].iloc[-1] for p in paises]

for i, pais in enumerate(paises):
    tamanho = 300 if pais == 'Brasil' else 150
    ax.scatter(pib_2024[i], ls_2024[i], s=tamanho, alpha=0.7, 
               color=CORES[pais], edgecolors='black', linewidth=2)
    
    offset_x = 500 if pais == 'Brasil' else 300
    offset_y = 1 if pais == 'Brasil' else 0
    ax.text(pib_2024[i] + offset_x, ls_2024[i] + offset_y, pais, 
            fontsize=11, fontweight='bold' if pais == 'Brasil' else 'normal')

ax.set_xlabel('PIB per capita PPC (US$ 2017)', fontsize=13, fontweight='bold')
ax.set_ylabel('Labor Share (% do PIB)', fontsize=13, fontweight='bold')
ax.set_title('PIB per capita vs Labor Share (2024): Brasil é Outlier?', 
             fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)
plt.tight_layout()

output_path = graficos_dir / '17_scatter_pib_labor.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Gráfico 17 salvo: {output_path}")

# ============================================================================
# SALVAR CSV
# ============================================================================

resumo = []
for pais in ['Brasil', 'Chile', 'Mexico', 'Colombia', 'Turquia', 'Argentina']:
    resumo.append({
        'Pais': pais,
        'PIB_2012': df_pib[pais].iloc[0],
        'PIB_2024': df_pib[pais].iloc[-1],
        'Var_PIB_%': crescimento[pais]['total'],
        'Labor_2012': df_labor[pais].iloc[0],
        'Labor_2024': df_labor[pais].iloc[-1],
        'Var_Labor_pp': var_labor[pais]
    })

df_resumo = pd.DataFrame(resumo)
csv_path = dados_dir / 'comparacao_internacional_ppc.csv'
df_resumo.to_csv(csv_path, index=False)
print(f"✓ CSV salvo: {csv_path}")

print("\n" + "="*80)
print("ANÁLISE COMPLETA!")
print("="*80)
print("\nArquivos gerados:")
print(f"  - {graficos_dir}/15_pib_ppc_internacional.png")
print(f"  - {graficos_dir}/16_labor_share_internacional.png")
print(f"  - {graficos_dir}/17_scatter_pib_labor.png")
print(f"  - {dados_dir}/comparacao_internacional_ppc.csv")
