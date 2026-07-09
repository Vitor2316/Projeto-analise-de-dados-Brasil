# Salários Reais no Brasil, 2012–2025: Uma Decomposição Estrutural e Cíclica

[![Status](https://img.shields.io/badge/Status-Completo-success)](https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0+-blue)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Versão 3.0** · Autor: Vitor Ramos dos Santos · Última atualização: fevereiro de 2026

*[Read in English](README.md)*

---

## Visão geral

Entre 2012 e 2024, o salário real mediano dos trabalhadores formais brasileiros subiu 15,6% (PNAD Contínua). Este projeto decompõe esse ganho em componentes mais ligados a política pública e mudança estrutural, e componentes mais ligados ao ciclo do mercado de trabalho — e confronta o resultado com os dados de emprego até dezembro de 2025.

**Principal achado:** uma estimativa de 58% do ganho está associada a fatores estruturais (principalmente a política de salário mínimo e uma mudança na participação do trabalho no PIB) com maior probabilidade de persistir; uma estimativa de 42% está associada a condições cíclicas (desemprego historicamente baixo, recuperação da retração de 2015–2021) mais sensíveis ao ciclo econômico. Essa decomposição depende de premissas calibradas, não de um coeficiente de regressão estatisticamente significativo — veja a [Metodologia](METODOLOGIA_PT.md) para a derivação completa e essa ressalva em detalhe.

**Comece por aqui:** [Resumo Executivo](EXECUTIVE_SUMMARY.md) (5 min) · [Metodologia Completa](METODOLOGIA_PT.md) · [Gráficos](graficos/)

---

## Números principais

| Indicador | 2012 | 2024 | Variação |
|---|---|---|---|
| Salário real mediano (P50) | R$805 | R$930 | +15,6% |
| Participação do trabalho no PIB | 68,1% | 73,7% | +5,6pp |
| Índice de Gini (renda do trabalho) | 0,504 | 0,488 | -0,016 |
| Taxa de desemprego | 7,4% | 6,6% | -0,8pp |

Dezembro de 2025 (dado mais recente do CAGED): -618 mil vagas formais líquidas, concentradas em serviços (-281 mil). Isso é discutido na Seção 5 do [Resumo Executivo](EXECUTIVE_SUMMARY.md) como um ponto de dado consistente com — mas não suficiente sozinho para confirmar — uma reversão do componente cíclico descrito acima.

---

## Gráficos

### Trajetória salarial e distribuição

**Trajetória do trabalhador típico, 2012–2025**
![Trajetória](graficos/01_trajetoria_trabalhador_tipico.png)
Dez anos (2012–2021) sem ganho líquido relevante, seguidos por uma recuperação concentrada em 2022–2024.

**Decomposição do ganho de +15,6%: estrutural vs. cíclico**
![Decomposição](graficos/02_decomposicao_estrutural_conjuntural.png)
Uma estimativa de 58% do ganho é estrutural (política de salário mínimo, redistribuição); 42% é cíclico (baixo desemprego, efeito de recuperação). Ver a ressalva sobre calibração na [Metodologia](METODOLOGIA_PT.md), Seção 9.1.

**Ganhos por percentil (P10, P50, P90)**
![Progressivo](graficos/03_ganhos_progressivos_percentis.png)
Percentis mais baixos cresceram mais que os mais altos (+16,7% vs. +10,3%), consistente com a política de salário mínimo como fator contribuinte.

### Participação do trabalho e ciclo econômico

**Participação do trabalho no PIB, 2012–2024**
![Participação PIB](graficos/04_participacao_trabalho_pib.png)
A participação do trabalho subiu de 68,1% para 73,7%, com queda correspondente na participação do capital — cerca de R$655 bilhões/ano em termos de 2024.

**Massa salarial vs. PIB (índice, 2012 = 100)**
![Massa salarial vs PIB](graficos/06_massa_salarial_vs_pib.png)
A massa salarial real cresceu mais rápido que o PIB no período, consistente com a mudança de participação acima.

**Desemprego e salários reais**
![Desemprego](graficos/05_desemprego_vs_salario.png)
Séries descritivas exibidas lado a lado. Nota: a regressão formal de salário sobre desemprego na amostra completa não foi estatisticamente significativa (R² = 0,037, p = 0,493) — ver Metodologia, Seção 7.1.

**Horas trabalhadas vs. rendimento por hora**
![Horas vs produtividade](graficos/09_horas_vs_produtividade.png)
As horas médias trabalhadas caíram levemente enquanto o rendimento por hora subiu 21%. Trata-se de uma proxy de produtividade aparente, não uma medida direta de produtividade — três explicações plausíveis são discutidas no Resumo Executivo, Seção 4.

### Dados de emprego (CAGED)

**Dezembro de 2025: perdas líquidas de vagas por setor**
![Reversão CAGED](graficos/07_caged_reversao_dez2025.png)
-618 mil vagas formais líquidas em dezembro de 2025, lideradas por serviços (-281 mil), indústria (-135 mil) e construção (-104 mil).

**Criação de vagas, 2020–2025**
![Desaceleração na criação de empregos](graficos/08_criacao_empregos_desaceleracao.png)
A criação líquida de vagas desacelerou em relação ao pico de 2021.

### Projeções e incerteza

**Cenários para 2026 (ilustrativo)**
![Projeções 2026](graficos/10_projecoes_2026.png)

**Previsão 2026–2030, múltiplos modelos**
![Previsão 2026-2030](graficos/11_previsao_2026_2030.png)
Tendência linear, tendência recente e projeções por cenário exibidas juntas, com banda de confiança de 95% em torno da tendência linear. As linhas de cenário usam as elasticidades calibradas descritas na Metodologia, Seção 9.1, não coeficientes ajustados estatisticamente.

**Análise de sensibilidade**
![Análise de sensibilidade](graficos/12_analise_sensibilidade.png)
Salário projetado para 2026 em função de desemprego, crescimento do PIB, inflação e política de salário mínimo, mantendo os demais fatores fixos.

**Simulação Monte Carlo (10.000 simulações)**
![Monte Carlo](graficos/13_monte_carlo.png)
Distribuição de resultados para o salário em 2026 sob premissas macro aleatorizadas. Valor esperado ≈ R$914, com intervalo de 90% de aproximadamente R$870–960.

**Matriz de cenários: desemprego × inflação**
![Matriz de cenários](graficos/14_matriz_cenarios.png)

### Comparação internacional

**PIB per capita ajustado por PPC, Brasil vs. pares**
![PIB PPC](graficos/15_pib_ppc_internacional.png)

**Participação do trabalho no PIB, comparação internacional**
![Participação internacional](graficos/16_labor_share_internacional.png)

**PIB per capita vs. participação do trabalho, 2024**
![Dispersão](graficos/17_scatter_pib_labor.png)
Usado para verificar se o nível de participação do trabalho no Brasil é um outlier em relação a economias comparáveis (Chile, México, Colômbia, Turquia, Argentina), como checagem de consistência do achado de redistribuição acima.

---

## Resumo da metodologia

- **Dados primários:** IBGE PNAD Contínua (2012–2024, pesquisa domiciliar nacional)
- **Validação:** dados de emprego do CAGED, Contas Nacionais, registros de salário mínimo, comparadores internacionais
- **Métodos estatísticos:** regressão linear, teste de quebra estrutural, simulação Monte Carlo, análise de sensibilidade
- **Limitação conhecida:** a única regressão formalmente testada (salário vs. desemprego, amostra completa) não foi estatisticamente significativa. As elasticidades usadas no simulador de cenários são premissas calibradas, informadas por padrões de subperíodo e pela literatura de economia do trabalho, não coeficientes ajustados. Isso é declarado explicitamente onde esses números são usados — ver [Metodologia](METODOLOGIA_PT.md), Seções 7.1, 9.1 e 12.3.
- **Limitação de cobertura:** a PNAD Contínua cobre apenas trabalhadores formais; cerca de 39% da força de trabalho brasileira é informal e fica fora desta análise.

Derivação completa, testes de hipótese e todas as limitações: [METODOLOGIA_PT.md](METODOLOGIA_PT.md).

---

<<<<<<< HEAD
## Estrutura do repositório
=======
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
| **H1: Formalização** |  Refutada | Informalidade estável (~39%) |
| **H2: Salário Mínimo** |  Confirmada | P10 segue SM (+18.5% vs +16.7%) |
| **H3: Desemprego Baixo** |  Confirmada | Correlação inversa por período |
| **H4: Concentração no Topo** |  Refutada | Base cresceu mais que topo |
| **H5: Viés de Sobrevivência** |  Parcial | Efeito existe mas não domina |
| **H6: Serviços Pós-COVID** |  Confirmada | Mas revertendo em dez/2025 |

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
>>>>>>> 613e3e37a13f8d99b8df1b02b85f16c51e068cb1

```
├── README.md                    # Versão em inglês
├── README_PT.md                 # Este arquivo
├── EXECUTIVE_SUMMARY.md          # Resumo de 5 minutos dos achados
├── METODOLOGIA_PT.md            # Metodologia completa, testes, limitações
├── graficos/                    # 17 gráficos (300 DPI), referenciados acima
├── dados/                       # CSVs de origem e derivados
├── scripts/                     # Python e R, totalmente reproduzível
└── LICENSE                      # MIT
```

## Reproduzindo a análise

```bash
git clone https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil
cd Projeto-analise-de-dados-Brasil
pip install -r requirements.txt   # numpy, pandas, matplotlib, seaborn, scikit-learn, scipy
python scripts/gerar_graficos_v3.py
```

Todas as fontes de dados são públicas (IBGE SIDRA, Ministério do Trabalho). Nenhum dado proprietário ou restrito é utilizado.

---

## Autor

Vitor Ramos dos Santos — estudante de ensino médio técnico em informática. Esta pesquisa foi conduzida de forma independente usando fontes de dados públicas.

**Contato:** vitorramossantos8@gmail.com
**LinkedIn:** www.linkedin.com/in/vitor-ramos2132

## Licença

<<<<<<< HEAD
MIT — ver [LICENSE](LICENSE).
=======
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
 Email: vitorramossantos8@gmail.com  
 LinkedIn: [linkedin.com/in/vitor-ramos-santos](https://linkedin.com/in/vitor-ramos-santos)  
 GitHub: [github.com/Vitor2316](https://github.com/Vitor2316)

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

**Status:  FINALIZADO** (Fevereiro 2026)

---

##  Diferenciais deste Estudo

1. **Transparência Total:** Documenta erro inicial e correção
2. **Análise Profunda:** Não para no primeiro resultado
3. **Validação Rigorosa:** Cruza múltiplas fontes
4. **Descoberta Original:** Compressão de lucros (+5.6pp PIB)
5. **Timing Perfeito:** Capturou reversão em tempo real (dez/2025)

---

** Se este estudo foi útil, considere deixar uma estrela no repositório!**
>>>>>>> 613e3e37a13f8d99b8df1b02b85f16c51e068cb1

**Aviso:** Esta análise representa a interpretação do autor sobre dados publicamente disponíveis. Não constitui aconselhamento financeiro, jurídico ou de investimento.
