# ==============================================================================
# SCRIPT: Limpeza e Processamento de Dados SIDRA/PNAD
# Autor: Vitor Ramos dos Santos
# Data: Fevereiro 2026
# ==============================================================================

library(tidyverse)
library(dplyr)
library(tidyr)

# ETAPA 1: LEITURA DOS DADOS BRUTOS DO SIDRA ================================

# Tabela 5436 - Rendimento médio mensal
dados_rendimento_bruto <- read.csv("tabela5436.csv", sep = ";", encoding = "UTF-8")

# Tabela 6371 - Horas trabalhadas
dados_horas_bruto <- read.csv("tabela6371.csv", sep = ";", encoding = "UTF-8")

# ETAPA 2: EXTRAÇÃO DA LINHA DE VALORES =====================================

# Geralmente os valores estão na linha 5
linha_rendimento <- dados_rendimento_bruto[5, -1, drop = FALSE]
linha_horas <- dados_horas_bruto[5, -1, drop = FALSE]

# ETAPA 3: CONVERSÃO PARA FORMATO LONG ======================================

# Rendimento
dados_rendimento_long <- pivot_longer(linha_rendimento,
                                      cols = everything(),
                                      names_to = "trimestre",
                                      values_to = "rendimento")

# Horas
dados_horas_long <- pivot_longer(linha_horas,
                                 cols = everything(),
                                 names_to = "trimestre",
                                 values_to = "horas")

# ETAPA 4: LIMPEZA DE NOMES DE TRIMESTRES ===================================

limpar_trimestre <- function(df) {
  df %>%
    mutate(
      # Remove "X" do início
      trimestre = str_remove(trimestre, "^X"),
      # Substitui pontos por espaços
      trimestre = str_replace_all(trimestre, "\\.", " "),
      # Remove º (ordinal)
      trimestre = str_remove(trimestre, "º")
    )
}

dados_rendimento_long <- limpar_trimestre(dados_rendimento_long)
dados_horas_long <- limpar_trimestre(dados_horas_long)

# ETAPA 5: CONVERSÃO DE VALORES =============================================

# Converter vírgula para ponto e transformar em numérico
dados_rendimento_long <- dados_rendimento_long %>%
  mutate(rendimento = as.numeric(gsub(",", ".", rendimento)))

dados_horas_long <- dados_horas_long %>%
  mutate(horas = as.numeric(gsub(",", ".", horas)))

# ETAPA 6: JUNÇÃO DAS TABELAS ===============================================

dados_completos <- inner_join(dados_rendimento_long, 
                               dados_horas_long, 
                               by = "trimestre")

# ETAPA 7: CÁLCULO DE RENDIMENTO POR HORA ===================================

# Rendimento mensal / (horas semanais * 4.33 semanas/mês)
dados_completos <- dados_completos %>%
  mutate(rendimento_hora = rendimento / (horas * 4.33))

# ETAPA 8: ADICIONAR COLUNA DE ANO ==========================================

dados_completos <- dados_completos %>%
  mutate(ano = as.integer(str_extract(trimestre, "\\d{4}")))

# ETAPA 9: SALVAR DADOS LIMPOS ===============================================

write.csv(dados_completos, "dados_brasil_limpos.csv", row.names = FALSE)

# ETAPA 10: VERIFICAÇÃO ======================================================

print("Dados processados com sucesso!")
print(paste("Total de trimestres:", nrow(dados_completos)))
print(head(dados_completos))
print(summary(dados_completos))
