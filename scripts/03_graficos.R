# ==============================================================================
# SCRIPT: Visualizações Principais
# Autor: Vitor Ramos dos Santos
# Data: Fevereiro 2026
# ==============================================================================

library(ggplot2)
library(dplyr)
library(tidyr)

# CORES PADRÃO DOS PAÍSES ===================================================

cores_paises <- c(
  "Brasil" = "#009b3a", 
  "Chile" = "#0039a6",
  "Colombia" = "#fcd116",
  "Peru" = "#D91023",
  "Turquia" = "#E30A17",
  "Uruguai" = "#0038A8"
)

# GRÁFICO 1: BRASIL - SALÁRIO REAL VS RENDIMENTO/HORA ======================

dados_brasil <- read.csv("brasil_trimestral_corrigido.csv")

dados_brasil <- dados_brasil %>%
  mutate(trimestre_num = 1:n())

dados_long <- pivot_longer(dados_brasil,
                           cols = c(salario_real_indice, rendimento_hora_indice),
                           names_to = "metrica",
                           values_to = "indice")

dados_long <- dados_long %>%
  mutate(metrica = case_when(
    metrica == "salario_real_indice" ~ "Salário Real (ajustado inflação)",
    metrica == "rendimento_hora_indice" ~ "Rendimento por Hora"
  ))

g1 <- ggplot(dados_long, aes(x = trimestre_num, y = indice, color = metrica)) +
  geom_line(size = 1.5) +
  geom_hline(yintercept = 100, linetype = "dashed", color = "gray50") +
  scale_color_manual(values = c("Salário Real (ajustado inflação)" = "#d62728",
                                 "Rendimento por Hora" = "#2ca02c")) +
  scale_x_continuous(breaks = seq(1, 55, by = 8),
                     labels = c("2012", "2014", "2016", "2018", "2020", "2022", "2024")) +
  labs(title = "Brasil: Produtividade vs Poder de Compra (2012-2025)",
       subtitle = "Índice Base 2012 = 100 - Dados Trimestrais",
       x = "Ano",
       y = "Índice",
       color = "",
       caption = "Fonte: IBGE/PNAD, IPCA") +
  theme_minimal() +
  theme(legend.position = "bottom",
        plot.title = element_text(size = 13, face = "bold"),
        plot.subtitle = element_text(size = 10))

ggsave("grafico_brasil_trimestral.png", g1, width = 10, height = 6, dpi = 300)

# GRÁFICO 2: COMPARAÇÃO INTERNACIONAL - PRODUTIVIDADE ======================

dados_prod <- read.csv("produtividade_anual_paises.csv")

dados_long_prod <- pivot_longer(dados_prod,
                                cols = c(Brasil, Chile, Colombia, Peru, Turquia, Uruguai),
                                names_to = "pais",
                                values_to = "indice")

g2 <- ggplot(dados_long_prod, aes(x = ano, y = indice, color = pais)) +
  geom_line(size = 1.5) +
  geom_point(size = 2) +
  geom_hline(yintercept = 100, linetype = "dashed", color = "gray50") +
  scale_color_manual(values = cores_paises) +
  scale_x_continuous(breaks = seq(2012, 2025, by = 2)) +
  labs(title = "Evolução da Produtividade - Países Emergentes (2012-2025)",
       subtitle = "Índice de rendimento por hora (Base: 2012 = 100) - Dados Anuais",
       x = "Ano",
       y = "Índice",
       color = "País",
       caption = "Fonte: OECD, ILO, IBGE/PNAD") +
  theme_minimal() +
  theme(legend.position = "right",
        plot.title = element_text(size = 13, face = "bold"))

ggsave("grafico_produtividade_internacional.png", g2, width = 10, height = 6, dpi = 300)

# GRÁFICO 3: COMPARAÇÃO INTERNACIONAL - SALÁRIO REAL =======================

dados_salario <- read.csv("salario_real_anual_paises.csv")

dados_long_sal <- pivot_longer(dados_salario,
                               cols = c(Brasil, Chile, Colombia, Peru, Turquia, Uruguai),
                               names_to = "pais",
                               values_to = "indice")

g3 <- ggplot(dados_long_sal, aes(x = ano, y = indice, color = pais)) +
  geom_line(size = 1.5) +
  geom_point(size = 2) +
  geom_hline(yintercept = 100, linetype = "dashed", color = "gray50") +
  scale_color_manual(values = cores_paises) +
  scale_x_continuous(breaks = seq(2012, 2025, by = 2)) +
  labs(title = "Evolução do Poder de Compra - Países Emergentes (2012-2025)",
       subtitle = "Salário Real ajustado pela inflação (Base: 2012 = 100) - Dados Anuais",
       x = "Ano",
       y = "Índice",
       color = "País",
       caption = "Fonte: Bancos Centrais, IBGE, OECD, ILO") +
  theme_minimal() +
  theme(legend.position = "right",
        plot.title = element_text(size = 13, face = "bold"))

ggsave("grafico_salario_real_internacional.png", g3, width = 10, height = 6, dpi = 300)

# GRÁFICO 4: BARRAS - NÍVEIS ABSOLUTOS 2025 ================================

nivel_2025 <- data.frame(
  pais = c("Brasil", "Chile", "Colombia", "Peru", "Turquia", "Uruguai"),
  salario_hora_usd = c(4.2, 5.8, 4.5, 3.9, 3.5, 6.2)
)

g4 <- ggplot(nivel_2025, aes(x = reorder(pais, salario_hora_usd), 
                              y = salario_hora_usd, 
                              fill = pais)) +
  geom_col(width = 0.9) +
  scale_fill_manual(values = cores_paises) +
  coord_flip() +
  labs(title = "Produtividade Absoluta em 2025",
       subtitle = "Salário médio por hora trabalhada (USD PPP estimado)",
       x = "",
       y = "USD por hora",
       caption = "Fonte: Estimativas baseadas em OECD, ILO") +
  theme_minimal() +
  theme(legend.position = "none",
        plot.title = element_text(size = 13, face = "bold"))

ggsave("grafico_barras_2025.png", g4, width = 8, height = 6, dpi = 300)

print("Todos os gráficos salvos com sucesso!")
