"""
============================================================================
GERADOR DE GRÁFICOS - ANÁLISE SALÁRIOS BRASIL 2012-2025 (V3.0)
Versão Final Validada
Autor: Vitor Ramos dos Santos
============================================================================
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from matplotlib import rcParams

# Configuração global
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
rcParams['font.size'] = 11
rcParams['figure.dpi'] = 300

# Paleta de cores profissional
CORES = {
    'verde': '#2ECC71',
    'vermelho': '#E74C3C',
    'azul': '#3498DB',
    'amarelo': '#F39C12',
    'cinza': '#95A5A6',
    'cinza_claro': '#ECF0F1'
}

def formatar_reais(x, pos):
    """Formatar valores em reais"""
    return f'R${x:.0f}'

def formatar_mil(x, pos):
    """Formatar milhares"""
    return f'{x:.0f} mil'

# ============================================================================
# GRÁFICO 1: TRAJETÓRIA DO TRABALHADOR TÍPICO
# ============================================================================

def grafico_1_trajetoria():
    anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                     2020, 2021, 2022, 2023, 2024, 2025])
    p50 = np.array([805, 829, 865, 834, 836, 851, 863, 852, 
                    880, 810, 831, 872, 930, 938])
    
    # Marcos históricos
    marcos = {
        2014: ('Pico\nR$865', 865),
        2016: ('Impeachment', 836),
        2020: ('COVID-19', 880),
        2021: ('Vale\nR$810\n(= 2012)', 810),
        2023: ('Lula 3', 872)
    }
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Linha principal
    ax.plot(anos, p50, color=CORES['azul'], linewidth=3, marker='o', 
            markersize=8, label='Salário Real Mediana')
    
    # Linha de referência 2012
    ax.axhline(805, color=CORES['cinza'], linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(2012.5, 805, 'Nível de 2012', va='bottom', color=CORES['cinza'], 
            fontsize=10, weight='bold')
    
    # Marcos históricos
    for ano, (label, y) in marcos.items():
        ax.plot(ano, y, 'D', color=CORES['vermelho'], markersize=12, zorder=5)
        ax.text(ano, y, f'\n{label}', ha='center', va='bottom', 
                fontsize=9, weight='bold', color=CORES['vermelho'])
    
    ax.set_xlabel('Ano', fontsize=13, weight='bold')
    ax.set_ylabel('Salário Real Mensal (R$ de 2012)', fontsize=13, weight='bold')
    ax.set_title('Trajetória do Trabalhador Típico (Mediana)', 
                 fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, '10 anos perdidos (2012-2021), recuperação em 3 anos (2022-2024)',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    ax.yaxis.set_major_formatter(FuncFormatter(formatar_reais))
    ax.set_xticks(anos)
    ax.set_xticklabels(anos, rotation=45, ha='right')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_ylim(790, 950)
    
    plt.figtext(0.99, 0.01, 'Fonte: IBGE/PNAD Contínua | Autor: Vitor Ramos dos Santos',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('01_trajetoria_trabalhador_tipico.png', dpi=300, bbox_inches='tight', 
                facecolor='white')
    plt.close()
    print("✅ Gráfico 1: Trajetória criado")

# ============================================================================
# GRÁFICO 2: DECOMPOSIÇÃO ESTRUTURAL vs CONJUNTURAL
# ============================================================================

def grafico_2_decomposicao():
    componentes = ['Salário\nMínimo', 'Redistribuição', 'Desemprego\nBaixo', 'Efeito\nBase']
    valores = [6.2, 3.0, 3.0, 5.0]
    cores_barras = [CORES['verde'], CORES['verde'], CORES['amarelo'], CORES['amarelo']]
    tipos = ['Estrutural\n(58%)', 'Estrutural\n(58%)', 
             'Conjuntural\n(42%)', 'Conjuntural\n(42%)']
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars = ax.bar(componentes, valores, color=cores_barras, width=0.6, 
                  edgecolor='white', linewidth=2)
    
    # Valores nas barras
    for i, (bar, val) in enumerate(zip(bars, valores)):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.3, 
                f'+{val:.1f}pp', ha='center', fontsize=13, weight='bold')
    
    ax.set_ylabel('Contribuição (pontos percentuais)', fontsize=13, weight='bold')
    ax.set_title('Decomposição dos Ganhos Salariais (+15.6%)', 
                 fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, '58% estrutural (permanece) vs 42% conjuntural (reverte)',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    # Legenda customizada
    verde_patch = mpatches.Patch(color=CORES['verde'], label='Estrutural (permanente)')
    amarelo_patch = mpatches.Patch(color=CORES['amarelo'], label='Conjuntural (temporário)')
    ax.legend(handles=[verde_patch, amarelo_patch], loc='upper right', 
              fontsize=11, frameon=True, shadow=True)
    
    ax.set_ylim(0, 7.5)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 
                'Total: 9pp estrutural + 7pp conjuntural = +15.6% (arredondado)\nFonte: Análise própria com dados IBGE/PNAD',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('02_decomposicao_estrutural_conjuntural.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 2: Decomposição criado")

# ============================================================================
# GRÁFICO 3: GANHOS PROGRESSIVOS
# ============================================================================

def grafico_3_progressivo():
    percentis = ['P10\n(10% mais\npobres)', 'P50\n(Mediana)', 
                 'P90\n(10% mais\nricos)', 'Salário\nMínimo']
    variacoes = [16.7, 15.6, 10.3, 18.5]
    cores_barras = [CORES['verde'], CORES['azul'], CORES['vermelho'], CORES['cinza']]
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars = ax.bar(percentis, variacoes, color=cores_barras, width=0.6,
                  edgecolor='white', linewidth=2)
    
    for bar, val in zip(bars, variacoes):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, 
                f'+{val:.1f}%', ha='center', fontsize=14, weight='bold')
    
    ax.set_ylabel('Variação Real 2012-2024 (%)', fontsize=13, weight='bold')
    ax.set_title('Ganhos Foram Progressivos', fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, 'Base cresceu mais (+16.7%) que topo (+10.3%) | Desigualdade caiu',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    ax.set_ylim(0, 21)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 'Fonte: IBGE/PNAD Contínua - Tabela 7535 (percentis)',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('03_ganhos_progressivos_percentis.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 3: Ganhos Progressivos criado")

# ============================================================================
# GRÁFICO 4: PARTICIPAÇÃO DO TRABALHO NO PIB
# ============================================================================

def grafico_4_participacao_pib():
    anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                     2020, 2021, 2022, 2023, 2024])
    trabalho = np.array([68.1, 67.8, 65.9, 70.2, 71.6, 71.6, 71.4, 74.2, 
                         67.1, 66.6, 69.4, 70.4, 73.7])
    capital = 100 - trabalho
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    ax.fill_between(anos, 0, trabalho, color=CORES['verde'], alpha=0.3, 
                    label='Participação do Trabalho (Salários)')
    ax.fill_between(anos, trabalho, 100, color=CORES['cinza'], alpha=0.3,
                    label='Participação do Capital (Lucros)')
    
    ax.plot(anos, trabalho, color=CORES['verde'], linewidth=3, marker='o', markersize=7)
    ax.plot(anos, 100-trabalho, color=CORES['cinza'], linewidth=3, marker='s', markersize=7)
    
    # Anotações
    ax.annotate('Trabalho capturou\n+5.6pp do PIB', xy=(2018, 50), 
                fontsize=13, weight='bold', color=CORES['verde'],
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                         edgecolor=CORES['verde'], linewidth=2))
    
    ax.annotate('Lucros\ncomprimidos', xy=(2018, 15), 
                fontsize=11, weight='bold', color=CORES['cinza'],
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                         edgecolor=CORES['cinza'], linewidth=2))
    
    ax.set_xlabel('Ano', fontsize=13, weight='bold')
    ax.set_ylabel('% do PIB', fontsize=13, weight='bold')
    ax.set_title('Redistribuição: Trabalho Ganhou do Capital', 
                 fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, 
            'Participação do trabalho subiu de 68.1% → 73.7% | Lucros caíram de 31.9% → 26.3%',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    ax.set_xticks(anos)
    ax.set_xticklabels(anos, rotation=45, ha='right')
    ax.set_ylim(0, 100)
    ax.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 
                'Ganhos salariais vieram de compressão de margens empresariais\nFonte: Cálculo próprio com dados IBGE e Contas Nacionais',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('04_participacao_trabalho_pib.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 4: Participação no PIB criado")

# ============================================================================
# GRÁFICO 5: DESEMPREGO vs SALÁRIO
# ============================================================================

def grafico_5_desemprego_salario():
    anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                     2020, 2021, 2022, 2023, 2024])
    desemprego = np.array([7.4, 7.3, 7.0, 8.9, 11.6, 12.6, 12.1, 11.8, 
                           13.7, 14.0, 9.6, 7.7, 6.6])
    p50 = np.array([805, 829, 865, 834, 836, 851, 863, 852, 
                    880, 810, 831, 872, 930])
    
    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    # Área de crise
    ax1.axvspan(2015, 2021, alpha=0.1, color=CORES['vermelho'])
    ax1.text(2018, 15, 'Crise + COVID\n(desemprego alto)', 
             ha='center', fontsize=11, color=CORES['vermelho'], weight='bold')
    
    # Eixo 1: Desemprego
    color1 = CORES['vermelho']
    ax1.set_xlabel('Ano', fontsize=13, weight='bold')
    ax1.set_ylabel('Taxa de Desemprego (%)', fontsize=13, weight='bold', color=color1)
    ax1.plot(anos, desemprego, color=color1, linewidth=3, marker='o', 
             markersize=8, label='Desemprego')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(5, 16)
    
    # Eixo 2: Salário
    ax2 = ax1.twinx()
    color2 = CORES['azul']
    ax2.set_ylabel('Salário Real Mediana (R$)', fontsize=13, weight='bold', color=color2)
    ax2.plot(anos, p50, color=color2, linewidth=3, marker='s', 
             markersize=8, label='Salário Real')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.yaxis.set_major_formatter(FuncFormatter(formatar_reais))
    ax2.set_ylim(790, 950)
    
    ax1.set_title('Desemprego Alto = Salário Baixo (Relação Inversa)', 
                  fontsize=17, weight='bold', pad=20)
    fig.text(0.5, 0.95, 'Quando desemprego sobe, trabalhador perde poder de barganha',
             ha='center', fontsize=12, color=CORES['cinza'], style='italic')
    
    ax1.set_xticks(anos)
    ax1.set_xticklabels(anos, rotation=45, ha='right')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Legenda combinada
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', 
               fontsize=11, frameon=True, shadow=True)
    
    plt.figtext(0.99, 0.01, 'Fonte: IBGE/PNAD Contínua',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('05_desemprego_vs_salario.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 5: Desemprego vs Salário criado")

# ============================================================================
# GRÁFICO 6: MASSA SALARIAL vs PIB
# ============================================================================

def grafico_6_massa_pib():
    anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                     2020, 2021, 2022, 2023, 2024])
    massa_indice = np.array([100, 105.2, 109.5, 105.4, 104.3, 104.1, 108.1, 110.2, 
                             103.8, 100.2, 106.5, 118.9, 126.5])
    pib_indice = np.array([100, 103.0, 103.5, 99.8, 96.5, 97.7, 99.5, 100.7, 
                           96.8, 101.7, 104.8, 107.8, 111.2])
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    ax.plot(anos, massa_indice, color=CORES['verde'], linewidth=3, 
            marker='o', markersize=8, label='Massa Salarial Real')
    ax.plot(anos, pib_indice, color=CORES['azul'], linewidth=3, 
            marker='s', markersize=8, label='PIB Real')
    
    # Seta mostrando gap
    ax.annotate('', xy=(2024, 126.5), xytext=(2024, 111.2),
                arrowprops=dict(arrowstyle='<->', color=CORES['vermelho'], lw=2))
    ax.text(2023, 119, 'Gap = +15pp\nRedistribuição', 
            ha='right', fontsize=12, weight='bold', color=CORES['vermelho'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', 
                     edgecolor=CORES['vermelho'], linewidth=2))
    
    ax.set_xlabel('Ano', fontsize=13, weight='bold')
    ax.set_ylabel('Índice (2012 = 100)', fontsize=13, weight='bold')
    ax.set_title('Massa Salarial Cresceu MAIS que PIB', 
                 fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, 
            'Massa +26.5% vs PIB +11.2% | Gap de 15pp = redistribuição do capital para trabalho',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    ax.set_xticks(anos)
    ax.set_xticklabels(anos, rotation=45, ha='right')
    ax.set_ylim(95, 130)
    ax.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 'Massa Salarial: IBGE Tabela 4663 | PIB: Contas Nacionais',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('06_massa_salarial_vs_pib.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 6: Massa vs PIB criado")

# ============================================================================
# GRÁFICO 7: CAGED REVERSÃO DEZ/2025
# ============================================================================

def grafico_7_caged_reversao():
    setores = ['Serviços', 'Indústria', 'Construção', 'Comércio', 'Agropecuária']
    saldos = [-280.810, -135.087, -104.077, -54.355, -43.836]
    
    fig, ax = plt.subplots(figsize=(11, 7))
    
    bars = ax.barh(setores, saldos, color=CORES['vermelho'], 
                   height=0.6, edgecolor='white', linewidth=2)
    
    for bar, val in zip(bars, saldos):
        ax.text(val - 10, bar.get_y() + bar.get_height()/2, 
                f'{val:.0f} mil', ha='right', va='center', 
                fontsize=13, weight='bold', color='white')
    
    ax.axvline(0, color=CORES['cinza'], linewidth=2)
    ax.set_xlabel('Saldo de Empregos (admissões - demissões)', 
                  fontsize=13, weight='bold')
    ax.set_title('REVERSÃO: Dezembro 2025 com -618 Mil Empregos', 
                 fontsize=17, weight='bold', pad=20, color=CORES['vermelho'])
    ax.text(0.5, 1.03, 'Serviços (motor do crescimento 2022-2024) lideram demissões',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['vermelho'], style='italic')
    
    ax.set_xlim(-300, 10)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 
                'Fonte: Novo CAGED - Ministério do Trabalho | Dados: Dezembro 2025',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('07_caged_reversao_dez2025.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 7: CAGED Reversão criado")

# ============================================================================
# GRÁFICO 8: CRIAÇÃO DE EMPREGOS (DESACELERAÇÃO)
# ============================================================================

def grafico_8_criacao_empregos():
    anos = ['2020', '2021', '2022', '2025']
    saldos = [-189, 2782, 2014, 1279]
    cores_barras = [CORES['vermelho'], CORES['verde'], CORES['verde'], CORES['amarelo']]
    
    fig, ax = plt.subplots(figsize=(11, 7))
    
    bars = ax.bar(anos, saldos, color=cores_barras, width=0.5,
                  edgecolor='white', linewidth=2)
    
    for bar, val in zip(bars, saldos):
        y_pos = val + 100 if val > 0 else val - 100
        ax.text(bar.get_x() + bar.get_width()/2, y_pos, 
                f'{val:+.0f} mil', ha='center', fontsize=14, weight='bold')
    
    ax.axhline(0, color=CORES['cinza'], linewidth=2)
    ax.set_ylabel('Saldo Acumulado de Empregos (mil)', fontsize=13, weight='bold')
    ax.set_title('Criação de Empregos em Desaceleração', 
                 fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, '2025 criou METADE do pico de 2021 | Ciclo perdendo força',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    ax.set_ylim(-500, 3000)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 'Fonte: Novo CAGED - Ministério do Trabalho',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('08_criacao_empregos_desaceleracao.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 8: Criação de Empregos criado")

# ============================================================================
# GRÁFICO 9: HORAS vs RENDIMENTO/HORA
# ============================================================================

def grafico_9_horas_produtividade():
    anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                     2020, 2021, 2022, 2023, 2024])
    horas = np.array([40.4, 40.1, 39.9, 39.5, 39.3, 39.0, 39.1, 39.2, 
                      39.2, 39.1, 39.2, 39.3, 39.3])
    rend_hora = np.array([17.33, 17.90, 17.83, 17.75, 18.12, 18.46, 18.50, 18.86, 
                          18.63, 19.20, 19.46, 20.05, 20.99])
    
    fig, ax1 = plt.subplots(figsize=(14, 8))
    
    # Eixo 1: Horas
    color1 = CORES['vermelho']
    ax1.set_xlabel('Ano', fontsize=13, weight='bold')
    ax1.set_ylabel('Horas Trabalhadas/Semana', fontsize=13, weight='bold', color=color1)
    ax1.plot(anos, horas, color=color1, linewidth=3, marker='v', 
             markersize=8, label='Horas/semana')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(38.5, 41)
    
    # Eixo 2: Rendimento/hora
    ax2 = ax1.twinx()
    color2 = CORES['verde']
    ax2.set_ylabel('Rendimento/Hora (R$)', fontsize=13, weight='bold', color=color2)
    ax2.plot(anos, rend_hora, color=color2, linewidth=3, marker='^', 
             markersize=8, label='Rendimento/hora')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.yaxis.set_major_formatter(FuncFormatter(formatar_reais))
    ax2.set_ylim(16, 22)
    
    # Anotação
    ax1.annotate('Paradoxo da\nProdutividade', xy=(2018, 42), 
                 fontsize=14, weight='bold', ha='center',
                 bbox=dict(boxstyle='round,pad=0.7', facecolor='yellow', 
                          alpha=0.3, edgecolor='black', linewidth=2))
    
    ax1.set_title('Trabalha MENOS, Produz MAIS', fontsize=17, weight='bold', pad=20)
    fig.text(0.5, 0.95, 'Horas caíram -2.7% mas rendimento/hora subiu +21%',
             ha='center', fontsize=12, color=CORES['cinza'], style='italic')
    
    ax1.set_xticks(anos)
    ax1.set_xticklabels(anos, rotation=45, ha='right')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Legenda combinada
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='center left', 
               fontsize=11, frameon=True, shadow=True)
    
    plt.figtext(0.99, 0.01, 'Fonte: IBGE/PNAD Contínua - Tabelas 10369 e 5436',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('09_horas_vs_produtividade.png', dpi=300, 
                bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 9: Horas vs Produtividade criado")

# ============================================================================
# GRÁFICO 10: PROJEÇÕES 2026
# ============================================================================

def grafico_10_projecoes():
    cenarios = ['Pessimista', 'Base', 'Otimista']
    valores = [870, 930, 960]
    probs = ['20%', '60%', '20%']
    cores_barras = [CORES['vermelho'], CORES['amarelo'], CORES['verde']]
    variacoes = [(v/930 - 1)*100 for v in valores]
    
    fig, ax = plt.subplots(figsize=(11, 8))
    
    bars = ax.bar(cenarios, valores, color=cores_barras, width=0.5,
                  edgecolor='white', linewidth=2)
    
    for i, (bar, val, var, prob) in enumerate(zip(bars, valores, variacoes, probs)):
        ax.text(bar.get_x() + bar.get_width()/2, val + 20, 
                f'R${val}\n({var:+.1f}%)', ha='center', fontsize=13, weight='bold')
        ax.text(bar.get_x() + bar.get_width()/2, 100, 
                f'Prob: {prob}', ha='center', fontsize=11, weight='bold', color='white')
    
    ax.axhline(930, color=CORES['cinza'], linestyle='--', linewidth=2)
    ax.text(2.5, 930, 'Nível 2024', va='bottom', ha='left', 
            color=CORES['cinza'], fontsize=11, weight='bold')
    
    ax.set_ylabel('Salário Real Mensal (R$ de 2012)', fontsize=13, weight='bold')
    ax.set_title('Projeções para 2026: Salário Real Mediana', 
                 fontsize=17, weight='bold', pad=20)
    ax.text(0.5, 1.03, 
            'Cenário base mais provável (60%): estabilidade | Risco assimétrico para baixo',
            transform=ax.transAxes, ha='center', fontsize=12, 
            color=CORES['cinza'], style='italic')
    
    ax.set_ylim(0, 1050)
    ax.yaxis.set_major_formatter(FuncFormatter(formatar_reais))
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.figtext(0.99, 0.01, 
                'Pessimista: Inflação 7%, PIB +0.5%, Desemprego 8.5%\n' +
                'Base: Inflação 5.5%, PIB +2%, Desemprego 7%\n' +
                'Otimista: Inflação 4%, PIB +3%, Desemprego 5.5%',
                ha='right', fontsize=8, style='italic', color=CORES['cinza'])
    
    plt.tight_layout()
    plt.savefig('10_projecoes_2026.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✅ Gráfico 10: Projeções 2026 criado")

# ============================================================================
# MAIN: GERAR TODOS OS GRÁFICOS
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*70)
    print("GERANDO TODOS OS GRÁFICOS - VERSÃO 3.0")
    print("="*70 + "\n")
    
    grafico_1_trajetoria()
    grafico_2_decomposicao()
    grafico_3_progressivo()
    grafico_4_participacao_pib()
    grafico_5_desemprego_salario()
    grafico_6_massa_pib()
    grafico_7_caged_reversao()
    grafico_8_criacao_empregos()
    grafico_9_horas_produtividade()
    grafico_10_projecoes()
    
    print("\n" + "="*70)
    print("✅ TODOS OS 10 GRÁFICOS CRIADOS COM SUCESSO!")
    print("="*70 + "\n")
    
    print("Arquivos gerados:")
    for i in range(1, 11):
        arquivos = [
            "01_trajetoria_trabalhador_tipico.png",
            "02_decomposicao_estrutural_conjuntural.png",
            "03_ganhos_progressivos_percentis.png",
            "04_participacao_trabalho_pib.png",
            "05_desemprego_vs_salario.png",
            "06_massa_salarial_vs_pib.png",
            "07_caged_reversao_dez2025.png",
            "08_criacao_empregos_desaceleracao.png",
            "09_horas_vs_produtividade.png",
            "10_projecoes_2026.png"
        ]
        print(f"  • {arquivos[i-1]}")
    
    print("\n📊 Gráficos prontos para usar no README e no estudo!")
