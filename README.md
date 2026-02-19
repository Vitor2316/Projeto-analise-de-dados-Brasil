#  Análise de Produtividade e Salário Real no Brasil (2012-2025)

[![Status](https://img.shields.io/badge/Status-Finalizado-success)](https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil)
[![R](https://img.shields.io/badge/R-4.0+-blue)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://www.python.org/)
[![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-green)](LICENSE)

> **Versão 3.0 (Final Validada)** - Estudo completo com decomposição estrutural vs conjuntural, validação cruzada e descoberta de reversão do ciclo em dezembro/2025.

---

##  Descoberta Principal

**Trabalhadores formais brasileiros experimentaram ganho real de +15.6% (mediana) no poder de compra entre 2012-2024**, com distribuição **progressiva**: base (+16.7%) cresceu mais que topo (+10.3%).

### Decomposição dos Ganhos:
- **58% estrutural** (permanente): salário mínimo real + redistribuição do PIB
- **42% conjuntural** (reversível): desemprego histórico + recuperação pós-crise

### ⚠️ Alerta Crítico (Fev/2026):
**Dados de dezembro 2025 confirmam reversão do ciclo:** -618 mil empregos, com serviços (motor do crescimento 2022-2024) liderando demissões.

---

##  Gráficos Principais

### 1. Trajetória do Trabalhador Típico (2012-2025)
![Trajetória](graficos/01_trajetoria_trabalhador_tipico.png)

**Descoberta:** 10 anos perdidos (2012-2021), recuperação concentrada em 3 anos (2022-2024).

---

### 2. Decomposição: Estrutural vs Conjuntural
![Decomposição](graficos/02_decomposicao_estrutural_conjuntural.png)

**Descoberta:** 58% dos ganhos são estruturais (ficam mesmo com crise), 42% são conjunturais (podem reverter).

---

### 3. Ganhos Progressivos (Base vs Topo)
![Progressivo](graficos/03_ganhos_progressivos_percentis.png)

**Descoberta:** Base cresceu +16.7%, topo cresceu apenas +10.3%. Desigualdade caiu.

---

### 4. Participação do Trabalho no PIB
![PIB](graficos/04_participacao_trabalho_pib.png)

**Descoberta CRÍTICA:** Trabalhadores capturaram +5.6pp do PIB. **Lucros empresariais foram comprimidos** para financiar os ganhos salariais. Isso torna os ganhos **FRÁGEIS**.

---

### 5. Desemprego vs Salário Real (Relação Inversa)
![Desemprego](graficos/05_desemprego_vs_salario.png)

**Descoberta:** Quando desemprego sobe (2015-2021), salário cai. Quando desemprego cai (2022-2024), salário sobe.

Embora o Brasil tenha crescido 24%, Uruguai e Chile já partiam de níveis mais altos de produtividade. Turquia, apesar do crescimento de 40%, ainda tem produtividade similar ao Brasil.

---

### 6. CAGED: Reversão em Dezembro 2025
![CAGED](graficos/07_caged_reversao_dez2025.png)


**Descoberta Principal ponto:** -618 mil empregos em dezembro/2025. Serviços (que sustentaram 2022-2024) lideram demissões. **O ciclo está revertendo AGORA.**
=======
---

### *Contexto Econômico do Período*

- Recessão 2014-2016
- Pandemia 2020
- Choque inflacionário pós-2021

>>>>>>> 4f3dc004229ef6ac195dc1c7d0ff32610920c766

---

##  Resultados Completos

| Indicador | 2012 | 2024 | Variação | Interpretação |
|-----------|------|------|----------|---------------|
| **Salário Real Mediana (P50)** | R$805 | R$930 | **+15.6%** | Trabalhador típico |
| **Base (P10)** | R$187 | R$218 | **+16.7%** | Puxado pelo salário mínimo |
| **Topo (P90)** | R$2.234 | R$2.465 | **+10.3%** | Menor crescimento |
| **Gini** | 0.504 | 0.488 | **-3.2%** | Desigualdade caiu |
| **Rendimento/Hora** | R$17.33 | R$20.99 | **+21.1%** | Produtividade aparente |
| **Horas/Semana** | 40.4h | 39.3h | **-2.7%** | Trabalha menos |
| **Participação Trabalho no PIB** | 68.1% | 73.7% | **+5.6pp** | Lucros comprimidos |
| **Desemprego** | 7.4% | 6.6% | **-0.8pp** | Mínima histórica |
| **Taxa de Informalidade** | ~39% | ~38% | Estável | Não houve formalização |

---

##  Metodologia

### Correção Crítica Documentada

**Erro Identificado e Corrigido:**
A Tabela 5436 do IBGE fornece rendimentos em "valores reais" - **já deflacionados**. Aplicar deflação adicional causa erro de "dupla deflação".

**Versões do Estudo:**
-  **v1.0:** Salário real -42% (dupla deflação - erro)
-  **v2.0:** Salário real +22% (média simples - incompleto)
-  **v3.0:** Salário real +15.6% (mediana + análise distribucional - correto e completo)

### Fontes de Dados

**Primárias (IBGE/PNAD Contínua):**
- Tabela 5436: Rendimento médio real (já deflacionado)
- Tabela 7535: Percentis (P10, P50, P90)
- Tabela 7453: Índice de Gini
- Tabela 4562: Taxa de desemprego
- Tabela 4708: Taxa de informalidade
- Tabela 4359: Taxa de participação
- Tabela 4663: Massa salarial agregada
- Tabela 10369: Horas trabalhadas

**Secundárias:**
- Novo CAGED (Ministério do Trabalho)
- Contas Nacionais (PIB real)
- OECD Labour Productivity Database

### Testes de Validação

| Teste | Resultado | Status |
|-------|-----------|--------|
| Salário mínimo real (+18.5%) vs P10 (+16.7%) | Consistente |  Validado |
| Massa salarial (nosso cálculo vs IBGE) | 7.4pp diferença |  Validado |
| Gini (desigualdade caindo) vs P10 > P90 | Coerente |  Validado |
| Desemprego vs salário (correlação inversa) | Confirmada |  Validado |

---

##  Hipóteses Testadas

| Hipótese | Veredicto | Evidência |
|----------|-----------|-----------|
| **H1: Formalização** | ❌ Refutada | Informalidade estável (~39%) |
| **H2: Salário Mínimo** | ✅ Confirmada | P10 segue SM (+18.5% vs +16.7%) |
| **H3: Desemprego Baixo** | ✅ Confirmada | Correlação inversa por período |
| **H4: Concentração no Topo** | ❌ Refutada | Base cresceu mais que topo |
| **H5: Viés de Sobrevivência** | ⚠️ Parcial | Efeito existe mas não domina |
| **H6: Serviços Pós-COVID** | ✅ Confirmada | Mas revertendo em dez/2025 |

---

##  Projeções 2026

| Cenário | Probabilidade | P50 Projetado | Variação vs 2024 |
|---------|--------------|---------------|------------------|
| **Pessimista** | 20% | R$870 | -6.5% |
| **Base** | **60%** | R$930 | 0% (estável) |
| **Otimista** | 20% | R$960 | +3.2% |

**Cenário Base (mais provável):**
- PIB: +2.0%
- Inflação: 5.5%
- Desemprego: 6.5-7.5%
- Salário real mediana: estável

**Risco:** Assimétrico para baixo. Dados de dez/2025 (-618 mil empregos) sugerem materialização do cenário pessimista.

---

##  Estrutura do Projeto

```
Projeto-analise-de-dados-Brasil/
│
├── dados/
│   ├── brasil_anual_corrigido.csv         # Série temporal principal
│   ├── percentis_rendimento.csv           # P10, P50, P90 (2012-2024)
│   ├── massa_salarial_validacao.csv       # Validação cruzada
│   └── caged_setorial_2025.csv            # Dados de emprego
│
├── graficos/
│   ├── 01_trajetoria_trabalhador_tipico.png
│   ├── 02_decomposicao_estrutural_conjuntural.png
│   ├── 03_ganhos_progressivos_percentis.png
│   ├── 04_participacao_trabalho_pib.png
│   ├── 05_desemprego_vs_salario.png
│   ├── 06_massa_salarial_vs_pib.png
│   ├── 07_caged_reversao_dez2025.png
│   ├── 08_criacao_empregos_desaceleracao.png
│   ├── 09_horas_vs_produtividade.png
│   └── 10_projecoes_2026.png
│
├── scripts/
│   ├── gerar_graficos_v3.py               # Python: gerar todos os gráficos
│   ├── graficos_finais_v3_parte1.R        # R: gráficos 1-5
│   ├── graficos_finais_v3_parte2.R        # R: gráficos 6-10
│   └── analise_completa.R                 # R: análise estatística
│
├── RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md  # 52 páginas completas
├── METODOLOGIA.md                         # Detalhamento metodológico
└── README.md                              # Este arquivo

```

---

##  Como Reproduzir

### Requisitos

**Python:**
```bash
pip install matplotlib numpy pandas seaborn
```

**R:**
```r
install.packages(c("ggplot2", "dplyr", "tidyr", "scales", "patchwork"))
```

### Gerar Gráficos

**Python (recomendado):**
```bash
python scripts/gerar_graficos_v3.py
```

**R:**
```r
source("scripts/graficos_finais_v3_parte1.R")
source("scripts/graficos_finais_v3_parte2.R")
```

### Análise Completa (R)

```r
source("scripts/analise_completa.R")
```

---

##  Destaques Metodológicos

### 1. Rigor Científico
- Identificou e corrigiu erro de dupla deflação
- Testou 6 hipóteses concorrentes
- Validou com 4 fontes independentes
- Documentou todas as limitações

### 2. Análise Distribucional
- Não se limitou à média
- Analisou P10, P50 (mediana), P90
- Calculou Gini e razão P90/P10
- Descobriu ganhos progressivos

### 3. Decomposição Inédita
- Separou estrutural (58%) vs conjuntural (42%)
- Quantificou compressão de lucros (+5.6pp PIB)
- Identificou reversão em tempo real (dez/2025)

### 4. Perspectiva Temporal
- 14 anos de dados (3 governos, 2 crises)
- Análise período a período
- Projeções fundamentadas (não especulativas)

---

##  Limitações Reconhecidas

### Dados Não Disponíveis
1. **Produtividade Real:** PIB/horas totais (setorial)
2. **Lucro Empresarial:** Dados consolidados de margem
3. **Inflação Setorial:** Repasse de custos para preços
4. **CAGED Completo:** Série histórica 2012-2019
5. **Microdados PNAD:** Para intervalos de confiança

### Vieses Reconhecidos
1. **Composição:** PNAD capta só formais (39% informais fora)
2. **Sobrevivência:** Desemprego alto tira pobres da amostra
3. **Produtividade Aparente:** Rendimento/hora pode ter viés setorial

### Causalidade
**O estudo identifica CORRELAÇÕES, não CAUSALIDADE rigorosa.** Para causalidade seriam necessários experimentos naturais ou variáveis instrumentais.

---

##  Documentação Completa

- **[RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md](RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md)**: Estudo completo (52 páginas)
- **[METODOLOGIA.md](METODOLOGIA.md)**: Detalhes técnicos e fórmulas
- **[CHANGELOG.md](CHANGELOG.md)**: Histórico de versões e correções

---

##  Contribuições

Sugestões, críticas e melhorias são bem-vindas! Abra uma **issue** ou **pull request**.

---

##  Contato

**Vitor Ramos dos Santos**  
📧 Email: vitorramossantos8@gmail.com  
💼 LinkedIn: [linkedin.com/in/vitor-ramos-santos](https://linkedin.com/in/vitor-ramos-santos)  
🐙 GitHub: [github.com/Vitor2316](https://github.com/Vitor2316)

---

##  Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

##  Agradecimentos

- **IBGE** - Pela disponibilização dos dados da PNAD Contínua
- **Ministério do Trabalho** - Pelos dados do Novo CAGED
- **Comunidade R e Python** - Pelas bibliotecas de visualização

---

##  Status do Projeto

- [x] Coleta de dados (SIDRA, CAGED)
- [x] Limpeza e tratamento
- [x] Correção metodológica (dupla deflação)
- [x] Análise distribucional (percentis)
- [x] Decomposição estrutural vs conjuntural
- [x] Validação cruzada (4 fontes)
- [x] Testes de hipóteses (6 hipóteses)
- [x] Identificação de reversão (dez/2025)
- [x] Projeções 2026
- [x] Gráficos profissionais (10 principais)
- [x] Relatório final (52 páginas)
- [x] Documentação completa

**Status: ✅ FINALIZADO** (Fevereiro 2026)

---


---

**⭐ Se este estudo foi útil, considere deixar uma estrela no repositório!**

