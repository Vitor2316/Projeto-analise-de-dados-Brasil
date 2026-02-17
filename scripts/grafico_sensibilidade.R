library(ggplot2)
library(dplyr)
library(patchwork)

dados_trim <- read.csv("brasil_trimestral_corrigido.csv")

dados_anual_calculado <- dados_trim %>%
  group_by(ano) %>%
  summarise(
    salario_real_indice = mean(salario_real_indice),
    rendimento_hora_indice = mean(rendimento_hora_indice),
    .groups = 'drop'
  ) %>%
  mutate(posicao = (ano - 2012) * 4 + 2.5)

p1 <- ggplot() +
  geom_line(data = dados_trim, 
            aes(x = 1:nrow(dados_trim), y = salario_real_indice), 
            color = "blue", linewidth = 1.2, alpha = 0.7) +
  geom_point(data = dados_anual_calculado, 
             aes(x = posicao, y = salario_real_indice), 
             color = "red", size = 2.5) +
  geom_hline(yintercept = 100, linetype = "dashed", color = "gray50") +
  labs(title = "Salário Real",
       subtitle = "Linha azul = dados trimestrais | Pontos vermelhos = médias anuais",
       x = "Trimestre", 
       y = "Índice (2012 = 100)") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 11))

p2 <- ggplot() +
  geom_line(data = dados_trim, 
            aes(x = 1:nrow(dados_trim), y = rendimento_hora_indice), 
            color = "green", linewidth = 1.2, alpha = 0.7) +
  geom_point(data = dados_anual_calculado, 
             aes(x = posicao, y = rendimento_hora_indice), 
             color = "red", size = 2.5) +
  geom_hline(yintercept = 100, linetype = "dashed", color = "gray50") +
  labs(title = "Rendimento/Hora",
       subtitle = "Linha verde = dados trimestrais | Pontos vermelhos = médias anuais",
       x = "Trimestre", 
       y = "Índice (2012 = 100)") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 11))

p1 + p2 + 
  plot_annotation(
    title = "Análise de Sensibilidade: Comparação Trimestral vs Anual",
    subtitle = "Demonstra que médias anuais suavizam oscilações naturais dos dados trimestrais",
    theme = theme(plot.title = element_text(size = 13, face = "bold"),
                  plot.subtitle = element_text(size = 10))
  )
