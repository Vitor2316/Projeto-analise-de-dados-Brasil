# 🚀 GUIA PASSO A PASSO - CONFIGURAÇÃO COMPLETA DO REPOSITÓRIO

## 📦 PASSO 1: BAIXAR E DESCOMPACTAR

### 1.1 Baixar arquivo
- Baixe o arquivo `PROJETO_FINAL.tar.gz` que está nos outputs
- Salve na sua pasta de projetos

### 1.2 Descompactar
```bash
# No terminal (Linux/Mac)
tar -xzf PROJETO_FINAL.tar.gz

# No Windows
# Use 7-Zip ou WinRAR para extrair
# Botão direito > Extrair aqui
```

Você terá uma pasta `PROJETO_FINAL/` com tudo dentro.

---

## 📂 PASSO 2: MOVER PARA SEU REPOSITÓRIO GITHUB

### 2.1 Se você JÁ TEM o repositório clonado:

```bash
# Navegue até seu repositório
cd ~/Projeto-analise-de-dados-Brasil

# Copie TODO o conteúdo da pasta PROJETO_FINAL
cp -r ~/Downloads/PROJETO_FINAL/* ./

# OU no Windows (PowerShell):
Copy-Item -Path "C:\Downloads\PROJETO_FINAL\*" -Destination ".\" -Recurse
```

### 2.2 Se você NÃO TEM o repositório clonado ainda:

```bash
# Clone seu repositório
git clone https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil.git
cd Projeto-analise-de-dados-Brasil

# Copie o conteúdo
cp -r ~/Downloads/PROJETO_FINAL/* ./
```

---

## 📋 PASSO 3: ENTENDER A ESTRUTURA

```
Projeto-analise-de-dados-Brasil/
│
├── dados/                     ← 9 arquivos CSV
│   ├── brasil_anual_CORRIGIDO_FINAL.csv
│   ├── percentis_rendimento.csv
│   ├── massa_salarial_validacao.csv
│   ├── desemprego_salario.csv
│   ├── participacao_pib.csv
│   ├── caged_setorial_2025.csv
│   ├── projecoes_2026.csv
│   ├── salario_real_anual_paises.csv (opcional)
│   └── produtividade_anual_paises.csv (opcional)
│
├── graficos/                  ← VAZIO (você vai gerar)
│
├── scripts/                   ← 3 arquivos
│   ├── gerar_graficos_v3.py
│   ├── graficos_finais_v3_parte1.R
│   └── graficos_finais_v3_parte2.R
│
├── LICENSE                    ← MIT License
├── README.md                  ← 🇺🇸 INGLÊS (principal)
├── README_PT.md               ← 🇧🇷 Português
├── README_EN.md               ← 🇺🇸 Cópia do inglês
├── METHODOLOGY.md             ← 🇺🇸 INGLÊS (principal)
├── METHODOLOGY_EN.md          ← 🇺🇸 Cópia do inglês
├── METODOLOGIA_PT.md          ← 🇧🇷 Português
├── RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md  ← PT (52 págs)
└── GUIA_ORGANIZACAO.md        ← Este guia
```

---

## 🎨 PASSO 4: GERAR OS GRÁFICOS

### 4.1 Instalar dependências

**Python:**
```bash
pip install matplotlib numpy pandas seaborn
```

**R (se preferir):**
```r
install.packages(c("ggplot2", "dplyr", "tidyr", "scales", "patchwork"))
```

### 4.2 Rodar script

```bash
# Navegue até a pasta scripts
cd scripts

# Rode o Python
python gerar_graficos_v3.py

# OU rode o R
Rscript graficos_finais_v3_parte1.R
Rscript graficos_finais_v3_parte2.R
```

### 4.3 Verificar resultado

```bash
# Volte para raiz
cd ..

# Veja os gráficos gerados
ls graficos/
```

Você deve ter 10 arquivos PNG na pasta `graficos/`.

---

## 🌍 PASSO 5: CONFIGURAR IDIOMA PRINCIPAL (INGLÊS)

### Por que README.md já é inglês?

Eu já configurei `README.md` como a versão em **INGLÊS**.

### O que isso significa:

1. Quando alguém entra no seu GitHub, vê **README.md** (inglês) primeiro
2. No final do README tem link para `README_PT.md` (português)
3. Recrutadores internacionais veem inglês
4. Brasileiros podem clicar no link português

### Versões duplicadas propositalmente:

- `README.md` = inglês (principal)
- `README_EN.md` = inglês (cópia para referência)
- `README_PT.md` = português

**Mesma coisa para METODOLOGIA:**

- `METHODOLOGY.md` = inglês (principal)
- `METHODOLOGY_EN.md` = inglês (cópia)
- `METODOLOGIA_PT.md` = português

### Se quiser mudar para português como principal:

```bash
# Salve o inglês
mv README.md README_EN.md

# Faça português ser o principal
mv README_PT.md README.md
```

Mas **EU RECOMENDO DEIXAR INGLÊS** como principal!

---

## 🔒 PASSO 6: ENTENDER O LICENSE

### O que é o arquivo LICENSE?

É um arquivo de texto que diz:
```
MIT License

Copyright (c) 2026 Vitor Ramos dos Santos

[texto padrão...]
```

### Você "tem" essa licença porque:

1. **Você criou o projeto** ✅
2. **Você escolheu usar MIT** (licença mais comum em open source)
3. **Você colocou SEU NOME** no copyright

### Isso NÃO significa que você:

❌ Fez algum curso
❌ Pagou por alguma certificação
❌ Recebeu permissão de alguém

### Isso SIM significa que:

✅ Você está dizendo: "esse código é meu, mas todo mundo pode usar"
✅ Você está se protegendo legalmente (sem garantias)
✅ Você está sendo profissional (projetos sérios têm licença)

### É tipo um "Creative Commons" para código!

---

## 🚀 PASSO 7: FAZER COMMIT E PUSH

### 7.1 Ver o que mudou

```bash
git status
```

Deve mostrar:
- Novos arquivos (dados/, scripts/, README.md, etc)
- Arquivos modificados

### 7.2 Adicionar tudo

```bash
git add .
```

### 7.3 Fazer commit

```bash
git commit -m "v3.0: Complete study with structural decomposition and cycle reversal discovery (Dec/2025)"
```

### 7.4 Fazer push

```bash
git push origin main
```

Se der erro de branch:
```bash
git push origin master
```

---

## ✅ PASSO 8: VERIFICAR NO GITHUB

1. Vá no seu GitHub: https://github.com/Vitor2316/Projeto-analise-de-dados-Brasil
2. Você deve ver:
   - README.md renderizado (em inglês)
   - Pastas: dados/, graficos/, scripts/
   - Arquivos: LICENSE, METHODOLOGY.md, etc
   - 10 gráficos PNG na pasta graficos/

---

## 🎯 CHECKLIST FINAL

Antes de considerar "pronto", verifique:

### Arquivos:
- [ ] 9 CSVs na pasta `dados/`
- [ ] 10 PNGs na pasta `graficos/`
- [ ] 3 scripts na pasta `scripts/`
- [ ] LICENSE na raiz
- [ ] README.md em inglês
- [ ] README_PT.md em português
- [ ] METHODOLOGY.md em inglês
- [ ] METODOLOGIA_PT.md em português
- [ ] RELATORIO_FINAL_SALARIOS_BRASIL_2012-2025.md

### Configuração:
- [ ] Inglês como idioma principal (README.md)
- [ ] Link para português no final do README
- [ ] LICENSE com SEU NOME

### Git:
- [ ] `git status` limpo
- [ ] `git push` funcionou
- [ ] GitHub mostra os arquivos

---

## 💡 DICAS FINAIS

### Se der erro ao rodar scripts:

1. **Erro: módulo não encontrado**
   ```bash
   pip install matplotlib numpy pandas seaborn
   ```

2. **Erro: arquivo CSV não encontrado**
   ```bash
   # Rode o script DENTRO da pasta scripts/
   cd scripts
   python gerar_graficos_v3.py
   ```

3. **Gráficos não aparecem**
   ```bash
   # Verifique se pasta graficos/ existe
   mkdir -p ../graficos
   ```

### Para editar gráficos:

Abra `scripts/gerar_graficos_v3.py` e procure por:
- `CORES` - para mudar cores
- `fontsize` - para mudar tamanhos
- `title` - para mudar títulos

### Para adicionar mais dados:

1. Crie novo CSV na pasta `dados/`
2. Adicione descrição no README
3. (Opcional) Crie script para processar

---

## 🌟 PRONTO!

Seu repositório agora é:
- ✅ **Profissional** - tem LICENSE, README bilíngue
- ✅ **Organizado** - pastas claras, arquivos nomeados corretamente
- ✅ **Reproduzível** - qualquer um pode rodar os scripts
- ✅ **Internacional** - inglês como principal, português disponível
- ✅ **Completo** - dados + scripts + gráficos + documentação

**Parabéns! Você tem um portfólio de cientista de dados sênior!** 🚀

---

**Dúvidas?**
- Releia as seções relevantes
- Verifique o CHECKLIST FINAL
- Rode `git status` para ver o que falta

**Última atualização:** 19 de Fevereiro de 2026  
**Autor:** Vitor Ramos dos Santos

