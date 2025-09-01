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

| Variável                             |   SHAP |   Ganho |   Split |
|:-------------------------------------|-------:|--------:|--------:|
| Língua estrangeira                   |      1 |       2 |      98 |
| Renda familiar mensal                |      2 |       1 |      13 |
| Qtde. computadores                   |      3 |       7 |      51 |
| Cor/raça                             |      4 |      14 |      38 |
| Qtde. freezers                       |      5 |      20 |      64 |
| Possui TV por assinatura             |      6 |      43 |      88 |
| Faixa etária                         |      7 |      19 |      28 |
| Cód. município                       |      8 |       3 |       1 |
| Ocupação pai                         |      9 |       8 |      32 |
| Tipo de escola                       |     10 |       6 |      90 |
| Grau estudo mãe                      |     11 |      13 |      35 |
| Dependência administrativa           |     12 |       5 |      79 |
| Grau estudo pai                      |     13 |      12 |      33 |
| Categoria escola privada             |     14 |       4 |     101 |
| UF escola                            |     15 |      17 |       3 |
| Ocupação mãe                         |     16 |      18 |      31 |
| Qtde. micro-ondas                    |     17 |      52 |      62 |
| Qtde. celulares                      |     18 |      31 |      42 |
| Vínculo Sec. Educação                |     19 |      10 |      45 |
| Empresa privada mantened.            |     20 |       9 |      43 |
| Órgão regional                       |     21 |      11 |       2 |
| Pessoas na residência                |     22 |      45 |      37 |
| Qtde. motocicletas                   |     23 |      63 |      46 |
| Qtde. máq. lavar roupa               |     24 |      37 |      68 |
| Qtde. psicólogos                     |     25 |      16 |      30 |
| Região geográfica                    |     26 |      32 |      57 |
| Sala artes                           |     27 |      21 |      26 |
| Possui aspirador                     |     28 |      24 |      83 |
| Não sabe grau estudo mãe             |     29 |      47 |      84 |
| Qtde. máq. secar roupa               |     30 |      79 |      78 |
| Não sabe grau estudo pai             |     31 |      59 |      85 |
| Qtde. monitores                      |     32 |      29 |      16 |
| Qtde. banheiros                      |     33 |      30 |      55 |
| Qtde. quartos                        |     34 |      69 |      41 |
| Qtde. TVs                            |     35 |      49 |      50 |
| Exame seleção                        |     36 |      34 |     100 |
| Matrículas ens. médio                |     37 |      15 |       5 |
| Qtde. carros                         |     38 |      35 |      47 |
| Dias empregado(a) doméstico(a)       |     39 |      50 |      60 |
| Educação profissional                |     40 |      38 |      23 |
| Auditório                            |     41 |      42 |      24 |
| Nacionalidade                        |     42 |      68 |      73 |
| Qtde. desktop alunos                 |     43 |      33 |       4 |
| Sala música                          |     44 |      40 |      21 |
| Qtde. bibliotecários                 |     45 |      27 |       9 |
| Possui internet                      |     46 |      66 |      95 |
| Tipo de instituição                  |     47 |      57 |      72 |
| Turmas ens. médio                    |     48 |      23 |      11 |
| Qtde. geladeiras                     |     49 |      84 |      65 |
| Estado civil                         |     50 |      80 |      74 |
| Mantened. sistema S                  |     51 |      28 |      52 |
| Matrículas tempo integral            |     52 |      36 |       6 |
| Qtde. projetores                     |     53 |      53 |      12 |
| Sexo                                 |     54 |      82 |      69 |
| Qtde. tablets alunos                 |     55 |      65 |      19 |
| Mantened. sem fins lucr.             |     56 |      25 |      49 |
| Lab. ciências                        |     57 |      55 |      22 |
| Parceria poder público               |     58 |      22 |      58 |
| Área verde                           |     59 |      64 |      25 |
| Qtde. pedagogos                      |     60 |      54 |      14 |
| Possui telefone fixo                 |     61 |      94 |      89 |
| Docentes ens. médio                  |     62 |      26 |       7 |
| Qtde. lousas digitais                |     63 |      44 |      20 |
| Qtde. máq. lavar louça               |     64 |      73 |      77 |
| Possui DVD                           |     65 |      76 |      82 |
| Qtde. salas aula                     |     66 |      41 |       8 |
| Mantened. sindicato                  |     67 |      46 |      62 |
| Lab. informática                     |     68 |      48 |      29 |
| Quadra esportes                      |     69 |      51 |      17 |
| Qtde. notebooks alunos               |     70 |      56 |      10 |
| Funciona outra escola                |     71 |      71 |      40 |
| Qtde. televisores                    |     72 |      62 |      15 |
| Turmas tempo integral                |     73 |      58 |      18 |
| Ocupação prédio escolar              |     74 |      78 |      99 |
| Biblioteca                           |     75 |      72 |      34 |
| Proposta pedagógica atualizada       |     76 |      93 |      92 |
| Piscina                              |     77 |      39 |      39 |
| Vínculo Seg. Pública                 |     78 |      81 |      53 |
| Mantened. ONG                        |     79 |      60 |      80 |
| Internet alunos                      |     80 |      61 |      27 |
| Aulas semipresenciais                |     81 |      91 |      67 |
| Aulas EAD                            |     82 |      67 |      44 |
| Sem tratamento lixo                  |     83 |      90 |      97 |
| Matrículas normal/magistério         |     84 |      77 |      61 |
| Internet ensino                      |     85 |      70 |      36 |
| Vínculo outro órgão                  |     86 |      89 |      91 |
| Localização                          |     87 |      98 |     102 |
| Funciona prédio escolar              |     88 |      86 |      70 |
| Funciona prisional/socio             |     89 |      75 |      66 |
| Sem material pedagógico              |     90 |      83 |      56 |
| Funciona outros                      |     91 |      74 |      48 |
| Água potável                         |     92 |      88 |      59 |
| Funciona prisional                   |     93 |      85 |      71 |
| Aulas presenciais                    |     94 |      87 |      54 |
| Mantened. ONG/OSCIP                  |     95 |      96 |      87 |
| Sit. funcionamento escola            |     96 |     101 |      93 |
| Funciona socioeducativo              |     97 |      91 |      75 |
| Sem esgoto                           |     98 |      95 |      76 |
| Funciona galpão                      |     99 |     100 |      86 |
| Banheiro                             |    100 |      97 |      81 |
| Mantened. OSCIP                      |    101 |      99 |      94 |
| Localização diferenciada             |    102 |     103 |     104 |
| Sem água                             |    103 |     102 |      96 |
| Sem energia                          |    104 |     104 |     103 |
| Vínculo Sec. Saúde                   |    105 |     105 |     105 |
| Ocupação galpão                      |    106 |     106 |     106 |
