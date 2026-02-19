# ============================================================================
# GRÁFICOS FINAIS - VERSÃO 3.0
# Análise de Salários Brasil 2012-2025
# Autor: Vitor Ramos dos Santos
# ============================================================================

library(ggplot2)
library(dplyr)
library(tidyr)
library(scales)
library(patchwork)

# Configuração global
theme_set(theme_minimal(base_size = 12))

# Paleta de cores profissional
cores <- list(
  verde = "#2ECC71",
  vermelho = "#E74C3C",
  azul = "#3498DB",
  amarelo = "#F39C12",
  cinza = "#95A5A6",
  cinza_claro = "#ECF0F1"
)

# ============================================================================
# GRÁFICO 1: TRAJETÓRIA DO TRABALHADOR TÍPICO (2012-2025)
# ============================================================================

# Dados
dados_trajetoria <- data.frame(
  ano = 2012:2025,
  p50 = c(805, 829, 865, 834, 836, 851, 863, 852, 880, 810, 831, 872, 930, 938),
  contexto = c(
    "Dilma 1", "Pré-crise", "Pico", "Crise -3.5%", "Crise -3.3%", 
    "Desemp. pico", "Recuperação", "Pré-COVID", "COVID", "Pior momento",
    "Recuperação", "Lula 3", "Pleno emprego", "Reversão?"
  )
)

# Marcos históricos
marcos <- data.frame(
  ano = c(2014, 2016, 2020, 2021, 2023),
  evento = c("Pico\nR$865", "Impeachment", "COVID-19", "Vale\nR$810\n(= 2012)", "Lula 3"),
  y = c(865, 836, 880, 810, 872)
)

g1 <- ggplot(dados_trajetoria, aes(x = ano, y = p50)) +
  geom_line(color = cores$azul, size = 1.5) +
  geom_point(size = 3, color = cores$azul) +
  geom_hline(yintercept = 805, linetype = "dashed", color = cores$cinza, size = 0.8) +
  geom_text(aes(x = 2012.5, y = 805, label = "Nível de 2012"), 
            vjust = -0.5, hjust = 0, color = cores$cinza, size = 3.5) +
  geom_point(data = marcos, aes(x = ano, y = y), 
             color = cores$vermelho, size = 4, shape = 18) +
  geom_text(data = marcos, aes(x = ano, y = y, label = evento), 
            vjust = -1, hjust = 0.5, size = 3, fontface = "bold") +
  scale_y_continuous(labels = dollar_format(prefix = "R$"), 
                     breaks = seq(800, 950, 25)) +
  scale_x_continuous(breaks = 2012:2025) +
  labs(
    title = "Trajetória do Trabalhador Típico (Mediana)",
    subtitle = "10 anos perdidos (2012-2021), recuperação em 3 anos (2022-2024)",
    x = "Ano",
    y = "Salário Real Mensal (R$ de 2012)",
    caption = "Fonte: IBGE/PNAD Contínua | Autor: Vitor Ramos dos Santos"
  ) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    plot.subtitle = element_text(size = 12, color = cores$cinza),
    axis.text.x = element_text(angle = 45, hjust = 1),
    panel.grid.minor = element_blank()
  )

ggsave("01_trajetoria_trabalhador_tipico.png", g1, 
       width = 12, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 2: DECOMPOSIÇÃO ESTRUTURAL vs CONJUNTURAL
# ============================================================================

decomp_data <- data.frame(
  componente = c("Salário Mínimo", "Redistribuição", "Desemprego Baixo", "Efeito Base"),
  pontos = c(6.2, 3.0, 3.0, 5.0),
  tipo = c("Estrutural", "Estrutural", "Conjuntural", "Conjuntural"),
  ordem = c(1, 2, 3, 4)
) %>%
  mutate(componente = factor(componente, levels = componente[order(ordem)]))

g2 <- ggplot(decomp_data, aes(x = componente, y = pontos, fill = tipo)) +
  geom_col(width = 0.7) +
  geom_text(aes(label = sprintf("+%.1fpp", pontos)), 
            vjust = -0.5, size = 4, fontface = "bold") +
  scale_fill_manual(values = c("Estrutural" = cores$verde, 
                                "Conjuntural" = cores$amarelo)) +
  scale_y_continuous(limits = c(0, 7), breaks = seq(0, 7, 1)) +
  labs(
    title = "Decomposição dos Ganhos Salariais (+15.6%)",
    subtitle = "58% estrutural (permanece) vs 42% conjuntural (reverte)",
    x = NULL,
    y = "Contribuição (pontos percentuais)",
    fill = "Tipo de Ganho",
    caption = "Total: 9pp estrutural + 7pp conjuntural = +15.6% (arredondado)\nFonte: Análise própria com dados IBGE/PNAD"
  ) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.text.x = element_text(angle = 20, hjust = 1, size = 11),
    legend.position = "top",
    panel.grid.major.x = element_blank()
  )

ggsave("02_decomposicao_estrutural_conjuntural.png", g2, 
       width = 10, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 3: GANHOS PROGRESSIVOS (P10 vs P50 vs P90)
# ============================================================================

ganhos_data <- data.frame(
  percentil = c("P10\n(10% mais\npobres)", "P50\n(Mediana)", 
                "P90\n(10% mais\nricos)", "Salário\nMínimo"),
  variacao = c(16.7, 15.6, 10.3, 18.5),
  cor = c(cores$verde, cores$azul, cores$vermelho, cores$cinza)
)

g3 <- ggplot(ganhos_data, aes(x = reorder(percentil, -variacao), y = variacao)) +
  geom_col(aes(fill = percentil), width = 0.7, show.legend = FALSE) +
  geom_text(aes(label = sprintf("+%.1f%%", variacao)), 
            vjust = -0.5, size = 5, fontface = "bold") +
  scale_fill_manual(values = ganhos_data$cor) +
  scale_y_continuous(limits = c(0, 21), breaks = seq(0, 20, 5)) +
  labs(
    title = "Ganhos Foram Progressivos",
    subtitle = "Base cresceu mais (+16.7%) que topo (+10.3%) | Desigualdade caiu",
    x = NULL,
    y = "Variação Real 2012-2024 (%)",
    caption = "Fonte: IBGE/PNAD Contínua - Tabela 7535 (percentis)"
  ) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.text.x = element_text(size = 11),
    panel.grid.major.x = element_blank()
  )

ggsave("03_ganhos_progressivos_percentis.png", g3, 
       width = 10, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 4: PARTICIPAÇÃO DO TRABALHO NO PIB
# ============================================================================

part_pib_data <- data.frame(
  ano = 2012:2024,
  trabalho = c(68.1, 67.8, 65.9, 70.2, 71.6, 71.6, 71.4, 74.2, 
               67.1, 66.6, 69.4, 70.4, 73.7),
  capital = c(31.9, 32.2, 34.1, 29.8, 28.4, 28.4, 28.6, 25.8, 
              32.9, 33.4, 30.6, 29.6, 26.3)
)

# Reshape para long
part_long <- part_pib_data %>%
  pivot_longer(cols = c(trabalho, capital), 
               names_to = "componente", 
               values_to = "percentual")

g4 <- ggplot(part_long, aes(x = ano, y = percentual, fill = componente)) +
  geom_area(alpha = 0.7) +
  geom_line(aes(color = componente), size = 1) +
  scale_fill_manual(values = c("trabalho" = cores$verde, "capital" = cores$cinza),
                    labels = c("Participação do Capital (Lucros)", 
                               "Participação do Trabalho (Salários)")) +
  scale_color_manual(values = c("trabalho" = cores$verde, "capital" = cores$cinza),
                     labels = c("Participação do Capital (Lucros)", 
                                "Participação do Trabalho (Salários)")) +
  scale_y_continuous(labels = percent_format(scale = 1), 
                     breaks = seq(0, 100, 10)) +
  scale_x_continuous(breaks = 2012:2024) +
  annotate("text", x = 2018, y = 50, 
           label = "Trabalho capturou\n+5.6pp do PIB", 
           size = 5, fontface = "bold", color = cores$verde) +
  annotate("text", x = 2018, y = 15, 
           label = "Lucros\ncomprimidos", 
           size = 4, fontface = "bold", color = cores$cinza) +
  labs(
    title = "Redistribuição: Trabalho Ganhou do Capital",
    subtitle = "Participação do trabalho subiu de 68.1% → 73.7% | Lucros caíram de 31.9% → 26.3%",
    x = "Ano",
    y = "% do PIB",
    fill = NULL,
    color = NULL,
    caption = "Ganhos salariais vieram de compressão de margens empresariais\nFonte: Cálculo próprio com dados IBGE e Contas Nacionais"
  ) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    legend.position = "top",
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

ggsave("04_participacao_trabalho_pib.png", g4, 
       width = 12, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 5: DESEMPREGO vs SALÁRIO REAL
# ============================================================================

desemp_salario_data <- data.frame(
  ano = 2012:2024,
  desemprego = c(7.4, 7.3, 7.0, 8.9, 11.6, 12.6, 12.1, 11.8, 13.7, 14.0, 9.6, 7.7, 6.6),
  p50 = c(805, 829, 865, 834, 836, 851, 863, 852, 880, 810, 831, 872, 930)
)

g5 <- ggplot(desemp_salario_data, aes(x = ano)) +
  geom_line(aes(y = desemprego), color = cores$vermelho, size = 1.5) +
  geom_point(aes(y = desemprego), color = cores$vermelho, size = 3) +
  geom_line(aes(y = (p50 - 700) / 20), color = cores$azul, size = 1.5) +
  geom_point(aes(y = (p50 - 700) / 20), color = cores$azul, size = 3) +
  scale_y_continuous(
    name = "Taxa de Desemprego (%)",
    sec.axis = sec_axis(~. * 20 + 700, name = "Salário Real Mediana (R$)",
                        labels = dollar_format(prefix = "R$"))
  ) +
  scale_x_continuous(breaks = 2012:2024) +
  annotate("rect", xmin = 2015, xmax = 2021, ymin = -Inf, ymax = Inf,
           alpha = 0.1, fill = cores$vermelho) +
  annotate("text", x = 2018, y = 15, 
           label = "Crise + COVID\n(desemprego alto)", 
           size = 3.5, color = cores$vermelho) +
  labs(
    title = "Desemprego Alto = Salário Baixo (Relação Inversa)",
    subtitle = "Quando desemprego sobe, trabalhador perde poder de barganha",
    x = "Ano",
    caption = "Fonte: IBGE/PNAD Contínua"
  ) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    axis.title.y.left = element_text(color = cores$vermelho, face = "bold"),
    axis.title.y.right = element_text(color = cores$azul, face = "bold"),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

ggsave("05_desemprego_vs_salario.png", g5, 
       width = 12, height = 7, dpi = 300, bg = "white")

print("✅ Gráficos 1-5 criados com sucesso!")
print("Execute o script parte 2 para os gráficos 6-10")
