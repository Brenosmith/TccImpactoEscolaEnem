# Configuração e Instalação do Projeto TCC

> **Guia completo para configuração do ambiente de desenvolvimento no Windows**

## 📋 Requisitos do Sistema

- **Python 3.8+** (recomendado: 3.9 ou 3.10)
- **8GB RAM** mínimo (16GB+ recomendado para datasets grandes)
- **5GB espaço livre** em disco
- **Git** instalado no sistema
- **Windows** com Command Prompt (cmd)

---

## ⚡ Instalação Rápida

### 1️⃣ Clone o repositório

```cmd
git clone https://github.com/Brenosmith/TccImpactoEscolaEnem.git
```

```cmd
cd TccImpactoEscolaEnem
```

### 2️⃣ Configure o ambiente virtual

**Criar o ambiente virtual:**
```cmd
python -m venv venv_tcc
```

**Ativar o ambiente:**
```cmd
venv_tcc\Scripts\activate
```

> **✅ Verificação:** Deve aparecer `(venv_tcc)` no início da linha do terminal.

### 3️⃣ Instale as dependências

**Atualizar o pip:**
```cmd
pip install --upgrade pip
```

**Instalar bibliotecas do projeto:**
```cmd
pip install -r src/requirements.txt
```

> **⏱️ Tempo estimado:** 5-10 minutos

### 4️⃣ Teste a instalação

```cmd
python -c "import pandas, numpy, sklearn, lightgbm, tensorflow, mlflow, shap; print('✅ Instalação concluída com sucesso!')"
```

### 5️⃣ Inicie o Jupyter

**JupyterLab (recomendado):**
```cmd
jupyter lab
```

**Jupyter Notebook (clássico):**
```cmd
jupyter notebook
```

> **📁 Navegação:** Acesse a pasta `src/` para os notebooks do projeto.

---

## 🚀 Como Executar o Projeto

### 🎯 Opção 1: Execução Rápida (Recomendado)

Para resultados imediatos usando bases já processadas:

**📊 Bases disponíveis em `src/Bases/Finais/`:**
- `enem_microdados_2023.pkl` - Base ENEM
- `dados_escolares_2023.pkl` - Variáveis escolares
- `dados_socioeconomicos_2023.pkl` - Variáveis socioeconômicas
- `enem_censo_2023_full.pkl` - Base unificada ENEM + Censo

**🏆 Notebooks principais:**

| Notebook | Descrição |
|----------|-----------|
| `11_Modelagem_Base_Unificada_Todas_Notas.ipynb` | Modelagem final completa |
| `12_SHAP_Base_Unificada_Todas_Notas.ipynb` | Análise de interpretabilidade |
| `4.5_Modelagem_Enem_23_LGBM.ipynb` | Melhor modelo individual |

### 🔄 Opção 2: Pipeline Completo

Para reproduzir todo o processo desde dados brutos:

**� Sequência obrigatória (6-8 horas total):**

| Etapa | Notebooks | Descrição |
|-------|-----------|-----------|
| **1️⃣ Tratamento** | `1.1` → `1.2` → `1.3` → `1.4` → `1.5` | Limpeza e preparação dos dados |
| **2️⃣ Exploração** | `2.1`, `3.1` | Análise exploratória e seleção de features |
| **3️⃣ Modelagem Individual** | `4.1` → `4.2` → `4.3` → `4.4` → `4.5` | Comparação de algoritmos |
| **4️⃣ Modelagem Unificada** | `6.1` → `6.2` → `6.3` → `11.x` | Modelos com dados combinados |

**💡 Dicas de execução:**
- ✅ Execute os notebooks na ordem sequencial
- ⏱️ Aguarde conclusão completa antes do próximo
- 🖥️ Monitore uso de memória (até 8GB RAM)
- 💾 Resultados salvos automaticamente em `src/Resultados/`

---

## 📊 MLflow - Visualização de Experimentos

### O que é o MLflow?
Plataforma para rastrear e comparar experimentos de machine learning.

### 🔧 Como ativar:

**1️⃣ Ative o ambiente virtual:**
```cmd
venv_tcc\Scripts\activate
```

**2️⃣ Navegue para a pasta dos experimentos:**
```cmd
cd src
```

**3️⃣ Inicie a interface:**
```cmd
mlflow ui
```

**4️⃣ Porta alternativa (se necessário):**
```cmd
mlflow ui --port 5001
```

**5️⃣ Acesse no navegador:**
- 🌐 http://localhost:5000 (padrão)
- 🌐 http://localhost:5001 (alternativa)

---

## 🔧 Informações Técnicas

## 📚 Principais Bibliotecas Utilizadas

**Análise de Dados e Manipulação:**
- [`pandas`](https://pandas.pydata.org/) - Manipulação e análise de dados
- [`numpy`](https://numpy.org/) - Computação numérica
- [`openpyxl`](https://openpyxl.readthedocs.io/) - Leitura e escrita de arquivos Excel

**Machine Learning:**
- [`scikit-learn`](https://scikit-learn.org/) - Algoritmos de machine learning
- [`lightgbm`](https://lightgbm.readthedocs.io/) - Gradient boosting framework
- [`xgboost`](https://xgboost.readthedocs.io/) - Extreme gradient boosting
- [`tensorflow`](https://www.tensorflow.org/) - Deep learning e redes neurais

**Visualização:**
- [`matplotlib`](https://matplotlib.org/) - Gráficos e visualizações
- [`seaborn`](https://seaborn.pydata.org/) - Visualizações estatísticas
- [`plotly`](https://plotly.com/python/) - Gráficos interativos

**Interpretabilidade:**
- [`shap`](https://shap.readthedocs.io/) - Explicabilidade de modelos de ML

**Ambiente de Desenvolvimento:**
- [`jupyter`](https://jupyter.org/) - Notebooks interativos
- [`mlflow`](https://mlflow.org/) - Gerenciamento de experimentos de ML

**Otimização:**
- [`scikit-optimize`](https://scikit-optimize.github.io/) - Otimização bayesiana de hiperparâmetros

### 💡 Lembretes importantes:
- 🔄 **Sempre ative o ambiente virtual** antes de trabalhar
- 🔒 **Se fechar o terminal**, reative com `venv_tcc\Scripts\activate`
- 📁 **Navegue até `src/`** para acessar os notebooks
- 💾 **Resultados são salvos automaticamente**

---

## 📚 Links Úteis

- 📖 [README Principal](./README.md) - Descrição completa do projeto
- 🐍 [Documentação Python](https://docs.python.org/)
- 📊 [MLflow Documentation](https://mlflow.org/docs/)
- 📓 [Jupyter Documentation](https://jupyter.org/documentation)

---
