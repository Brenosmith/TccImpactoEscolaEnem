# Tabela de importância das variáveis nos modelos utilizados

- 📥 [Baixar arquivo Excel (.xlsx)](./Importancia_Variaveis.xlsx) *(clique em "View raw" na página para baixar)*

Esta tabela apresenta a importância relativa das variáveis utilizadas em dois modelos preditivos aplicados no TCC para prever a nota de Ciências Humanas do ENEM. 
O método **SHAP** foi utilizado para interpretar o modelo **LightGBM**, que obteve os melhores resultados nas métricas de avaliação. 
Já as colunas de **Ganho** e **Split** foram extraídas a partir do modelo **Random Forest**, escolhido por sua interpretabilidade 
e bom desempenho, permitindo o cálculo do impacto das variáveis mesmo com menor complexidade computacional.

Colunas:
- Variável: descrição da variável utilizada nos modelos.
- SHAP: posição de importância da variável segundo os valores SHAP do modelo LightGBM (1 = mais importante).
- Ganho: posição da variável segundo o ganho médio de informação no Random Forest.
- Split: número total de divisões em que a variável foi utilizada nas árvores do Random Forest.

| Variável                             |   SHAP |   Ganho |   Split |
|:-------------------------------------|-------:|--------:|--------:|
| Língua estrangeira                   |      1 |       2 |      60 |
| Renda familiar mensal                |      2 |       1 |       6 |
| Qtde. computadores                   |      3 |       4 |      29 |
| Cor/raça                             |      4 |      11 |      27 |
| Qtde. freezers                       |      5 |      24 |      42 |
| Possui TV por assinatura             |      6 |      35 |      68 |
| Faixa etária                         |      7 |      19 |      16 |
| Ocupação pai                         |      8 |       7 |      18 |
| Categoria escola privada             |      9 |       3 |     103 |
| UF escola                            |     10 |      15 |       3 |
| Cód. município                       |     11 |       8 |       1 |
| Tipo de escola                       |     12 |       6 |      89 |
| Grau estudo mãe                      |     13 |      12 |      21 |
| Dependência administrativa           |     14 |       9 |      71 |
| Grau estudo pai                      |     15 |      13 |      24 |
| Órgão regional                       |     16 |      14 |       2 |
| Qtde. micro-ondas                    |     17 |      51 |      47 |
| Ocupação mãe                         |     18 |      22 |      20 |
| Qtde. celulares                      |     19 |      29 |      32 |
| Empresa privada mantened.            |     20 |       5 |      50 |
| Pessoas na residência                |     21 |      38 |      26 |
| Qtde. máq. lavar roupa               |     22 |      40 |      56 |
| Qtde. motocicletas                   |     23 |      52 |      38 |
| Qtde. psicólogos                     |     24 |      17 |      35 |
| Vínculo Sec. Educação                |     25 |      10 |      64 |
| Região geográfica                    |     26 |      30 |      54 |
| Sala artes                           |     27 |      20 |      36 |
| Não sabe grau estudo mãe             |     28 |      42 |      88 |
| Qtde. máq. secar roupa               |     29 |      72 |      76 |
| Qtde. monitores                      |     30 |      28 |      19 |
| Qtde. carros                         |     31 |      34 |      41 |
| Qtde. TVs                            |     32 |      46 |      40 |
| Qtde. quartos                        |     33 |      70 |      37 |
| Não sabe grau estudo pai             |     34 |      57 |      84 |
| Qtde. banheiros                      |     35 |      23 |      52 |
| Exame seleção                        |     36 |      31 |      95 |
| Matrículas ens. médio                |     37 |      18 |       5 |
| Possui aspirador                     |     38 |      26 |      81 |
| Turmas ens. médio                    |     39 |      21 |      13 |
| Dias empregado(a) doméstico(a)       |     40 |      45 |      57 |
| Auditório                            |     41 |      43 |      30 |
| Qtde. bibliotecários                 |     42 |      27 |      11 |
| Qtde. desktop alunos                 |     43 |      33 |       4 |
| Educação profissional                |     44 |      36 |      34 |
| Nacionalidade                        |     45 |      59 |      72 |
| Qtde. projetores                     |     46 |      55 |      12 |
| Qtde. geladeiras                     |     47 |      80 |      62 |
| Sala música                          |     48 |      44 |      28 |
| Mantened. sem fins lucr.             |     49 |      25 |      54 |
| Estado civil                         |     50 |      75 |      74 |
| Tipo de instituição                  |     51 |      53 |      70 |
| Possui internet                      |     52 |      64 |      92 |
| Qtde. pedagogos                      |     53 |      61 |      15 |
| Sexo                                 |     54 |      78 |      59 |
| Docentes ens. médio                  |     55 |      37 |       8 |
| Qtde. tablets alunos                 |     56 |      67 |      17 |
| Matrículas tempo integral            |     57 |      39 |       7 |
| Lab. ciências                        |     58 |      54 |      31 |
| Lab. informática                     |     59 |      47 |      43 |
| Mantened. sindicato                  |     60 |      49 |      67 |
| Possui telefone fixo                 |     61 |      92 |      90 |
| Qtde. máq. lavar louça               |     62 |      69 |      75 |
| Qtde. lousas digitais                |     63 |      41 |      25 |
| Área verde                           |     64 |      66 |      33 |
| Parceria poder público               |     65 |      16 |      58 |
| Possui DVD                           |     66 |      73 |      86 |
| Qtde. notebooks alunos               |     67 |      63 |      10 |
| Matrículas normal/magistério         |     68 |      76 |      45 |
| Ocupação prédio escolar              |     69 |      74 |      98 |
| Vínculo Seg. Pública                 |     70 |      84 |      61 |
| Qtde. salas aula                     |     71 |      48 |       9 |
| Funciona outra escola                |     72 |      77 |      49 |
| Piscina                              |     73 |      32 |      51 |
| Aulas EAD                            |     74 |      56 |      48 |
| Turmas tempo integral                |     75 |      65 |      23 |
| Biblioteca                           |     76 |      81 |      44 |
| Qtde. televisores                    |     77 |      62 |      14 |
| Quadra esportes                      |     78 |      58 |      22 |
| Aulas semipresenciais                |     79 |      86 |      63 |
| Vínculo outro órgão                  |     80 |      79 |      96 |
| Mantened. sistema S                  |     81 |      50 |      53 |
| Internet alunos                      |     82 |      68 |      39 |
| Mantened. ONG                        |     83 |      60 |      85 |
| Internet ensino                      |     84 |      71 |      46 |
| Proposta pedagógica atualizada       |     85 |      94 |      94 |
| Sem material pedagógico              |     86 |      85 |      66 |
| Aulas presenciais                    |     87 |      87 |      69 |
| Água potável                         |     88 |      91 |      72 |
| Funciona prédio escolar              |     89 |      90 |      77 |
| Localização                          |     90 |      96 |     102 |
| Funciona prisional                   |     91 |      88 |      79 |
| Mantened. ONG/OSCIP                  |     92 |      93 |      91 |
| Funciona outros                      |     93 |      82 |      65 |
| Funciona socioeducativo              |     94 |      83 |      82 |
| Funciona galpão                      |     95 |     100 |      87 |
| Funciona prisional/socio             |     96 |      89 |      77 |
| Sem tratamento lixo                  |     97 |      97 |     100 |
| Sit. funcionamento escola            |     98 |     101 |      93 |
| Banheiro                             |     99 |      98 |      80 |
| Mantened. OSCIP                      |    100 |      99 |      99 |
| Sem esgoto                           |    101 |      95 |      83 |
| Localização diferenciada             |    102 |     104 |     104 |
| Sem energia                          |    103 |     103 |      97 |
| Sem água                             |    104 |     102 |     101 |
| Vínculo Sec. Saúde                   |    105 |     105 |     106 |
| Ocupação galpão                      |    106 |     106 |     105 |
