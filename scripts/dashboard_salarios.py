"""
================================================================================
DASHBOARD INTERATIVO - ANÁLISE SALÁRIOS BRASIL
Streamlit App com Simulador de Cenários
================================================================================

Para rodar:
    streamlit run dashboard_salarios.py

Funcionalidades:
- Visualização interativa dos dados
- Simulador de cenários econômicos
- Comparação de períodos
- Análise de sensibilidade
================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Análise Salários Brasil",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        padding: 20px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E86C1;
    }
    .warning-box {
        background-color: #FFF3CD;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #F39C12;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DADOS
# ============================================================================

@st.cache_data
def load_data():
    anos = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 
                     2020, 2021, 2022, 2023, 2024])
    
    data = pd.DataFrame({
        'ano': anos,
        'p10': [187, 205, 215, 202, 198, 185, 182, 184, 210, 192, 203, 207, 218],
        'p50': [805, 829, 865, 834, 836, 851, 863, 852, 880, 810, 831, 872, 930],
        'p90': [2234, 2293, 2355, 2240, 2319, 2301, 2337, 2295, 2368, 2172, 2234, 2376, 2465],
        'desemprego': [7.4, 7.3, 7.0, 8.9, 11.6, 12.6, 12.1, 11.8, 13.7, 14.0, 9.6, 7.7, 6.6],
        'part_trabalho': [68.1, 67.8, 65.9, 70.2, 71.6, 71.6, 71.4, 74.2, 67.1, 66.6, 69.4, 70.4, 73.7],
        'gini': [0.504, 0.499, 0.497, 0.490, 0.498, 0.498, 0.506, 0.506, 0.500, 0.499, 0.486, 0.494, 0.488]
    })
    
    # Variação percentual
    data['variacao_p50'] = data['p50'].pct_change() * 100
    
    return data

df = load_data()

# ============================================================================
# SIDEBAR - CONTROLES
# ============================================================================

st.sidebar.markdown("## 🎛️ Controles")

# Seletor de período
periodo = st.sidebar.radio(
    "Período de Análise",
    ["Completo (2012-2024)", "Pré-crise (2012-2014)", "Crise (2015-2021)", "Recuperação (2022-2024)"]
)

if periodo == "Pré-crise (2012-2014)":
    df_filtered = df[df['ano'] <= 2014]
elif periodo == "Crise (2015-2021)":
    df_filtered = df[(df['ano'] >= 2015) & (df['ano'] <= 2021)]
elif periodo == "Recuperação (2022-2024)":
    df_filtered = df[df['ano'] >= 2022]
else:
    df_filtered = df

st.sidebar.markdown("---")

# Modo de visualização
modo = st.sidebar.selectbox(
    "Modo de Visualização",
    ["Dashboard Principal", "Simulador de Cenários", "Análise Comparativa"]
)

# ============================================================================
# HEADER
# ============================================================================

st.markdown('<div class="main-header">📊 Análise Salários Brasil 2012-2025</div>', 
            unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #7F8C8D; font-size: 1.1rem; margin-bottom: 30px;">
Dashboard Interativo | Desenvolvido por Vitor Ramos dos Santos
</div>
""", unsafe_allow_html=True)

# ============================================================================
# MODO 1: DASHBOARD PRINCIPAL
# ============================================================================

if modo == "Dashboard Principal":
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        var_total = ((df['p50'].iloc[-1] / df['p50'].iloc[0]) - 1) * 100
        st.metric(
            "Variação Total P50",
            f"+{var_total:.1f}%",
            delta=f"R${df['p50'].iloc[-1] - df['p50'].iloc[0]:.0f}",
            delta_color="normal"
        )
    
    with col2:
        desemp_atual = df['desemprego'].iloc[-1]
        desemp_var = df['desemprego'].iloc[-1] - df['desemprego'].iloc[0]
        st.metric(
            "Desemprego Atual",
            f"{desemp_atual:.1f}%",
            delta=f"{desemp_var:+.1f}pp",
            delta_color="inverse"
        )
    
    with col3:
        gini_atual = df['gini'].iloc[-1]
        gini_var = df['gini'].iloc[-1] - df['gini'].iloc[0]
        st.metric(
            "Gini (Desigualdade)",
            f"{gini_atual:.3f}",
            delta=f"{gini_var:+.3f}",
            delta_color="inverse"
        )
    
    with col4:
        part_atual = df['part_trabalho'].iloc[-1]
        part_var = df['part_trabalho'].iloc[-1] - df['part_trabalho'].iloc[0]
        st.metric(
            "Part. Trabalho PIB",
            f"{part_atual:.1f}%",
            delta=f"{part_var:+.1f}pp"
        )
    
    st.markdown("---")
    
    # Gráfico principal: Evolução P50
    fig1 = go.Figure()
    
    fig1.add_trace(go.Scatter(
        x=df_filtered['ano'],
        y=df_filtered['p50'],
        mode='lines+markers',
        name='Salário Real Mediana',
        line=dict(color='#2E86C1', width=3),
        marker=dict(size=10)
    ))
    
    # Linha de referência 2012
    fig1.add_hline(y=df['p50'].iloc[0], line_dash="dash", 
                   line_color="gray", opacity=0.5,
                   annotation_text="Nível 2012", annotation_position="right")
    
    fig1.update_layout(
        title="Evolução do Salário Real (Mediana)",
        xaxis_title="Ano",
        yaxis_title="Salário Real (R$ de 2012)",
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Dois gráficos lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        # Desemprego vs Salário
        fig2 = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig2.add_trace(
            go.Scatter(x=df_filtered['ano'], y=df_filtered['desemprego'],
                      name="Desemprego", line=dict(color='#E74C3C', width=2)),
            secondary_y=False
        )
        
        fig2.add_trace(
            go.Scatter(x=df_filtered['ano'], y=df_filtered['p50'],
                      name="Salário", line=dict(color='#2ECC71', width=2)),
            secondary_y=True
        )
        
        fig2.update_xaxes(title_text="Ano")
        fig2.update_yaxes(title_text="Desemprego (%)", secondary_y=False)
        fig2.update_yaxes(title_text="Salário Real (R$)", secondary_y=True)
        fig2.update_layout(title="Desemprego vs Salário", height=350)
        
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Participação no PIB
        fig3 = go.Figure()
        
        fig3.add_trace(go.Scatter(
            x=df_filtered['ano'],
            y=df_filtered['part_trabalho'],
            fill='tozeroy',
            name='Participação Trabalho',
            line=dict(color='#2ECC71')
        ))
        
        fig3.update_layout(
            title="Participação do Trabalho no PIB",
            xaxis_title="Ano",
            yaxis_title="% do PIB",
            height=350
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    
    # Insights
    st.markdown("### 🔍 Insights Principais")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>📈 Ganhos Progressivos</h4>
        <p>Base (P10) cresceu <strong>+16.7%</strong><br>
        Topo (P90) cresceu <strong>+10.3%</strong><br>
        <em>Desigualdade diminuiu</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>💼 Compressão de Lucros</h4>
        <p>Trabalho capturou <strong>+5.6pp</strong> do PIB<br>
        Capital perdeu <strong>-5.6pp</strong><br>
        <em>Redistribuição forçada</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
        <h4>⚠️ Fragilidade</h4>
        <p>58% estrutural (fica)<br>
        42% conjuntural (reverte)<br>
        <em>Ganhos parcialmente reversíveis</em></p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# MODO 2: SIMULADOR DE CENÁRIOS
# ============================================================================

elif modo == "Simulador de Cenários":
    
    st.markdown("## 🎮 Simulador de Cenários 2026")
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚙️ Ajuste os parâmetros econômicos e veja o impacto no salário real</strong>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        desemprego_sim = st.slider(
            "Taxa de Desemprego (%)",
            min_value=5.0,
            max_value=15.0,
            value=7.0,
            step=0.5,
            help="Desemprego atual: 6.6%"
        )
        
        inflacao_sim = st.slider(
            "Inflação Anual (%)",
            min_value=2.0,
            max_value=10.0,
            value=5.5,
            step=0.5,
            help="Meta: 3% | Atual: ~4.8%"
        )
    
    with col2:
        pib_sim = st.slider(
            "Crescimento PIB (%)",
            min_value=-2.0,
            max_value=5.0,
            value=2.0,
            step=0.5,
            help="2024: +3.2%"
        )
        
        salario_minimo_real = st.slider(
            "Ganho Real Salário Mínimo (%)",
            min_value=0.0,
            max_value=5.0,
            value=2.0,
            step=0.5,
            help="Fórmula atual: INPC + PIB passado"
        )
    
    # Cálculo do impacto
    base_2024 = 930
    
    # Impacto desemprego (elasticidade -2.0)
    impacto_desemp = -2.0 * (desemprego_sim - 6.6)
    
    # Impacto salário mínimo (40% do ganho)
    impacto_sm = 0.40 * salario_minimo_real
    
    # Impacto PIB (via emprego e produtividade)
    impacto_pib = 0.30 * pib_sim
    
    # Impacto inflação (corrói ganho nominal)
    impacto_inflacao = -(inflacao_sim - 3.0) * 0.5
    
    # Total
    impacto_total = impacto_desemp + impacto_sm + impacto_pib + impacto_inflacao
    salario_2026 = base_2024 * (1 + impacto_total/100)
    
    st.markdown("---")
    
    # Resultado
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Salário 2024 (Base)",
            f"R${base_2024:.0f}",
            delta=None
        )
    
    with col2:
        st.metric(
            "Salário 2026 (Projetado)",
            f"R${salario_2026:.0f}",
            delta=f"{impacto_total:+.1f}%"
        )
    
    with col3:
        var_vs_2012 = ((salario_2026 / 805) - 1) * 100
        st.metric(
            "Variação vs 2012",
            f"{var_vs_2012:+.1f}%",
            delta=None
        )
    
    # Decomposição do impacto
    st.markdown("### 📊 Decomposição do Impacto")
    
    decomp_data = pd.DataFrame({
        'Fator': ['Desemprego', 'Salário Mínimo', 'PIB', 'Inflação'],
        'Impacto (pp)': [impacto_desemp, impacto_sm, impacto_pib, impacto_inflacao]
    })
    
    fig_decomp = px.bar(
        decomp_data,
        x='Fator',
        y='Impacto (pp)',
        color='Impacto (pp)',
        color_continuous_scale=['red', 'yellow', 'green'],
        title="Contribuição de Cada Fator"
    )
    
    fig_decomp.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_decomp, use_container_width=True)
    
    # Interpretação
    st.markdown("### 💡 Interpretação")
    
    if impacto_total > 0:
        st.success(f"✅ Cenário POSITIVO: Salário real cresce {impacto_total:.1f}% em 2026")
    elif impacto_total > -3:
        st.warning(f"⚠️ Cenário NEUTRO: Salário real varia {impacto_total:+.1f}% em 2026")
    else:
        st.error(f"❌ Cenário NEGATIVO: Salário real cai {abs(impacto_total):.1f}% em 2026")

# ============================================================================
# MODO 3: ANÁLISE COMPARATIVA
# ============================================================================

else:  # Análise Comparativa
    
    st.markdown("## 📊 Análise Comparativa de Períodos")
    
    # Métricas por período
    periodos = {
        'Pré-crise (2012-2014)': df[(df['ano'] >= 2012) & (df['ano'] <= 2014)],
        'Crise (2015-2021)': df[(df['ano'] >= 2015) & (df['ano'] <= 2021)],
        'Recuperação (2022-2024)': df[df['ano'] >= 2022]
    }
    
    comparacao = []
    for nome, dados in periodos.items():
        var_p50 = ((dados['p50'].iloc[-1] / dados['p50'].iloc[0]) - 1) * 100
        desemp_medio = dados['desemprego'].mean()
        vol = dados['variacao_p50'].std()
        
        comparacao.append({
            'Período': nome,
            'Var. Salário (%)': var_p50,
            'Desemprego Médio (%)': desemp_medio,
            'Volatilidade': vol
        })
    
    df_comp = pd.DataFrame(comparacao)
    
    st.dataframe(df_comp, use_container_width=True, hide_index=True)
    
    # Gráficos comparativos
    col1, col2 = st.columns(2)
    
    with col1:
        fig_var = px.bar(
            df_comp,
            x='Período',
            y='Var. Salário (%)',
            color='Var. Salário (%)',
            color_continuous_scale=['red', 'yellow', 'green'],
            title="Variação Salarial por Período"
        )
        st.plotly_chart(fig_var, use_container_width=True)
    
    with col2:
        fig_desemp = px.bar(
            df_comp,
            x='Período',
            y='Desemprego Médio (%)',
            color='Desemprego Médio (%)',
            color_continuous_scale='Reds',
            title="Desemprego Médio por Período"
        )
        st.plotly_chart(fig_desemp, use_container_width=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7F8C8D; padding: 20px;">
<p><strong>Análise Salários Brasil 2012-2025</strong></p>
<p>Desenvolvido por Vitor Ramos dos Santos | Fevereiro 2026</p>
<p>Dados: IBGE/PNAD Contínua, CAGED, Contas Nacionais</p>
</div>
""", unsafe_allow_html=True)

