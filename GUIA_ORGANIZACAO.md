# 📦 GUIA DE ORGANIZAÇÃO - REPOSITÓRIO FINAL

## 🎯 O que você precisa fazer quando chegar em casa:

### PASSO 1: Organizar pastas no seu repositório GitHub

```
Projeto-analise-de-dados-Brasil/
│
├── dados/            ← CRIAR esta pasta
├── graficos/         ← CRIAR esta pasta (vazia por enquanto)
├── scripts/          ← CRIAR esta pasta
├── README.md         ← Substituir pelo novo
├── METODOLOGIA.md    ← Adicionar
├── RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md  ← Adicionar
└── LICENSE           ← Já existe
```

---

## 📂 PASSO 2: Adicionar arquivos na pasta `dados/`

**ESSENCIAIS (necessários para gráficos):**
- ✅ brasil_anual_CORRIGIDO_FINAL.csv
- ✅ percentis_rendimento.csv
- ✅ massa_salarial_validacao.csv
- ✅ desemprego_salario.csv
- ✅ participacao_pib.csv
- ✅ caged_setorial_2025.csv
- ✅ projecoes_2026.csv

**OPCIONAIS (comparação internacional):**
- salario_real_anual_paises.csv
- produtividade_anual_paises.csv

**REMOVER (versões antigas):**
- ❌ brasil_anual.csv (sem "CORRIGIDO_FINAL")
- ❌ brasil_trimestral_*.csv (não usamos mais)
- ❌ comparacao_*.csv (versões antigas)
- ❌ indice_*.csv (dados intermediários)
- ❌ teste_robustez.csv (dados intermediários)

---

## 🐍 PASSO 3: Adicionar arquivos na pasta `scripts/`

**MANTER:**
- ✅ gerar_graficos_v3.py
- ✅ graficos_finais_v3_parte1.R
- ✅ graficos_finais_v3_parte2.R

**REMOVER (versões antigas):**
- ❌ 01_limpeza_dados.R
- ❌ 02_calculo_indices.py
- ❌ 03_graficos.R
- ❌ 04_teste_robustez.py
- ❌ grafico_sensibilidade.R

---

## 🎨 PASSO 4: Gerar os gráficos

**No terminal, dentro da pasta `scripts/`:**

```bash
# Opção Python (mais fácil)
python gerar_graficos_v3.py
```

**OU em R:**
```r
Rscript graficos_finais_v3_parte1.R
Rscript graficos_finais_v3_parte2.R
```

Isso vai criar 10 arquivos PNG na pasta `graficos/`:
1. 01_trajetoria_trabalhador_tipico.png
2. 02_decomposicao_estrutural_conjuntural.png
3. 03_ganhos_progressivos_percentis.png
4. 04_participacao_trabalho_pib.png
5. 05_desemprego_vs_salario.png
6. 06_massa_salarial_vs_pib.png
7. 07_caged_reversao_dez2025.png
8. 08_criacao_empregos_desaceleracao.png
9. 09_horas_vs_produtividade.png
10. 10_projecoes_2026.png

---

## 📝 PASSO 5: Atualizar documentação na raiz

**SUBSTITUIR:**
- README.md ← usar o novo que está no outputs

**ADICIONAR:**
- METODOLOGIA.md
- RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md

**MANTER:**
- LICENSE (já existe)

---

## 🚀 PASSO 6: Fazer commit e push

```bash
git add .
git commit -m "v3.0: Estudo completo com decomposição estrutural e descoberta de reversão (dez/2025)"
git push origin main
```

---

## ✅ CHECKLIST FINAL

Antes de fazer push, confira:

### Pastas:
- [ ] `dados/` com 7-9 CSVs
- [ ] `graficos/` com 10 PNGs
- [ ] `scripts/` com 3 arquivos (1 .py + 2 .R)

### Documentos na raiz:
- [ ] README.md (atualizado v3.0)
- [ ] METODOLOGIA.md (novo)
- [ ] RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md (novo)
- [ ] LICENSE

### Arquivos REMOVIDOS:
- [ ] Sem arquivos duplicados (brasil_anual.csv vs brasil_anual_CORRIGIDO_FINAL.csv)
- [ ] Sem scripts antigos (01_limpeza_dados.R, etc)
- [ ] Sem dados intermediários (indice_*.csv, comparacao_*.csv)

---

## 🎯 RESULTADO FINAL

Repositório limpo, organizado, profissional:
- **~24 arquivos** (contra 50+ bagunçados antes)
- **Reproduzível:** Qualquer pessoa roda os scripts e gera os gráficos
- **Documentado:** 3 documentos completos (README, METODOLOGIA, RELATÓRIO)
- **Validado:** Todos os dados e scripts testados

---

## 💡 DICAS

**Se der erro ao rodar os scripts:**
1. Verifique se os CSVs estão na pasta `dados/`
2. Verifique se instalou as bibliotecas (pip install / install.packages)
3. Rode dentro da pasta `scripts/` (os caminhos dos CSVs são relativos)

**Se quiser editar os gráficos:**
- Abra o script (Python ou R)
- Procure por "CORES" ou "cores"
- Altere as cores hexadecimais (#2ECC71, etc)
- Procure por "fontsize" ou "size" para mudar tamanhos

**Se quiser adicionar mais dados:**
- Coloque na pasta `dados/`
- Documente no README (seção "Estrutura dos Dados")
- Crie um script novo ou adapte os existentes

---

**Última atualização:** 18 de Fevereiro de 2026  
**Autor:** Vitor Ramos dos Santos

