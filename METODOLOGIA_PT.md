# METODOLOGIA — Análise Salarial Brasil 2012-2025 (v3.5)

**Versão:** 3.5 Final
**Autor:** Vitor Ramos dos Santos
**Data:** Fevereiro de 2026
**Status:** Completa e Validada

---

## Sumário

1. [Objetivo da Pesquisa](#1-objetivo-da-pesquisa)
2. [Fontes de Dados](#2-fontes-de-dados)
3. [Correção Metodológica Crítica](#3-correção-metodológica-crítica)
4. [Processamento de Dados](#4-processamento-de-dados)
5. [Métricas Calculadas](#5-métricas-calculadas)
6. [Testes de Validação](#6-testes-de-validação)
7. [Análise Estatística Avançada](#7-análise-estatística-avançada)
8. [Decomposição Estrutural vs. Cíclica](#8-decomposição-estrutural-vs-cíclica)
9. [Modelagem e Previsão](#9-modelagem-e-previsão)
10. [Validação Internacional](#10-validação-internacional)
11. [Resolução do Paradoxo da Produtividade](#11-resolução-do-paradoxo-da-produtividade)
12. [Limitações e Premissas](#12-limitações-e-premissas)
13. [Considerações Éticas](#13-considerações-éticas)
14. [Referências](#14-referências)

---

## 1. OBJETIVO DA PESQUISA

### 1.1 Questão Central
Como evoluiu o poder de compra real dos trabalhadores brasileiros entre 2012-2025? Os ganhos foram distribuídos ou concentrados? Permanentes ou temporários?

### 1.2 Objetivos Específicos
1. **Quantificar** a variação real do salário mediano (trabalhador típico)
2. **Analisar** a distribuição dos ganhos por percentil (P10, P50, P90)
3. **Decompor** os ganhos em componentes estruturais vs. cíclicos
4. **Identificar** direcionadores causais (salário mínimo, desemprego, redistribuição)
5. **Validar** resultados com múltiplas fontes independentes
6. **Projetar** cenários probabilísticos para 2026-2030
7. **Quantificar** incerteza por meio de simulação Monte Carlo
8. **Validar** achados por comparação internacional

### 1.3 Período Analisado
- **Período principal:** 2012-2024 (13 anos completos)
- **Período estendido:** 2012-2025 (inclui dados parciais/projeções)
- **Frequência:** Anual (agregação de dados trimestrais da PNAD)

---

## 2. FONTES DE DADOS

### 2.1 Dados Primários (Brasil)

**Instituição:** IBGE — Instituto Brasileiro de Geografia e Estatística

**PNAD Contínua (Pesquisa Nacional por Amostra de Domicílios Contínua):**
- **Tabela 5436:** Rendimento médio mensal real, deflacionado pelo IBGE
- **Tabela 7535:** Percentis de rendimento a preços correntes do ano
- **Cobertura:** Todo o Brasil, apenas trabalhadores formais
- **Amostra:** Aproximadamente 211.000 domicílios/trimestre
- **Frequência:** Trimestral, agregada a anual

**Contas Nacionais:**
- **Contas Nacionais Trimestrais:** PIB, remuneração dos empregados
- **Cálculo da participação do trabalho:** (Remuneração dos empregados / PIB) × 100

**Salário Mínimo:**
- Série oficial ajustada pela inflação (INPC)

**CAGED (Cadastro Geral de Empregados e Desempregados):**
- Emprego mensal por setor
- Dezembro de 2025: dado de validação em tempo real

### 2.2 Dados Internacionais

**Banco Mundial:**
- PIB per capita PPC (dólares internacionais constantes de 2017)
- Países: Brasil, Chile, México, Colômbia, Turquia, Argentina

**OCDE / OIT:**
- Participação do trabalho na renda
- Estatísticas de emprego

### 2.3 Qualidade dos Dados

**Pontos fortes:**
- Estatísticas oficiais de governo
- Metodologia validada (o IBGE é instituição de referência)
- Múltiplas fontes de validação cruzada
- Série histórica longa (13+ anos)

**Limitações:**
- A PNAD exclui 39% dos trabalhadores informais
- Dados trimestrais agregados a anual (perde variação intra-anual)
- Produtividade verdadeira (PIB/total de horas) não é publicada

---

## 3. CORREÇÃO METODOLÓGICA CRÍTICA

### 3.1 Erro na Versão 1.0

**Metodologia incorreta:**
```
Salário real = Salário nominal × (IPCA_2024 / IPCA_ano)
```

**Problema:** dupla deflação
- A Tabela 5436 da PNAD já deflaciona para preços constantes
- Aplicar o IPCA novamente infla os valores artificialmente
- Resultado: queda falsa de -42%

### 3.2 Correção na Versão 2.0+

**Metodologia correta:**
```
Salário real = Valor da Tabela 5436 (já deflacionado pelo IBGE)
```

**Resultado:** ganho de +15,6% (2012-2024)

**Validação:** checado cruzadamente com massa salarial, PIB, salário mínimo e coeficiente de Gini.

---

## 4. PROCESSAMENTO DE DADOS

### 4.1 Extração de Dados da PNAD

**Fonte:** API SIDRA do IBGE
```python
url = "https://sidra.ibge.gov.br/api/values/t/5436/..."
```

**Variáveis extraídas:**
- Rendimento médio mensal (todos os trabalhadores)
- Por ano: 2012-2024
- Já deflacionado a preços constantes

### 4.2 Dados de Percentis

**Fonte:** Tabela 7535 (preços correntes do ano)

**Processamento:**
```python
valor_real = valor_nominal × (IPCA_2012 / IPCA_ano)
```

**Justificativa:** a Tabela 7535 não é pré-deflacionada, exige ajuste manual

### 4.3 Dados Internacionais

**API do Banco Mundial:**
```python
indicador = "NY.GDP.PCAP.PP.KD"  # PIB per capita PPC
```

**Dados da OCDE:**
- Participação do trabalho extraída manualmente de tabelas publicadas
- Consistência checada entre fontes

---

## 5. MÉTRICAS CALCULADAS

### 5.1 Crescimento do Salário Real

**Fórmula:**
```
Crescimento % = [(Salário_final / Salário_inicial) - 1] × 100
```

**Aplicação:**
- Mediana (P50): (930 / 805 - 1) × 100 = +15,6%

### 5.2 Rendimento por Hora (Proxy de Produtividade)

**Fórmula:**
```
Rendimento/hora = Rendimento mensal real / (Horas semanais × 4,33)
```

**NOTA CRÍTICA:** isso NÃO é produtividade econômica verdadeira. A produtividade verdadeira seria:
```
Produtividade verdadeira = PIB / Total de horas trabalhadas (economia inteira)
```

Nossa medida captura:
- Efeitos de composição setorial
- Efeitos de formalização
- Vieses de mensuração

NÃO ganhos de eficiência.

### 5.3 Participação do Trabalho no PIB

**Fórmula:**
```
Participação do trabalho = (Remuneração dos empregados / PIB) × 100
```

**Fonte:** Contas Nacionais do IBGE

**Resultado:** 68,1% (2012) → 73,7% (2024)

### 5.4 Salário Implícito (Comparação Internacional)

**Fórmula:**
```
Salário implícito = (PIB per capita PPC) × (Participação do trabalho / 100)
```

**Propósito:** comparar a evolução salarial independentemente da PNAD

**Resultado:** +14,1% (Brasil, 2012-2024)

---

## 6. TESTES DE VALIDAÇÃO

### 6.1 Validação da Massa Salarial

**Hipótese:** nossos cálculos de salário devem bater com a massa salarial oficial do IBGE

**Método:**
```
Nossa massa salarial = Salário médio × Número de trabalhadores
Massa salarial IBGE = Publicada nas Contas Nacionais
```

**Resultado:** correspondência perfeita (diferença de 0,0%)

**Nota sobre esse resultado:** essa correspondência é, em boa medida, tautológica — a massa salarial oficial é calculada essencialmente da mesma forma (salário médio × população ocupada), então uma diferença próxima de zero era esperada por construção, não uma confirmação independente forte.

### 6.2 Correlação com o Salário Mínimo

**Hipótese:** P10 deveria acompanhar de perto o salário mínimo

**Método:** comparar a trajetória do P10 com o salário mínimo real

**Resultado:** correlação alta, confirma que a base é influenciada pela política

### 6.3 Consistência com o PIB

**Hipótese:** o crescimento da massa salarial não deveria exceder excessivamente o crescimento do PIB

**Checagem:**
- Massa salarial: +26,5%
- PIB: +11,2%
- Diferença: +15pp → explicada pelo aumento da participação do trabalho (+5,6pp)

**Resultado:** consistente

### 6.4 Coeficiente de Gini

**Hipótese:** se o crescimento do P10 for maior que o do P90, o Gini deveria cair

**Resultado:** Gini 0,504 → 0,488 (desigualdade caiu, como previsto)

### 6.5 Validação Internacional por PPC

**Hipótese:** o crescimento salarial da PNAD deveria bater com PIB per capita × participação do trabalho

**Método:**
- PNAD: +15,6%
- Salário implícito PPC: +14,1%
- Diferença: 1,5pp

**Explicação:** viés de composição + diferença entre formal/informal

**Resultado:** validado dentro de margens esperadas

---

## 7. ANÁLISE ESTATÍSTICA AVANÇADA

### 7.1 Regressão Linear

**Modelo:** Salário real = f(Desemprego)

**Especificação:**
```
P50_real = β₀ + β₁ × Desemprego + ε
```

**Resultados:**
- Coeficiente (β₁): -2,35
- Interpretação: cada 1pp de aumento no desemprego → queda de R$2,35 no salário
- R²: 0,037 (correlação geral fraca)
- p-valor: 0,493 (**não significativo ao nível de 5%**)

**Explicação:** a correlação agregada fraca mascara relações fortes específicas de subperíodo:
- 2012-2014: desemprego cai, salários sobem
- 2015-2021: desemprego sobe, salários caem
- 2022-2024: desemprego cai, salários sobem

**Ressalva importante:** como essa regressão não é estatisticamente significativa (p = 0,493), o coeficiente -2,35 **não pode ser tratado como uma estimativa causal confiável** a partir desses dados. Ele é reportado aqui por transparência, não é usado diretamente adiante. A elasticidade usada na Seção 9 (Modelagem e Previsão) é uma premissa separada, explicitamente calibrada — veja a nota lá para entender por que os dois números diferem e para que serve cada um.

### 7.2 Teste de Quebra Estrutural

**Método:** comparar inclinações de tendência entre períodos

**Período 2012-2021:**
- Tendência: R$2,66/ano
- Crescimento acumulado: 0,6%

**Período 2022-2024:**
- Tendência: R$49,50/ano
- Crescimento acumulado: 11,9%

**Aceleração:** 18,6× mais rápida no período recente

**Interpretação:** mudança de regime detectada em 2022

### 7.3 Engenharia de Atributos (Feature Engineering)

**Volatilidade Salarial:**
```
Volatilidade = Desvio padrão das taxas de crescimento anual
```

**Resultados:**
- Geral (2012-2024): 3,84%
- Pré-COVID (2012-2019): 2,46%
- Pós-COVID (2020-2024): 5,12%
- Aumento: +108%

**Interpretação:** o mercado de trabalho ficou mais instável pós-COVID

**Extremos:**
- Maior queda: 2021 (-8,0%)
- Maior crescimento: 2024 (+6,7%)

### 7.4 Matriz de Correlação

|               | Salário | Desemprego | Part. Trabalho | PIB    |
|---------------|---------|------------|-----------------|--------|
| Salário       | 1,000   | -0,193     | 0,420           | 0,490  |
| Desemprego    | -0,193  | 1,000      | 0,031           | -0,669 |
| Part. Trabalho| 0,420   | 0,031      | 1,000           | 0,152  |
| PIB           | 0,490   | -0,669     | 0,152           | 1,000  |

**Principais achados:**
- Salário vs. Desemprego: negativa moderada (-0,193)
- Salário vs. Participação do trabalho: positiva moderada (0,420)
- Salário vs. PIB: positiva moderada (0,490)

**Nota:** essas são correlações simples de séries curtas (13 pontos anuais), não coeficientes de um modelo multivariado — devem ser lidas como indícios descritivos, não como evidência causal.

---

## 8. DECOMPOSIÇÃO ESTRUTURAL VS. CÍCLICA

### 8.1 Metodologia

**Objetivo:** separar ganhos permanentes de ganhos temporários

**Método:** atribuir o crescimento a direcionadores identificados

**Nota metodológica geral:** a divisão abaixo entre "estrutural" e "cíclico" é um julgamento analítico informado pelos padrões observados, não uma decomposição estatística exata (do tipo que se obteria com uma regressão multivariada significativa). Os percentuais devem ser lidos como estimativas aproximadas.

### 8.2 Componentes Estruturais (58% — permanentes)

**A. Política de Salário Mínimo Real (aproximadamente 6,2pp):**
- Fórmula: INPC + crescimento do PIB passado
- Vinculante para os percentis mais baixos
- Evidência: P10 cresceu +16,7% (acima da mediana)

**B. Redistribuição (aproximadamente 3,0pp):**
- Participação do trabalho aumentou +5,6pp
- Mesmo sem crescimento do PIB, isso eleva os salários
- Capturado do capital (lucros das empresas)

### 8.3 Componentes Cíclicos (42% — reversíveis)

**A. Desemprego Historicamente Baixo (aproximadamente 3,0pp):**
- 2024: 6,6% (mínimo da série)
- Elasticidade usada: -2,0 (cada 1pp de desemprego → 2% de salário) — valor calibrado, não estimado (ver Seção 9.1)
- Se o desemprego subir para 8-9%, perda de 3-6pp

**B. Efeito Base / Recuperação (aproximadamente 5,0pp):**
- 2021: de volta ao nível de 2012 (década perdida)
- 2022-2024: recuperação rápida
- Não é crescimento novo, apenas reposição do que se perdeu

### 8.4 Projeção sob Normalização

**Cenário:** desemprego sobe para 9%

**Perda:**
- Efeito desemprego: -2,0 × (9 - 6,6) = -4,8pp
- Efeito base se dissipa: -2,0pp
- Perda cíclica total: aproximadamente -7pp

**Retido:**
- Ganhos estruturais: aproximadamente +9pp
- Líquido vs. 2012: +9% - 7% = +2%

**P50 previsto:** aproximadamente R$870-880

**Lembrete:** este é um cenário construído sobre premissas calibradas (Seção 9.1), não uma previsão estatística com intervalo de confiança formal.

---

## 9. MODELAGEM E PREVISÃO

### 9.1 Modelo de Projeção

**Especificação:**

O impacto total sobre o salário é a soma de quatro direcionadores macroeconômicos:

```
Impacto_total = ε_desemp × (Desemp - 6,6) +
               ε_pib × PIB +
               ε_sm × SM_real +
               ε_infl × (Infl - 3,0)

Salário_2026 = Base_2024 × (1 + Impacto_total/100)
```

**Elasticidades usadas (calibradas, não estimadas estatisticamente):**
- Desemprego (ε_desemp): -2,0
- PIB (ε_pib): 0,3
- Salário mínimo (ε_sm): 0,4
- Inflação (ε_infl): -0,5

**Por que "calibradas" e não "estimadas":** esses valores **não** são resultado de uma regressão estatisticamente significativa sobre os dados deste projeto. A única regressão desemprego→salário rodada neste conjunto de dados (Seção 7.1) retornou R² = 0,037 e p = 0,493 — ou seja, indistinguível de ruído. O ε_desemp = -2,0 usado aqui reflete, em vez disso, uma síntese baseada em julgamento do padrão por subperíodo (leitura período a período da Seção 7.1) e da literatura geral de economia do trabalho sobre sensibilidade salário-desemprego (uma magnitude próxima à lei de Okun), arredondada para um número simples e conservador para fins de cenário.

As elasticidades de PIB, salário mínimo e inflação são calibradas da mesma forma — informadas pelas correlações da Seção 7.4 e por relações macroeconômicas padrão, não ajustadas com intervalos de confiança. Trate todo resultado das Seções 9.2–9.5 (Monte Carlo, análise de sensibilidade, testes de estresse, previsão 2026-2030) como **"o que acontece sob essas sensibilidades assumidas"**, não como uma previsão estatisticamente validada. Isso é uma ferramenta de planejamento de cenários, não uma previsão econométrica.

### 9.2 Simulação Monte Carlo

**Método:** 10.000 iterações com parâmetros estocásticos

**Distribuições assumidas:**
- Desemprego: Normal(μ=7,5%, σ=1,5%), truncada em [5%, 15%]
- PIB: Normal(μ=2,0%, σ=1,0%), truncada em [-2%, 5%]
- Inflação: Normal(μ=5,5%, σ=1,0%), truncada em [3%, 10%]
- SM real: Normal(μ=2,0%, σ=0,8%), truncada em [0%, 5%]

**Resultados (para 2026):**
- Média: R$914
- Mediana: R$913
- Desvio padrão: R$28
- Intervalo de 90% (P5-P95): [R$870, R$960]
- Probabilidade de queda vs. 2024: 48%

### 9.3 Análise de Sensibilidade

**Método:** variar cada parâmetro ceteris paribus

**Impactos isolados:**
- Desemprego 5% → 12%: ΔSalário = -R$130
- PIB -1% → +4%: ΔSalário = +R$46
- Inflação 3% → 8%: ΔSalário = -R$47
- SM real 0% → 4%: ΔSalário = +R$35

**Conclusão:** o desemprego tem o maior impacto

### 9.4 Testes de Estresse

**Cenários extremos testados:**

| Cenário | Desemprego | PIB | Inflação | Salário 2026 | Variação |
|---------|------------|-----|----------|---------------|----------|
| Crise Severa | 12% | -2% | 8% | R$827 | -11,1% |
| Estagflação | 10% | 0% | 7% | R$869 | -6,6% |
| Ajuste Recessivo | 9% | 0,5% | 5% | R$902 | -3,0% |
| Boom Insustentável | 5% | 4% | 6% | R$975 | +4,8% |

### 9.5 Previsão 2026-2030

**Três cenários construídos:**

**Pessimista (probabilidade: 30%):**
- Premissas: desemprego 10%, PIB 0,5%, inflação 7%
- Trajetória: R$930 (2024) → R$856 (2027) → R$856 (2030)
- Perda acumulada: -8%

**Base (probabilidade: 50%):**
- Premissas: desemprego 7-8%, PIB 2%, inflação 5,5%
- Trajetória: R$930 (2024) → R$902 (2027) → R$930 (2030)
- Variação: -3% (2027), depois recupera

**Otimista (probabilidade: 20%):**
- Premissas: desemprego 5,5%, PIB 3-4%, inflação 4%
- Trajetória: R$930 (2024) → R$1.004 (2027) → R$1.088 (2030)
- Ganho acumulado: +17%

**Previsão esperada (média ponderada por probabilidade):**
- 2026: R$913 (-1,8%)
- 2027: R$909 (-2,3%)
- 2028: R$916 (-1,5%)
- 2029: R$926 (-0,4%)
- 2030: R$939 (+1,0%)

---

## 10. VALIDAÇÃO INTERNACIONAL

### 10.1 Metodologia

**Propósito:** validar os achados da PNAD por meio de fonte independente (PIB per capita PPC)

**Países:** Brasil, Chile, México, Colômbia, Turquia, Argentina

**Métricas:**
1. Crescimento do PIB per capita PPC (2012-2024)
2. Variação da participação do trabalho
3. Salário implícito = PIB per capita × Participação do trabalho

### 10.2 Resultados

| País | PIB/capita PPC | Part. Trabalho | Salário Implícito |
|------|-----------------|-----------------|---------------------|
| **Brasil** | **+5,4%** | **+5,6pp** | **+14,1%** |
| Chile | +20,5% | +1,8pp | +24,6% |
| México | +21,3% | +1,7pp | +27,2% |
| Colômbia | +27,8% | +2,5pp | +34,8% |
| Turquia | +46,4% | +3,4pp | +58,1% |
| Argentina | -2,8% | +0,6pp | -1,7% |

### 10.3 Decomposição

**Brasil:**
- Efeito PIB per capita: +5,4% (crescimento econômico)
- Efeito redistribuição: +8,2% (aumento da participação do trabalho)
- Total: +14,1%

**Outros países:**
- Impulsionados por crescimento: 80-90% vindo do crescimento do PIB, 10-20% de redistribuição
- Brasil: 40% de crescimento, 60% de redistribuição

### 10.4 Achado Principal

**O Brasil é uma exceção clara no grupo comparado:**
- O PIB per capita cresceu abaixo de todos os pares, exceto a Argentina
- A participação do trabalho aumentou mais (+5,6pp vs. +0,6-3,4pp)
- Os ganhos salariais vieram principalmente de redistribuição, não de crescimento

Esse padrão é:
- **Incomum** (outros países dependem mais de crescimento)
- Um regime que **tem limites** (compressão de margens não pode continuar indefinidamente)
- Um regime para o qual os **dados de dezembro de 2025 são consistentes com o início de uma reversão** (não uma confirmação definitiva a partir de um único mês)

---

## 11. RESOLUÇÃO DO PARADOXO DA PRODUTIVIDADE

### 11.1 O Paradoxo

**Nosso estudo encontrou:**
- Rendimento por hora: +21,1% (2012-2024)
- Interpretado inicialmente como "ganho de produtividade"

**Dados macro mostram:**
- PIB per capita PPC: +5,4% (estagnado)
- Produtividade agregada: praticamente estável

**Contradição aparente:** como os trabalhadores podem ganhar +21% por hora se a produtividade está estagnada?

### 11.2 Resolução

**Nossa "produtividade" ≠ produtividade econômica**

**O que medimos:**
```
Produtividade aparente = Rendimento / Horas (da pesquisa PNAD)
```

**A produtividade verdadeira seria:**
```
Produtividade real = PIB / Total de horas trabalhadas (economia inteira)
```

Não temos dados de "total de horas trabalhadas".

### 11.3 Explicação do +21% de Rendimento/Hora

**Decomposição estimada:**

**~60% Composição setorial:**
- Trabalhadores migraram de setores de baixo salário/muitas horas (agropecuária, indústria)
- Para setores de salário mais alto/menos horas (serviços, especialmente qualificados)
- A média sobe sem que ninguém individualmente se torne mais produtivo

**~30% Redistribuição:**
- Participação do trabalho +5,6pp
- Mesma produção, maior fatia salarial
- Não é eficiência, é apenas deslocamento de renda

**~10% Artefato de mensuração:**
- Formalização (informal → formal infla a média)
- Viés de reporte (horas trabalhadas vs. horas declaradas)

**Nota:** essa decomposição percentual (60/30/10) é uma estimativa qualitativa para orientar a interpretação, não um resultado calculado com precisão estatística.

### 11.4 Validação Internacional

O salário implícito de +14,1% (PPC) do Brasil é consistente com:
- +5,4% vindo de crescimento real de produtividade
- +8,2% vindo de redistribuição
- = +14,1% total

A diferença entre nosso +15,6% (PNAD) e +14,1% (PPC) — 1,5pp — é explicada por:
- Viés de composição na PNAD
- Cobertura de trabalhadores formais vs. total

### 11.5 Reconhecimento Crítico

**NÃO afirmamos que a produtividade verdadeira aumentou.**

A comparação internacional sugere que:
- A produtividade agregada do Brasil ficou estagnada
- Os ganhos salariais vieram de redistribuição e composição
- Não de melhorias de eficiência

Isso está agora documentado explicitamente em todos os relatórios.

---

## 12. LIMITAÇÕES E PREMISSAS

### 12.1 Limitações de Dados

**Dados indisponíveis:**
1. Total de horas trabalhadas (economia inteira)
2. Margens de lucro corporativas (agregadas)
3. Repasse setorial de inflação
4. Série histórica completa do CAGED (2012-2019)
5. Microdados da PNAD (para intervalos de confiança robustos)
6. Taxas detalhadas de participação na força de trabalho

**Cobertura limitada:**
- Informalidade: dados disponíveis apenas a partir de 2016
- CAGED por setor: apenas 2020-2025 em formato adequado
- Percentis internacionais: não encontrados para comparação

### 12.2 Vieses Reconhecidos

**1. Viés de composição (PNAD):**
- Captura apenas trabalhadores formais empregados
- 39% de informais excluídos
- Se a composição muda (formais ganham mais), a média sobe sem ganhos individuais
- Mitigação: taxa de informalidade analisada (estável em aproximadamente 39%)

**2. Viés de sobrevivência:**
- Durante crises, desempregados (geralmente mais pobres) saem da amostra
- A média dos empregados remanescentes sobe artificialmente
- Evidência: 2015-2021 teve desemprego alto, mas a média não caiu proporcionalmente
- Mitigação: uso da mediana (P50) em vez da média

**3. Viés de produtividade aparente:**
- Rendimento/hora pode subir por deslocamento setorial, não produtividade real
- Sem PIB/total de horas, não é possível confirmar produtividade verdadeira
- Mitigação: documentado como "proxy", sem alegação de causalidade

**4. Viés de seleção temporal:**
- A análise de 2012-2024 captura um ciclo completo (crise + recuperação)
- Um período diferente poderia mostrar resultados diferentes
- Mitigação: subperíodos analisados separadamente

### 12.3 Premissas do Modelo

**Premissa 1: Estabilidade das elasticidades**
- Assumimos que as elasticidades calibradas (desemprego, PIB etc. — ver Seção 9.1) permanecem constantes
- Essas **não** são coeficientes estatisticamente estimados a partir dos dados deste projeto; a única regressão testada (Seção 7.1) não foi significativa (p = 0,493). São valores baseados em julgamento, informados pelos padrões de subperíodo observados e pela literatura geral
- Na realidade, podem variar com mudanças estruturais
- Justificativa: melhor calibração disponível dado o conjunto de dados, não uma estimativa estatisticamente validada

**Premissa 2: Distribuições normais**
- O Monte Carlo assume que os parâmetros seguem distribuições normais
- Eventos extremos (caudas gordas) podem estar subestimados
- Mitigação: distribuições truncadas em valores plausíveis

**Premissa 3: Independência entre parâmetros**
- Tratamos desemprego, PIB e inflação como independentes
- Na realidade existem correlações (desemprego alto geralmente com PIB baixo)
- Justificativa: simplificação necessária por tratabilidade

**Premissa 4: Efeitos lineares**
- Assumimos impactos lineares (cada 1pp de desemprego = mesmo efeito)
- Efeitos reais podem ser não-lineares
- Mitigação: faixas limitadas a valores historicamente observados

### 12.4 O Que NÃO Fizemos (por limitação)

- Análise por subgrupo: por setor, região, idade, gênero
- Regressão econométrica completa: com variáveis de controle e instrumentos
- Inferência causal rigorosa: diferenças-em-diferenças, variáveis instrumentais
- Intervalos de confiança robustos: exigiria microdados
- Testes de hipótese formais: teste-t, ANOVA (dado que os dados são expandidos por amostragem populacional)
- Análise completa de informalidade: dados apenas a partir de 2016
- Produtividade setorial verdadeira: PIB/horas por setor indisponível
- Modelos ARIMA/GARCH: série temporal curta demais (13 anos)

---

## 13. CONSIDERAÇÕES ÉTICAS

### 13.1 Transparência

**Erros documentados:**
- Erro da versão 1.0 (-42%) totalmente explicado
- Processo de correção transparente
- Todas as versões preservadas para revisão

**Limitações declaradas:**
- Lacunas de dados reconhecidas
- Vieses reconhecidos
- Explicações alternativas consideradas

### 13.2 Neutralidade

**Neutralidade política:**
- Análise baseada em dados, não em ideologia
- Apresenta achados desconfortáveis para diferentes perspectivas políticas
- Reconhece tanto os ganhos (trabalhadores) quanto a fragilidade (insustentabilidade)

**Interpretação equilibrada:**
- A política de salário mínimo funcionou (ganhos estruturais persistem)
- Mas os ganhos cíclicos estão revertendo (mercado de trabalho normalizando)
- Não é "bom" nem "ruim" — apenas o que os dados mostram, com as ressalvas estatísticas descritas ao longo do documento

### 13.3 Acessibilidade

**Código e dados públicos:**
- Todos os scripts disponíveis no GitHub
- Fontes de dados documentadas e acessíveis
- Metodologia detalhada para reprodução

**Múltiplos idiomas:**
- Documentação em português e inglês
- Acessível a públicos nacional e internacional

---

## 14. REFERÊNCIAS

### Fontes de Dados

**IBGE (Instituto Brasileiro de Geografia e Estatística):**
- PNAD Contínua — Tabela 5436 (rendimento deflacionado)
- PNAD Contínua — Tabela 7535 (percentis)
- Contas Nacionais Trimestrais
- Série Histórica do Salário Mínimo

**Ministério do Trabalho:**
- CAGED (Cadastro Geral de Empregados e Desempregados)

**Banco Mundial:**
- World Development Indicators
- PIB per capita PPC (dólares internacionais constantes de 2017)

**OCDE:**
- Labor Income Share Database
- Employment Outlook

**OIT (Organização Internacional do Trabalho):**
- Base de dados ILOSTAT

### Referências Acadêmicas

- Solow, R. (1956). "A Contribution to the Theory of Economic Growth"
- Piketty, T. (2014). "Capital in the Twenty-First Century"
- Autor, D. (2019). "Work of the Past, Work of the Future"

---

## APÊNDICE A: Tabela de Dados Completa

Ver arquivo separado: `dados/brasil_anual_CORRIGIDO_FINAL.csv`

---

## APÊNDICE B: Resumo de Fórmulas

**Crescimento do salário real:**
```
Crescimento % = [(Salário_final / Salário_inicial) - 1] × 100
```

**Participação do trabalho:**
```
Participação do trabalho = (Remuneração dos empregados / PIB) × 100
```

**Salário implícito (PPC):**
```
Salário implícito = PIB per capita PPC × (Participação do trabalho / 100)
```

**Projeção Monte Carlo:**
```
Salário_2026 = Base_2024 × (1 + Impacto/100)
onde Impacto = Σ (Elasticidade_i × ΔParâmetro_i)
```

---

**Versão da Metodologia:** 3.5 Final
**Última Atualização:** 23 de fevereiro de 2026
**Autor:** Vitor Ramos dos Santos
