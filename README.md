# TCC MBA USP ESALQ
#### Trabalho de conclusão de curso do MBA em Data Science e Analytics da USP ESALQ

> **🛠️ [📋 Guia de Configuração e Instalação](./README-SETUP.md)** - Instruções completas para configurar o ambiente de desenvolvimento

## Título: Impacto das Escolas no Desempenho ENEM: Comparação de Modelos Preditivos com Dados Educacionais e Socioeconômicos

Este repositório contém os materiais de apoio ao TCC: código, análises e dados suplementares.

## 📋 Resumo do Projeto

Este trabalho desenvolveu **modelos de machine learning** para prever as notas do **ENEM 2023** a partir da integração dos microdados do exame com informações do **Censo Escolar**, analisando a influência de fatores escolares e socioeconômicos no desempenho dos estudantes.

### 🎯 Objetivo
Quantificar e comparar o impacto relativo dos fatores **socioeconômicos** versus **escolares** no desempenho dos estudantes no ENEM.

### 📊 Dados Utilizados
- **+700 mil registros** de candidatos do ENEM 2023
- **Microdados do ENEM 2023** (socioeconômicos e demográficos)
- **Censo Escolar 2023** (infraestrutura e características das escolas)
- **Base unificada** com variáveis escolares e socioeconômicas

### 🤖 Modelos Implementados
- **Árvore de Decisão**
- **Random Forest**
- **XGBoost**
- **Redes Neurais**
- **LightGBM** (melhor performance)

### 🔍 Metodologia
1. **Tratamento de dados** (remoção de outliers, feature engineering)
2. **Integração das bases** ENEM + Censo Escolar  
3. **Modelagem comparativa** com diferentes algoritmos
4. **Análise de importância** usando SHAP values
5. **Validação estatística** dos resultados

## 🏆 Principais Resultados

### 📈 Métricas de Performance do Modelo LightGBM

| **Métrica** | **Ciências Humanas** | **Ciências da Natureza** | **Linguagens** | **Matemática** | **Redação** |
|-------------|----------------------|---------------------------|----------------|----------------|-------------|
| **MAE**     | 54,87                | 51,80                     | 47,38          | 78,71          | 134,32      |
| **RMSE**    | 69,59                | 64,83                     | 60,59          | 97,26          | 180,27      |
| **R²**      | **0,3207**           | **0,3428**                | **0,3233**     | **0,4171**     | **0,3037**  |

- **Melhor performance**: Matemática (R² = 0,4171)
- **Menor erro**: Linguagens (MAE = 47,38)
- **Maior variabilidade**: Redação (RMSE = 180,27)

---

### 🎯 Impacto dos Fatores por Disciplina (Análise SHAP)

| **Tipo de Variável** | **Ciências Humanas** | **Ciências da Natureza** | **Linguagens** | **Matemática** | **Redação** |
|----------------------|----------------------|---------------------------|----------------|----------------|-------------|
| **Socioeconômica**   | **66,1%**            | **64,5%**                 | **68,1%**      | **66,6%**      | **66,1%**   |
| **Escolar**          | **33,9%**            | **35,5%**                 | **31,9%**      | **33,4%**      | **33,9%**   |

**Principais insights:**
- **Maior impacto socioeconômico**: Linguagens (68,1%)
- **Maior impacto escolar**: Ciências da Natureza (35,5%)
- **Padrão consistente**: Fatores socioeconômicos predominam em todas as disciplinas (~2:1)

---

### 🔬 Comparativo de Performance por Conjunto de Variáveis (Ciências Humanas)

| **Métrica** | **Escolares** | **Socioeconômicos** | **ENEM** | **Completo** |
|-------------|---------------|---------------------|----------|--------------|
| **MAE**     | 58,80         | 56,57               | 54,85    | **54,88**    |
| **RMSE**    | 73,99         | 71,55               | 69,60    | **69,59**    |
| **R²**      | 0,2322        | 0,2820              | 0,3204   | **0,3207**   |

**Análise comparativa:**
- 🏆 **Modelo Completo**: Melhor performance geral (R² = 0,3207)
- 📊 **Dados ENEM**: Performance muito próxima ao modelo completo
- 💰 **Variáveis Socioeconômicas**: Superam significativamente as escolares
- 🏫 **Variáveis Escolares**: Menor poder preditivo isoladamente

**Ganho incremental**: A combinação de todos os dados oferece apenas **0,03%** de melhoria sobre os dados do ENEM sozinhos, evidenciando a alta qualidade das variáveis originais do exame.

## 📁 Recursos do Repositório

### 🗂️ Estrutura do Projeto

```
src/
├── 1.x_Tratamento_*.ipynb        # 📊 Tratamento e preparação dos dados
├── 2.x_Analise_*.ipynb           # 🔍 Análise exploratória
├── 3.x_Analise_*.ipynb           # 📈 Análise de importância das variáveis
├── 4.x_Modelagem_*.ipynb         # 🤖 Modelagem (Árvore, RF, XGB, RNA, LGBM)
├── 5.x_Analise_*.ipynb           # 📋 Análise de resultados
├── 6.x_Modelagem_*.ipynb         # 🔬 Modelagem por grupos (Escolares, Socioeconômicos, Unificada)
├── 7.x_Modelagem_*.ipynb         # 🧠 Testes adicionais com RNA
├── 8.x_Analise_*.ipynb           # 📊 Análise de resultados unificados
├── 9.x_Validacao_*.ipynb         # 📐 Validação estatística
├── 10_SHAP_*.ipynb               # 🎯 Análise SHAP (base unificada)
├── 11_Modelagem_*.ipynb          # 🚀 Modelagem final (todas as notas)
├── 12_SHAP_*.ipynb               # 🎯 Análise SHAP (todas as notas)
├── Dicionarios_Listas_Auxiliares.py  # 📚 Dicionários e listas
├── Funcoes_Comuns.py             # 🛠️ Funções comuns (métricas, MLflow)
├── Funcoes_Shap.py               # 🎯 Funções para análise SHAP
├── requirements.txt              # 📦 Dependências do projeto
├── Bases/Finais/                 # 📊 Datasets finais tratados
├── Modelos/                      # 🤖 Modelos treinados (.pkl)
├── Resultados/                   # 📈 Gráficos, outputs e análises
├── Referencia_Variaveis/         # 📚 Documentação das variáveis
└── mlruns/                       # 🔬 Experimentos MLflow
```

### 📊 Bases de Dados Tratadas (Prontas para Modelagem)
- [📈 `enem_microdados_2023.pkl`](./src/Bases/Finais/enem_microdados_2023.pkl) - Base ENEM 2023 tratada
- [🏫 `dados_escolares_2023.pkl`](./src/Bases/Finais/dados_escolares_2023.pkl) - Somente variáveis escolares (Censo + ENEM)
- [💰 `dados_socioeconomicos_2023.pkl`](./src/Bases/Finais/dados_socioeconomicos_2023.pkl) - Somente variáveis socioeconômicas (ENEM)
- [🔗 `enem_censo_2023_full.pkl`](./src/Bases/Finais/enem_censo_2023_full.pkl) - Base unificada completa (ENEM + Censo)

> ✅ **Datasets finais**: Todas as bases passaram por limpeza, feature engineering e estão prontas para aplicação direta nos algoritmos de ML

### 📄 Documentação
- [📄 Tabela descritiva das variáveis utilizadas do ENEM](./src/Referencia_Variaveis/Variaveis_Utilizadas_ENEM.md)
- [📄 Tabela descritiva das variáveis utilizadas do Censo Escolar](./src/Referencia_Variaveis/Variaveis_Utilizadas_Censo.md)

### 📈 Resultados Detalhados
- [📄 Ranking de importância das variáveis para Ciências Humanas (SHAP, ganho e split)](./src/Referencia_Variaveis/Importancia_Variaveis_CH.md)
- [📄 Ranking de importância das variáveis para todas as notas (SHAP)](./src/Referencia_Variaveis/Importancia_Variaveis_Shap_Todas_Notas.md)

---
 