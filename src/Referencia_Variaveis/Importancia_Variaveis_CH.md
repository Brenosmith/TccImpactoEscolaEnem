# Tabela de importância das variáveis nos modelos utilizados

- 📥 [Baixar arquivo Excel (.xlsx)](./Importancia_Variaveis_CH.xlsx) *(clique em "View raw" na página para baixar)*

Esta tabela apresenta a importância relativa das variáveis utilizadas em dois modelos preditivos aplicados no TCC para prever a nota de Ciências Humanas do ENEM. 
O método **SHAP** foi utilizado para interpretar o modelo **LightGBM**, que obteve os melhores resultados nas métricas de avaliação. 
Já as colunas de **Ganho** e **Split** foram extraídas a partir do modelo **Random Forest**, escolhido por sua interpretabilidade 
e bom desempenho, permitindo o cálculo do impacto das variáveis mesmo com menor complexidade computacional.

Colunas:
- Variável: descrição da variável utilizada nos modelos.
- Tipo de Variável: socioeconômica ou escolar.
- SHAP: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante).
- Ganho: posição da variável segundo o ganho médio de informação no Random Forest.
- Split: número total de divisões em que a variável foi utilizada nas árvores do Random Forest.

| Variável                             | Tipo de Variável |   SHAP |   Ganho |   Split |
|:-------------------------------------|:----------------|-------:|--------:|--------:|
| Língua estrangeira                   | Socioeconômica  |      1 |       2 |      98 |
| Renda familiar mensal                | Socioeconômica  |      2 |       1 |      13 |
| Qtde. computadores                   | Socioeconômica  |      3 |       7 |      51 |
| Cor/raça                             | Socioeconômica  |      4 |      14 |      38 |
| Qtde. freezers                       | Socioeconômica  |      5 |      20 |      64 |
| Possui TV por assinatura             | Socioeconômica  |      6 |      43 |      88 |
| Faixa etária                         | Socioeconômica  |      7 |      19 |      28 |
| Cód. município                       | Escolar         |      8 |       3 |       1 |
| Ocupação pai                         | Socioeconômica  |      9 |       8 |      32 |
| Tipo de escola                       | Escolar         |     10 |       6 |      90 |
| Grau estudo mãe                      | Socioeconômica  |     11 |      13 |      35 |
| Dependência administrativa           | Escolar         |     12 |       5 |      79 |
| Grau estudo pai                      | Socioeconômica  |     13 |      12 |      33 |
| Categoria escola privada             | Escolar         |     14 |       4 |     101 |
| UF escola                            | Escolar         |     15 |      17 |       3 |
| Ocupação mãe                         | Socioeconômica  |     16 |      18 |      31 |
| Qtde. micro-ondas                    | Socioeconômica  |     17 |      52 |      62 |
| Qtde. celulares                      | Socioeconômica  |     18 |      31 |      42 |
| Vínculo Sec. Educação                | Escolar         |     19 |      10 |      45 |
| Empresa privada mantened.            | Escolar         |     20 |       9 |      43 |
| Órgão regional                       | Escolar         |     21 |      11 |       2 |
| Pessoas na residência                | Socioeconômica  |     22 |      45 |      37 |
| Qtde. motocicletas                   | Socioeconômica  |     23 |      63 |      46 |
| Qtde. máq. lavar roupa               | Socioeconômica  |     24 |      37 |      68 |
| Qtde. psicólogos                     | Escolar         |     25 |      16 |      30 |
| Região geográfica                    | Escolar         |     26 |      32 |      57 |
| Sala artes                           | Escolar         |     27 |      21 |      26 |
| Possui aspirador                     | Socioeconômica  |     28 |      24 |      83 |
| Não sabe grau estudo mãe             | Socioeconômica  |     29 |      47 |      84 |
| Qtde. máq. secar roupa               | Socioeconômica  |     30 |      79 |      78 |
| Não sabe grau estudo pai             | Socioeconômica  |     31 |      59 |      85 |
| Qtde. monitores                      | Escolar         |     32 |      29 |      16 |
| Qtde. banheiros                      | Socioeconômica  |     33 |      30 |      55 |
| Qtde. quartos                        | Socioeconômica  |     34 |      69 |      41 |
| Qtde. TVs                            | Socioeconômica  |     35 |      49 |      50 |
| Exame seleção                        | Escolar         |     36 |      34 |     100 |
| Matrículas ens. médio                | Escolar         |     37 |      15 |       5 |
| Qtde. carros                         | Socioeconômica  |     38 |      35 |      47 |
| Qtde. de Dias empregado(a)           | Socioeconômica  |     39 |      50 |      60 |
| Educação profissional                | Escolar         |     40 |      38 |      23 |
| Auditório                            | Escolar         |     41 |      42 |      24 |
| Nacionalidade                        | Socioeconômica  |     42 |      68 |      73 |
| Qtde. desktop alunos                 | Escolar         |     43 |      33 |       4 |
| Sala música                          | Escolar         |     44 |      40 |      21 |
| Qtde. bibliotecários                 | Escolar         |     45 |      27 |       9 |
| Possui internet                      | Socioeconômica  |     46 |      66 |      95 |
| Tipo de instituição                  | Escolar         |     47 |      57 |      72 |
| Turmas ens. médio                    | Escolar         |     48 |      23 |      11 |
| Qtde. geladeiras                     | Socioeconômica  |     49 |      84 |      65 |
| Estado civil                         | Socioeconômica  |     50 |      80 |      74 |
| Mantened. sistema S                  | Escolar         |     51 |      28 |      52 |
| Matrículas tempo integral            | Escolar         |     52 |      36 |       6 |
| Qtde. projetores                     | Escolar         |     53 |      53 |      12 |
| Sexo                                 | Socioeconômica  |     54 |      82 |      69 |
| Qtde. tablets alunos                 | Escolar         |     55 |      65 |      19 |
| Mantened. sem fins lucr.             | Escolar         |     56 |      25 |      49 |
| Lab. ciências                        | Escolar         |     57 |      55 |      22 |
| Parceria poder público               | Escolar         |     58 |      22 |      58 |
| Área verde                           | Escolar         |     59 |      64 |      25 |
| Qtde. pedagogos                      | Escolar         |     60 |      54 |      14 |
| Possui telefone fixo                 | Socioeconômica  |     61 |      94 |      89 |
| Docentes ens. médio                  | Escolar         |     62 |      26 |       7 |
| Qtde. lousas digitais                | Escolar         |     63 |      44 |      20 |
| Qtde. máq. lavar louça               | Socioeconômica  |     64 |      73 |      77 |
| Possui DVD                           | Socioeconômica  |     65 |      76 |      82 |
| Qtde. salas aula                     | Escolar         |     66 |      41 |       8 |
| Mantened. sindicato                  | Escolar         |     67 |      46 |      62 |
| Lab. informática                     | Escolar         |     68 |      48 |      29 |
| Quadra esportes                      | Escolar         |     69 |      51 |      17 |
| Qtde. notebooks alunos               | Escolar         |     70 |      56 |      10 |
| Funciona outra escola                | Escolar         |     71 |      71 |      40 |
| Qtde. televisores                    | Escolar         |     72 |      62 |      15 |
| Turmas tempo integral                | Escolar         |     73 |      58 |      18 |
| Ocupação prédio escolar              | Escolar         |     74 |      78 |      99 |
| Biblioteca                           | Escolar         |     75 |      72 |      34 |
| Proposta pedagógica atualizada       | Escolar         |     76 |      93 |      92 |
| Piscina                              | Escolar         |     77 |      39 |      39 |
| Vínculo Seg. Pública                 | Escolar         |     78 |      81 |      53 |
| Mantened. ONG                        | Escolar         |     79 |      60 |      80 |
| Internet alunos                      | Escolar         |     80 |      61 |      27 |
| Aulas semipresenciais                | Escolar         |     81 |      91 |      67 |
| Aulas EAD                            | Escolar         |     82 |      67 |      44 |
| Sem tratamento lixo                  | Escolar         |     83 |      90 |      97 |
| Matrículas normal/magistério         | Escolar         |     84 |      77 |      61 |
| Internet ensino                      | Escolar         |     85 |      70 |      36 |
| Vínculo outro órgão                  | Escolar         |     86 |      89 |      91 |
| Localização                          | Escolar         |     87 |      98 |     102 |
| Funciona prédio escolar              | Escolar         |     88 |      86 |      70 |
| Funciona prisional/socio             | Escolar         |     89 |      75 |      66 |
| Sem material pedagógico              | Escolar         |     90 |      83 |      56 |
| Funciona outros                      | Escolar         |     91 |      74 |      48 |
| Água potável                         | Escolar         |     92 |      88 |      59 |
| Funciona prisional                   | Escolar         |     93 |      85 |      71 |
| Aulas presenciais                    | Escolar         |     94 |      87 |      54 |
| Mantened. ONG/OSCIP                  | Escolar         |     95 |      96 |      87 |
| Sit. funcionamento escola            | Escolar         |     96 |     101 |      93 |
| Funciona socioeducativo              | Escolar         |     97 |      91 |      75 |
| Sem esgoto                           | Escolar         |     98 |      95 |      76 |
| Funciona galpão                      | Escolar         |     99 |     100 |      86 |
| Banheiro                             | Escolar         |    100 |      97 |      81 |
| Mantened. OSCIP                      | Escolar         |    101 |      99 |      94 |
| Localização diferenciada             | Escolar         |    102 |     103 |     104 |
| Sem água                             | Escolar         |    103 |     102 |      96 |
| Sem energia                          | Escolar         |    104 |     104 |     103 |
| Vínculo Sec. Saúde                   | Escolar         |    105 |     105 |     105 |
| Ocupação galpão                      | Escolar         |    106 |     106 |     106 |
