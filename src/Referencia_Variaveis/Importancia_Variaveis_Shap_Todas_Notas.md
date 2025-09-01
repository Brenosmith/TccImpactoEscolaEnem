# Tabela de importância das variáveis nos modelos utilizados

- 📥 [Baixar arquivo Excel (.xlsx)](./Importancia_Variaveis_Shap_Todas_Notas.xlsx) *(clique em "View raw" na página para baixar)*

Esta tabela apresenta a importância relativa das variáveis utilizadas nos modelos LightGBM para todas as notas do ENEM. 
O método **SHAP** foi utilizado para interpretar o modelo **LightGBM**, que obteve os melhores resultados nas métricas de avaliação. 

Colunas:
- Descrição: descrição da variável utilizada nos modelos.
- Tipo de Variável: socioeconômica ou escolar.
- Posição SHAP NUM_NOTA_MT: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Matemática.
- Posição SHAP NUM_NOTA_LC: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Linguagens.
- Posição SHAP NUM_NOTA_CN: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Ciências da Natureza.
- Posição SHAP NUM_NOTA_CH: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Ciências Humanas.
- Posição SHAP NUM_NOTA_REDACAO: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Redação.

