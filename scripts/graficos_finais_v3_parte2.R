# ============================================================================
# GRÁFICOS FINAIS - VERSÃO 3.0 (PARTE 2)
# Gráficos 6-10
# ============================================================================

library(ggplot2)
library(dplyr)
library(scales)

# Paleta de cores
cores <- list(
  verde = "#2ECC71",
  vermelho = "#E74C3C",
  azul = "#3498DB",
  amarelo = "#F39C12",
  cinza = "#95A5A6"
)

# ============================================================================
# GRÁFICO 6: MASSA SALARIAL vs PIB REAL
# ============================================================================

massa_pib_data <- data.frame(
  ano = 2012:2024,
  massa_indice = c(100, 105.2, 109.5, 105.4, 104.3, 104.1, 108.1, 110.2, 
                   103.8, 100.2, 106.5, 118.9, 126.5),
  pib_indice = c(100, 103.0, 103.5, 99.8, 96.5, 97.7, 99.5, 100.7, 
                 96.8, 101.7, 104.8, 107.8, 111.2)
)

g6 <- ggplot(massa_pib_data, aes(x = ano)) +
  geom_line(aes(y = massa_indice, color = "Massa Salarial Real"), 
            size = 1.5) +
  geom_line(aes(y = pib_indice, color = "PIB Real"), 
            size = 1.5) +
  geom_point(aes(y = massa_indice), color = cores$verde, size = 3) +
  geom_point(aes(y = pib_indice), color = cores$azul, size = 3) +
  scale_color_manual(values = c("Massa Salarial Real" = cores$verde, 
                                 "PIB Real" = cores$azul)) +
  scale_y_continuous(limits = c(95, 130), breaks = seq(95, 130, 5)) +
  scale_x_continuous(breaks = 2012:2024) +
  annotate("segment", x = 2024, xend = 2024, 
           y = 111.2, yend = 126.5,
           arrow = arrow(ends = "both", length = unit(0.2, "cm")),
           color = cores$vermelho, size = 1) +
  annotate("text", x = 2023, y = 119, 
           label = "Gap = +15pp\nRedistribuição", 
           size = 4, fontface = "bold", color = cores$vermelho) +
  labs(
    title = "Massa Salarial Cresceu MAIS que PIB",
    subtitle = "Massa +26.5% vs PIB +11.2% | Gap de 15pp = redistribuição do capital para trabalho",
    x = "Ano",
    y = "Índice (2012 = 100)",
    color = NULL,
    caption = "Massa Salarial: IBGE Tabela 4663 | PIB: Contas Nacionais"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    legend.position = "top",
    axis.text.x = element_text(angle = 45, hjust = 1),
    panel.grid.minor = element_blank()
  )

ggsave("06_massa_salarial_vs_pib.png", g6, 
       width = 12, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 7: CAGED REVERSÃO DEZ/2025
# ============================================================================

caged_data <- data.frame(
  setor = c("Serviços", "Indústria", "Construção", "Comércio", "Agropecuária"),
  saldo = c(-280.810, -135.087, -104.077, -54.355, -43.836)
) %>%
  mutate(setor = factor(setor, levels = setor))

g7 <- ggplot(caged_data, aes(x = saldo, y = reorder(setor, saldo))) +
  geom_col(fill = cores$vermelho, width = 0.7) +
  geom_text(aes(label = sprintf("%+.0f mil", saldo)), 
            hjust = 1.1, color = "white", size = 5, fontface = "bold") +
  geom_vline(xintercept = 0, color = cores$cinza, size = 0.8) +
  scale_x_continuous(labels = comma_format(scale = 1, suffix = " mil")) +
  labs(
    title = "REVERSÃO: Dezembro 2025 com -618 Mil Empregos",
    subtitle = "Serviços (motor do crescimento 2022-2024) lideram demissões",
    x = "Saldo de Empregos (admissões - demissões)",
    y = NULL,
    caption = "Fonte: Novo CAGED - Ministério do Trabalho\nDados: Dezembro 2025"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(size = 16, face = "bold", color = cores$vermelho),
    plot.subtitle = element_text(color = cores$vermelho),
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank()
  )

ggsave("07_caged_reversao_dez2025.png", g7, 
       width = 10, height = 6, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 8: CRIAÇÃO DE EMPREGOS 2020-2025 (DESACELERAÇÃO)
# ============================================================================

criacao_data <- data.frame(
  ano = c(2020, 2021, 2022, 2025),
  saldo = c(-189, 2782, 2014, 1279),
  cor = c(cores$vermelho, cores$verde, cores$verde, cores$amarelo)
)

g8 <- ggplot(criacao_data, aes(x = as.factor(ano), y = saldo)) +
  geom_col(aes(fill = as.factor(ano)), width = 0.6, show.legend = FALSE) +
  geom_text(aes(label = sprintf("%+.0f mil", saldo)), 
            vjust = ifelse(criacao_data$saldo > 0, -0.5, 1.5), 
            size = 5, fontface = "bold") +
  scale_fill_manual(values = criacao_data$cor) +
  geom_hline(yintercept = 0, color = cores$cinza, size = 0.8) +
  scale_y_continuous(labels = comma_format(suffix = " mil")) +
  labs(
    title = "Criação de Empregos em Desaceleração",
    subtitle = "2025 criou METADE do pico de 2021 | Ciclo perdendo força",
    x = "Ano",
    y = "Saldo Acumulado de Empregos (mil)",
    caption = "Fonte: Novo CAGED - Ministério do Trabalho"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    panel.grid.major.x = element_blank()
  )

ggsave("08_criacao_empregos_desaceleracao.png", g8, 
       width = 10, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 9: HORAS vs RENDIMENTO/HORA (PARADOXO)
# ============================================================================

horas_prod_data <- data.frame(
  ano = 2012:2024,
  horas = c(40.4, 40.1, 39.9, 39.5, 39.3, 39.0, 39.1, 39.2, 39.2, 39.1, 39.2, 39.3, 39.3),
  rend_hora = c(17.33, 17.90, 17.83, 17.75, 18.12, 18.46, 18.50, 18.86, 
                18.63, 19.20, 19.46, 20.05, 20.99)
)

g9 <- ggplot(horas_prod_data, aes(x = ano)) +
  geom_line(aes(y = horas, color = "Horas/semana"), size = 1.5) +
  geom_line(aes(y = (rend_hora - 15) * 2, color = "Rendimento/hora"), size = 1.5) +
  geom_point(aes(y = horas), color = cores$vermelho, size = 3) +
  geom_point(aes(y = (rend_hora - 15) * 2), color = cores$verde, size = 3) +
  scale_y_continuous(
    name = "Horas Trabalhadas/Semana",
    sec.axis = sec_axis(~. / 2 + 15, name = "Rendimento/Hora (R$)",
                        labels = dollar_format(prefix = "R$"))
  ) +
  scale_color_manual(values = c("Horas/semana" = cores$vermelho, 
                                 "Rendimento/hora" = cores$verde)) +
  scale_x_continuous(breaks = 2012:2024) +
  annotate("text", x = 2018, y = 42, 
           label = "Paradoxo da\nProdutividade", 
           size = 5, fontface = "bold") +
  labs(
    title = "Trabalha MENOS, Produz MAIS",
    subtitle = "Horas caíram -2.7% mas rendimento/hora subiu +21%",
    x = "Ano",
    color = NULL,
    caption = "Fonte: IBGE/PNAD Contínua - Tabelas 10369 e 5436"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    legend.position = "top",
    axis.title.y.left = element_text(color = cores$vermelho, face = "bold"),
    axis.title.y.right = element_text(color = cores$verde, face = "bold"),
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

ggsave("09_horas_vs_produtividade.png", g9, 
       width = 12, height = 7, dpi = 300, bg = "white")

# ============================================================================
# GRÁFICO 10: CENÁRIOS 2026
# ============================================================================

cenarios_data <- data.frame(
  cenario = c("Pessimista", "Base", "Otimista"),
  p50 = c(870, 930, 960),
  prob = c("20%", "60%", "20%"),
  cor = c(cores$vermelho, cores$amarelo, cores$verde)
) %>%
  mutate(cenario = factor(cenario, levels = cenario),
         variacao = (p50 / 930 - 1) * 100)

g10 <- ggplot(cenarios_data, aes(x = cenario, y = p50)) +
  geom_col(aes(fill = cenario), width = 0.6, show.legend = FALSE) +
  geom_text(aes(label = sprintf("R$%d\n(%+.1f%%)", p50, variacao)), 
            vjust = -0.5, size = 5, fontface = "bold") +
  geom_text(aes(label = sprintf("Prob: %s", prob), y = 50), 
            size = 4, color = "white", fontface = "bold") +
  scale_fill_manual(values = cenarios_data$cor) +
  scale_y_continuous(labels = dollar_format(prefix = "R$"), 
                     limits = c(0, 1000), breaks = seq(0, 1000, 200)) +
  geom_hline(yintercept = 930, linetype = "dashed", 
             color = cores$cinza, size = 1) +
  annotate("text", x = 3.3, y = 930, 
           label = "Nível 2024", 
           vjust = -0.5, color = cores$cinza, fontface = "bold") +
  labs(
    title = "Projeções para 2026: Salário Real Mediana",
    subtitle = "Cenário base mais provável (60%): estabilidade | Risco assimétrico para baixo",
    x = "Cenário",
    y = "Salário Real Mensal (R$ de 2012)",
    caption = "Pessimista: Inflação 7%, PIB +0.5%, Desemprego 8.5%\nBase: Inflação 5.5%, PIB +2%, Desemprego 7%\nOtimista: Inflação 4%, PIB +3%, Desemprego 5.5%"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(size = 16, face = "bold"),
    panel.grid.major.x = element_blank()
  )

ggsave("10_projecoes_2026.png", g10, 
       width = 10, height = 7, dpi = 300, bg = "white")

print("✅ TODOS os gráficos 6-10 criados com sucesso!")
print("Total: 10 gráficos principais prontos para o estudo")
print("\nArquivos criados:")
print("01_trajetoria_trabalhador_tipico.png")
print("02_decomposicao_estrutural_conjuntural.png")
print("03_ganhos_progressivos_percentis.png")
print("04_participacao_trabalho_pib.png")
print("05_desemprego_vs_salario.png")
print("06_massa_salarial_vs_pib.png")
print("07_caged_reversao_dez2025.png")
print("08_criacao_empregos_desaceleracao.png")
print("09_horas_vs_produtividade.png")
print("10_projecoes_2026.png")
