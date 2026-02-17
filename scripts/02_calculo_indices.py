"""
==============================================================================
SCRIPT: Cálculo de Índices com Inflação Composta
Autor: Vitor Ramos dos Santos
Data: Fevereiro 2026
==============================================================================
"""

import pandas as pd
import numpy as np

# DADOS DE INFLAÇÃO ANUAL (IPCA) ==========================================

ipca_anual = {
    2012: 5.84, 2013: 5.91, 2014: 6.41, 2015: 10.67,
    2016: 6.29, 2017: 2.95, 2018: 3.75, 2019: 4.31,
    2020: 4.52, 2021: 10.06, 2022: 5.79, 2023: 4.62,
    2024: 4.83, 2025: 4.26
}

# FUNÇÃO: CALCULAR DEFLATOR COM INFLAÇÃO COMPOSTA =========================

def calcular_deflator_composto(ipca_dict, n_trimestres=55):
    """
    Calcula deflator trimestral usando inflação COMPOSTA (não linear).
    
    Fórmula: inflacao_trimestral = (1 + inflacao_anual) ^ (1/4) - 1
    """
    deflator = [100.0]  # Base 2012 Q1
    ano_atual = 2012
    
    for i in range(1, n_trimestres):
        # Determina qual ano estamos
        ano = 2012 + (i // 4)
        
        if ano in ipca_dict:
            inflacao_anual = ipca_dict[ano] / 100
            # INFLAÇÃO COMPOSTA (CORRETO)
            inflacao_trimestral = (1 + inflacao_anual) ** (1/4) - 1
            
            # Aplica ao deflator
            deflator.append(deflator[-1] * (1 + inflacao_trimestral))
    
    return deflator

# CARREGAR DADOS LIMPOS ====================================================

dados = pd.read_csv('dados_brasil_limpos.csv')

# CALCULAR DEFLATOR ========================================================

deflator = calcular_deflator_composto(ipca_anual, len(dados))

# ADICIONAR AO DATAFRAME ===================================================

dados['deflator'] = deflator

# CALCULAR SALÁRIO REAL ====================================================

dados['salario_real'] = (dados['rendimento'] / dados['deflator']) * 100

# CALCULAR ÍNDICES BASE 2012 = 100 =========================================

# Salário real
salario_real_base = dados['salario_real'].iloc[0]
dados['salario_real_indice'] = (dados['salario_real'] / salario_real_base) * 100

# Rendimento por hora
rendimento_hora_base = dados['rendimento_hora'].iloc[0]
dados['rendimento_hora_indice'] = (dados['rendimento_hora'] / rendimento_hora_base) * 100

# CRIAR DADOS ANUAIS (AGREGAÇÃO) ===========================================

dados_anual = dados.groupby('ano').agg({
    'salario_real_indice': 'mean',
    'rendimento_hora_indice': 'mean'
}).reset_index()

dados_anual = dados_anual.round(1)

# SALVAR RESULTADOS =========================================================

dados.to_csv('brasil_trimestral_corrigido.csv', index=False)
dados_anual.to_csv('brasil_anual.csv', index=False)

print("✓ Índices calculados com sucesso!")
print(f"\nVariação 2012-2025:")
print(f"  Salário Real: {dados['salario_real_indice'].iloc[-1] - 100:+.1f}%")
print(f"  Rendimento/Hora: {dados['rendimento_hora_indice'].iloc[-1] - 100:+.1f}%")
