# Análise de Produtividade e Poder de Compra no Brasil (2012-2025)

**Autor:** Vitor Ramos dos Santos  
**Contato:** vitorramossantos8@gmail.com | [LinkedIn](https://www.linkedin.com/in/vitor-ramos-santos)

---

## Sobre o Projeto

Este estudo analisa a evolução da produtividade do trabalho e do poder de compra dos trabalhadores brasileiros entre 2012 e 2025, comparando os resultados com outros países emergentes (Chile, Colômbia, Peru, Turquia e Uruguai).

### Principal Descoberta

O Brasil experimentou um **paradoxo econômico**:
- Produtividade cresceu **+26%** (rendimento por hora trabalhada)
- Poder de compra caiu **-42%** (salário real ajustado pela inflação)
- Único país entre os comparados onde os trabalhadores perderam poder de compra

---

## Estrutura do Repositório

```
├── dados/
│   ├── brasil_trimestral_corrigido.csv
│   ├── brasil_anual.csv
│   ├── produtividade_anual_paises.csv
│   └── salario_real_anual_paises.csv
│
├── scripts/
│   ├── limpeza_dados.R
│   ├── calculo_indices.py
│   └── graficos.R
│
├── graficos/
│   ├── evolucao_brasil.png
│   ├── comparacao_internacional.png
│   └── sensibilidade.png
│
├── METODOLOGIA.md
└── README.md
```

---

## Metodologia

A análise utiliza:
- **Dados primários:** PNAD Contínua (IBGE/SIDRA) - 55 trimestres
- **Métricas:** Rendimento por hora e salário real ajustado pela inflação
- **Correções:** Inflação composta (não linear), frequência anual para comparações internacionais
- **Validação:** Teste de robustez demonstra incerteza metodológica de ±23% no rendimento/hora

Documentação completa disponível em: [METODOLOGIA.md](METODOLOGIA.md)

---

## Principais Resultados

### Brasil (2012-2025)
| Métrica | Variação |
|---------|----------|
| Produtividade (rendimento/hora) | +26% (faixa: 20-26%) |
| Salário real | -42% |
| Horas trabalhadas/semana | 40.6h → 39.1h |

### Comparação Internacional (Salário Real)
| País | Variação 2012-2025 |
|------|-------------------|
| Turquia | +46% |
| Peru | +33% |
| Chile | +18% |
| Colômbia | +11% |
| Uruguai | +10% |
| **Brasil** | **-42%** |

---

## Ferramentas Utilizadas

- **R** (tidyverse, ggplot2, dplyr)
- **Python** (pandas, numpy, matplotlib)
- **Dados:** IBGE/SIDRA, OECD, ILO, Banco Mundial

---

## Como Reproduzir

1. Baixe os dados brutos do SIDRA (Tabelas 5436 e 6371)
2. Execute os scripts de limpeza em `scripts/`
3. Gere visualizações com `graficos.R`

Código completo disponível mediante solicitação.

---

## Limitações Reconhecidas

- Dados internacionais em frequência anual (vs. trimestral do Brasil)
- Sem ajuste PPP (foco em evolução temporal, não comparação absoluta)
- Rendimento/hora tem incerteza metodológica de ±23%
- Dados agregados (não desagregados por setor/região)

---

## Citação

```
Vitor Ramos dos Santos. (2026). Análise de Produtividade e Poder de Compra 
do Trabalho no Brasil (2012-2025). GitHub.
```

---

## Licença

Dados públicos (IBGE, OECD, ILO, Banco Mundial)  
Código disponível para fins educacionais e de pesquisa.

---

**Última atualização:** Fevereiro 2026
