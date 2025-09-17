# Tabela de importância das variáveis nos modelos utilizados

- 📥 [Baixar arquivo Excel (.xlsx)](./Importancia_Variaveis_Shap_Todas_Notas.xlsx) *(clique em "View raw" na página para baixar)*

Esta tabela apresenta a importância relativa das variáveis utilizadas nos modelos **LightGBM** para todas as notas do ENEM.  
O método **SHAP** foi utilizado para interpretar o modelo **LightGBM**, que obteve os melhores resultados nas métricas de avaliação. 

Colunas:
- **Descrição**: descrição da variável utilizada nos modelos.
- **Tipo de Variável**: socioeconômica ou escolar.
- **Posição SHAP NUM_NOTA_MT**: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Matemática.
- **Posição SHAP NUM_NOTA_LC**: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Linguagens.
- **Posição SHAP NUM_NOTA_CN**: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Ciências da Natureza.
- **Posição SHAP NUM_NOTA_CH**: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Ciências Humanas.
- **Posição SHAP NUM_NOTA_REDACAO**: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante) para a nota de Redação.

| Descrição                            | Tipo de Variável |   Posição SHAP NUM_NOTA_MT |   Posição SHAP NUM_NOTA_LC |   Posição SHAP NUM_NOTA_CN |   Posição SHAP NUM_NOTA_CH |   Posição SHAP NUM_NOTA_REDACAO |
|:-------------------------------------|:-----------------|---------------------------:|---------------------------:|---------------------------:|---------------------------:|--------------------------------:|
| Sexo                                 | Socioeconômica   |                          1 |                         14 |                          3 |                         43 |                               1 |
| Língua estrangeira                   | Socioeconômica   |                          2 |                          1 |                          1 |                          1 |                               2 |
| Renda familiar mensal                | Socioeconômica   |                          3 |                          2 |                          2 |                          2 |                               4 |
| Qtde. computadores                   | Socioeconômica   |                          4 |                          3 |                          4 |                          3 |                               9 |
| Cor/raça                             | Socioeconômica   |                          5 |                          4 |                          5 |                          4 |                              10 |
| Qtde. freezers                       | Socioeconômica   |                          6 |                          5 |                          7 |                          5 |                              12 |
| Dependência administrativa           | Escolar          |                          7 |                         17 |                          6 |                          6 |                               7 |
| Cód. município                       | Escolar          |                          8 |                          9 |                         12 |                          7 |                               6 |
| Faixa etária                         | Socioeconômica   |                          9 |                          7 |                         18 |                          8 |                               3 |
| Tipo de escola                       | Escolar          |                         10 |                         21 |                         10 |                         15 |                              14 |
| Possui TV por assinatura             | Socioeconômica   |                         11 |                         10 |                          9 |                          9 |                              21 |
| Ocupação pai                         | Socioeconômica   |                         12 |                          6 |                         16 |                         11 |                              13 |
| Vínculo Sec. Educação                | Escolar          |                         13 |                         11 |                          8 |                         10 |                               5 |
| Grau estudo mãe                      | Socioeconômica   |                         14 |                         13 |                         15 |                         13 |                              18 |
| UF escola                            | Escolar          |                         15 |                          8 |                         11 |                         12 |                               8 |
| Grau estudo pai                      | Socioeconômica   |                         16 |                         12 |                         13 |                         14 |                              20 |
| Categoria escola privada             | Escolar          |                         17 |                         16 |                         14 |                         16 |                              11 |
| Órgão regional                       | Escolar          |                         18 |                         18 |                         17 |                         18 |                              15 |
| Qtde. celulares                      | Socioeconômica   |                         19 |                         20 |                         21 |                         20 |                              29 |
| Empresa privada mantened.            | Escolar          |                         20 |                         22 |                         22 |                         22 |                              17 |
| Ocupação mãe                         | Socioeconômica   |                         21 |                         15 |                         23 |                         17 |                              16 |
| Qtde. máq. lavar roupa               | Socioeconômica   |                         22 |                         24 |                         26 |                         23 |                              19 |
| Qtde. psicólogos                     | Escolar          |                         23 |                         25 |                         25 |                         25 |                              23 |
| Qtde. banheiros                      | Socioeconômica   |                         24 |                         48 |                         28 |                         45 |                              41 |
| Região geográfica                    | Escolar          |                         25 |                         47 |                         41 |                         26 |                              28 |
| Pessoas na residência                | Socioeconômica   |                         26 |                         19 |                         24 |                         21 |                              24 |
| Qtde. micro-ondas                    | Socioeconômica   |                         27 |                         26 |                         19 |                         19 |                              31 |
| Não sabe grau estudo pai             | Socioeconômica   |                         28 |                         34 |                         37 |                         30 |                              22 |
| Qtde. desktop alunos                 | Escolar          |                         29 |                         30 |                         30 |                         34 |                              39 |
| Exame seleção                        | Escolar          |                         30 |                         39 |                         33 |                         31 |                              30 |
| Qtde. carros                         | Socioeconômica   |                         31 |                         28 |                         51 |                         35 |                              52 |
| Qtde. quartos                        | Socioeconômica   |                         32 |                         35 |                         35 |                         36 |                              37 |
| Não sabe grau estudo mãe             | Socioeconômica   |                         33 |                         31 |                         34 |                         28 |                              27 |
| Mantened. sem fins lucr.             | Escolar          |                         34 |                         33 |                         20 |                         33 |                              34 |
| Qtde. motocicletas                   | Socioeconômica   |                         35 |                         23 |                         29 |                         24 |                              25 |
| Auditório                            | Escolar          |                         36 |                         41 |                         32 |                         40 |                              26 |
| Qtde. monitores                      | Escolar          |                         37 |                         29 |                         39 |                         37 |                              40 |
| Possui aspirador                     | Socioeconômica   |                         38 |                         40 |                         31 |                         39 |                              69 |
| Tipo de instituição                  | Escolar          |                         39 |                         46 |                         50 |                         44 |                              32 |
| Qtde. geladeiras                     | Socioeconômica   |                         40 |                         42 |                         42 |                         48 |                              46 |
| Qtde. máq. secar roupa               | Socioeconômica   |                         41 |                         32 |                         36 |                         29 |                              50 |
| Qtde. de Dias empregado(a)          | Socioeconômica   |                         42 |                         37 |                         40 |                         38 |                              55 |
| Qtde. projetores                     | Escolar          |                         43 |                         50 |                         49 |                         51 |                              42 |
| Estado civil                         | Socioeconômica   |                         44 |                         52 |                         61 |                         47 |                              43 |
| Matrículas ens. médio                | Escolar          |                         45 |                         51 |                         59 |                         56 |                              33 |
| Qtde. TVs                            | Socioeconômica   |                         46 |                         38 |                         27 |                         32 |                              58 |
| Nacionalidade                        | Socioeconômica   |                         47 |                         44 |                         44 |                         42 |                              51 |
| Turmas ens. médio                    | Escolar          |                         48 |                         77 |                         56 |                         50 |                              35 |
| Educação profissional                | Escolar          |                         49 |                         36 |                         47 |                         41 |                              45 |
| Sala artes                           | Escolar          |                         50 |                         27 |                         43 |                         27 |                              75 |
| Mantened. sistema S                  | Escolar          |                         51 |                         65 |                         73 |                         59 |                              38 |
| Parceria poder público               | Escolar          |                         52 |                         61 |                         38 |                         71 |                              77 |
| Sala música                          | Escolar          |                         53 |                         57 |                         45 |                         46 |                              74 |
| Docentes ens. médio                  | Escolar          |                         54 |                         49 |                         53 |                         52 |                              56 |
| Qtde. bibliotecários                 | Escolar          |                         55 |                         45 |                         55 |                         53 |                              48 |
| Possui internet                      | Socioeconômica   |                         56 |                         43 |                         64 |                         49 |                              36 |
| Matrículas tempo integral            | Escolar          |                         57 |                         55 |                         52 |                         67 |                              49 |
| Lab. ciências                        | Escolar          |                         58 |                         58 |                         48 |                         58 |                              44 |
| Qtde. lousas digitais                | Escolar          |                         59 |                         60 |                         66 |                         54 |                              70 |
| Qtde. pedagogos                      | Escolar          |                         60 |                         62 |                         54 |                         62 |                              68 |
| Qtde. salas aula                     | Escolar          |                         61 |                         53 |                         65 |                         60 |                              67 |
| Turmas tempo integral                | Escolar          |                         62 |                         67 |                         68 |                         66 |                              60 |
| Possui DVD                           | Socioeconômica   |                         63 |                         56 |                         60 |                         63 |                              54 |
| Qtde. máq. lavar louça               | Socioeconômica   |                         64 |                         54 |                         62 |                         57 |                              61 |
| Qtde. tablets alunos                 | Escolar          |                         65 |                         64 |                         72 |                         65 |                              81 |
| Vínculo Seg. Pública                 | Escolar          |                         66 |                         87 |                         58 |                         68 |                              63 |
| Biblioteca                           | Escolar          |                         67 |                         79 |                         67 |                         77 |                              53 |
| Qtde. televisores                    | Escolar          |                         68 |                         70 |                         76 |                         70 |                              72 |
| Internet alunos                      | Escolar          |                         69 |                         80 |                         83 |                         81 |                              64 |
| Internet ensino                      | Escolar          |                         70 |                         76 |                         87 |                         78 |                              78 |
| Mantened. sindicato                  | Escolar          |                         71 |                         59 |                         57 |                         69 |                              71 |
| Qtde. notebooks alunos               | Escolar          |                         72 |                         73 |                         71 |                         61 |                              57 |
| Lab. informática                     | Escolar          |                         73 |                         66 |                         69 |                         73 |                              62 |
| Funciona prédio escolar              | Escolar          |                         74 |                         69 |                         70 |                         82 |                              93 |
| Área verde                           | Escolar          |                         75 |                         71 |                         63 |                         64 |                              47 |
| Possui telefone fixo                 | Socioeconômica   |                         76 |                         75 |                         46 |                         55 |                              92 |
| Aulas EAD                            | Escolar          |                         77 |                         74 |                         74 |                         75 |                              73 |
| Ocupação prédio escolar              | Escolar          |                         78 |                         84 |                         77 |                         88 |                              97 |
| Vínculo outro órgão                  | Escolar          |                         79 |                         83 |                         94 |                         86 |                             102 |
| Quadra esportes                      | Escolar          |                         80 |                         63 |                         85 |                         72 |                              59 |
| Funciona outra escola                | Escolar          |                         81 |                         68 |                         75 |                         74 |                              80 |
| Piscina                              | Escolar          |                         82 |                         78 |                         81 |                         85 |                              66 |
| Matrículas normal/magistério         | Escolar          |                         83 |                         85 |                         79 |                         79 |                              79 |
| Localização                          | Escolar          |                         84 |                         81 |                        103 |                         84 |                              76 |
| Mantened. ONG/OSCIP                  | Escolar          |                         85 |                         89 |                         80 |                         96 |                              89 |
| Aulas semipresenciais                | Escolar          |                         86 |                         72 |                         84 |                         76 |                              65 |
| Sem material pedagógico              | Escolar          |                         87 |                         82 |                         82 |                         83 |                              82 |
| Funciona prisional                   | Escolar          |                         88 |                         98 |                         92 |                         94 |                              95 |
| Funciona outros                      | Escolar          |                         89 |                         91 |                         88 |                         95 |                              91 |
| Sit. funcionamento escola            | Escolar          |                         90 |                         96 |                         90 |                         92 |                              96 |
| Água potável                         | Escolar          |                         91 |                         92 |                         86 |                         91 |                              85 |
| Funciona socioeducativo              | Escolar          |                         92 |                         88 |                         89 |                         87 |                              99 |
| Sem tratamento lixo                  | Escolar          |                         93 |                         99 |                         98 |                         93 |                              87 |
| Mantened. ONG                        | Escolar          |                         94 |                         95 |                         96 |                         97 |                              98 |
| Funciona prisional/socio             | Escolar          |                         95 |                         90 |                         95 |                         89 |                              90 |
| Proposta pedagógica atualizada       | Escolar          |                         96 |                         93 |                        100 |                         80 |                              88 |
| Aulas presenciais                    | Escolar          |                         97 |                         86 |                         91 |                         90 |                              83 |
| Funciona galpão                      | Escolar          |                         98 |                         97 |                         78 |                         98 |                              86 |
| Banheiro                             | Escolar          |                         99 |                         94 |                         97 |                         99 |                              84 |
| Mantened. OSCIP                      | Escolar          |                        100 |                        101 |                         99 |                        100 |                             101 |
| Sem esgoto                           | Escolar          |                        101 |                        100 |                        101 |                        101 |                             100 |
| Localização diferenciada             | Escolar          |                        102 |                        103 |                         93 |                        102 |                              94 |
| Sem água                             | Escolar          |                        103 |                        102 |                        102 |                        103 |                             103 |
| Sem energia                          | Escolar          |                        104 |                        104 |                        104 |                        104 |                             104 |
| Vínculo Sec. Saúde                   | Escolar          |                        105 |                        105 |                        105 |                        105 |                             105 |
| Ocupação galpão                      | Escolar          |                        106 |                        106 |                        106 |                        106 |                             106 |
