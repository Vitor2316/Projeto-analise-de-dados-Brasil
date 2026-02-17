"""
==============================================================================
SCRIPT: Teste de Robustez Metodológica
Autor: Vitor Ramos dos Santos
Data: Fevereiro 2026
==============================================================================
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("TESTE DE ROBUSTEZ: Comparação Método Trimestral vs Anual Direto")
print("=" * 80)

# MÉTODO 1: Trimestral → Anual (usado no estudo) ==========================

dados_trim = pd.read_csv('brasil_trimestral_corrigido.csv')
metodo1_anual = dados_trim.groupby('ano').agg({
    'salario_real_indice': 'mean',
    'rendimento_hora_indice': 'mean'
}).reset_index()
metodo1_anual.columns = ['ano', 'salario_real_m1', 'rendimento_hora_m1']

# MÉTODO 2: Direto Anual ===================================================

# Dados anuais brutos
rendimento_anual = [36552, 37308, 37728, 36000, 37188, 37548, 37896, 38640,
                    35988, 37668, 38280, 38496, 42000, 42864]

horas_anual = [40.35, 39.93, 39.68, 39.33, 39.18, 39.03, 39.18, 39.08,
               39.08, 39.05, 39.05, 39.18, 39.23, 39.15]

ipca_anual = {
    2012: 5.84, 2013: 5.91, 2014: 6.41, 2015: 10.67,
    2016: 6.29, 2017: 2.95, 2018: 3.75, 2019: 4.31,
    2020: 4.52, 2021: 10.06, 2022: 5.79, 2023: 4.62,
    2024: 4.83, 2025: 4.26
}

anos = list(range(2012, 2026))

# Deflator anual
deflator_anual = [100.0]
for i in range(1, len(anos)):
    ano = anos[i]
    inflacao = ipca_anual[ano] / 100
    deflator_anual.append(deflator_anual[-1] * (1 + inflacao))

# Salário real
salario_real_anual = [(rendimento_anual[i] / deflator_anual[i]) * 100 
                      for i in range(len(anos))]
salario_real_indice_m2 = [(x / salario_real_anual[0]) * 100 
                           for x in salario_real_anual]

# Rendimento/hora
rendimento_hora_anual = [rendimento_anual[i] / (horas_anual[i] * 4.33) 
                         for i in range(len(anos))]
rendimento_hora_indice_m2 = [(x / rendimento_hora_anual[0]) * 100 
                              for x in rendimento_hora_anual]

metodo2_anual = pd.DataFrame({
    'ano': anos,
    'salario_real_m2': salario_real_indice_m2,
    'rendimento_hora_m2': rendimento_hora_indice_m2
})

# COMPARAÇÃO ================================================================

comparacao = pd.merge(metodo1_anual, metodo2_anual, on='ano')

# Diferenças absolutas
comparacao['diff_salario_abs'] = comparacao['salario_real_m1'] - comparacao['salario_real_m2']
comparacao['diff_rendimento_abs'] = comparacao['rendimento_hora_m1'] - comparacao['rendimento_hora_m2']

# Diferenças relativas (%)
comparacao['diff_salario_rel'] = (comparacao['diff_salario_abs'] / comparacao['salario_real_m2'].abs()) * 100
comparacao['diff_rendimento_rel'] = (comparacao['diff_rendimento_abs'] / comparacao['rendimento_hora_m2']) * 100

# RESULTADOS ================================================================

print("\nESTATÍSTICAS DE DIFERENÇA:")
print(f"\nSALÁRIO REAL:")
print(f"  Diferença absoluta média: {comparacao['diff_salario_abs'].abs().mean():.2f} pontos")
print(f"  Diferença relativa média: {comparacao['diff_salario_rel'].abs().mean():.2f}%")

print(f"\nRENDIMENTO/HORA:")
print(f"  Diferença absoluta média: {comparacao['diff_rendimento_abs'].abs().mean():.2f} pontos")
print(f"  Diferença relativa média: {comparacao['diff_rendimento_rel'].abs().mean():.2f}%")

print("\n" + "=" * 80)
print("VARIAÇÃO TOTAL 2012-2025:")
print(f"\nMÉTODO 1 (Trimestral→Anual):")
print(f"  Salário Real: {comparacao['salario_real_m1'].iloc[-1] - 100:+.1f}%")
print(f"  Rendimento/Hora: {comparacao['rendimento_hora_m1'].iloc[-1] - 100:+.1f}%")

print(f"\nMÉTODO 2 (Direto Anual):")
print(f"  Salário Real: {comparacao['salario_real_m2'].iloc[-1] - 100:+.1f}%")
print(f"  Rendimento/Hora: {comparacao['rendimento_hora_m2'].iloc[-1] - 100:+.1f}%")

# Diferença final absoluta e relativa
diff_sal_final_abs = abs(comparacao['salario_real_m1'].iloc[-1] - comparacao['salario_real_m2'].iloc[-1])
diff_sal_final_rel = (diff_sal_final_abs / abs(comparacao['salario_real_m2'].iloc[-1])) * 100

diff_rend_final_abs = abs(comparacao['rendimento_hora_m1'].iloc[-1] - comparacao['rendimento_hora_m2'].iloc[-1])
diff_rend_final_rel = (diff_rend_final_abs / comparacao['rendimento_hora_m2'].iloc[-1]) * 100

print(f"\nDIFERENÇA ENTRE MÉTODOS:")
print(f"  Salário Real: {diff_sal_final_abs:.2f}pp (relativa: {diff_sal_final_rel:.1f}%)")
print(f"  Rendimento/Hora: {diff_rend_final_abs:.2f}pp (relativa: {diff_rend_final_rel:.1f}%)")

# SALVAR ====================================================================

comparacao.to_csv('teste_robustez.csv', index=False)
print("\n✓ Arquivo salvo: teste_robustez.csv")
print("=" * 80)
