"""
Dicionários e Listas Auxiliares para o projeto TCC
Contém mapeamentos de nomes descritivos, categorização de colunas e metadados das variáveis.
"""

# =============================================================================
# NOMES DESCRITIVOS DAS VARIÁVEIS
# =============================================================================

# Variáveis do ENEM - Dados Socioeconômicos e Demográficos
nomes_descritivos_enem = {
    # Dados Demográficos
    'CAT_FAIXA_ETARIA': 'Faixa etária',
    'CAT_SEXO': 'Sexo',
    'CAT_ESTADO_CIVIL': 'Estado civil',
    'CAT_COR_RACA': 'Cor/raça',
    'CAT_NACIONALIDADE': 'Nacionalidade',
    'CAT_LINGUA': 'Língua estrangeira',
    
    # Dados Escolares do ENEM
    'CAT_ESCOLA': 'Tipo de escola',
    'CAT_ENSINO': 'Tipo de instituição',
    'CAT_CO_MUNICIPIO_ESC': 'Cód. município',
    'CAT_CO_UF_ESC': 'UF escola',
    'CAT_DEPENDENCIA_ADM_ESC': 'Dependência administrativa',
    'CAT_LOCALIZACAO_ESC': 'Localização',
    'CAT_SIT_FUNC_ESC': 'Sit. funcionamento escola',
    
    # Notas do ENEM
    'NUM_NOTA_CN': 'Nota Ciências Natureza',
    'NUM_NOTA_CH': 'Nota Ciências Humanas',
    'NUM_NOTA_LC': 'Nota Linguagens',
    'NUM_NOTA_MT': 'Nota Matemática',
    'NUM_NOTA_REDACAO': 'Nota redação',
    
    # Questionário Socioeconômico - Educação dos Pais
    'NUM_Q001': 'Grau estudo pai',
    'BIN_Q001_DUMMY_H': 'Não sabe grau estudo pai',
    'NUM_Q002': 'Grau estudo mãe',
    'BIN_Q002_DUMMY_H': 'Não sabe grau estudo mãe',
    'CAT_Q003': 'Ocupação pai',
    'CAT_Q004': 'Ocupação mãe',
    
    # Questionário Socioeconômico - Composição Familiar e Renda
    'NUM_Q005': 'Pessoas na residência',
    'NUM_Q006': 'Renda familiar mensal',
    'NUM_Q007': 'Dias empregado(a) doméstico(a)',
    
    # Questionário Socioeconômico - Bens Domésticos
    'NUM_Q008': 'Qtde. banheiros',
    'NUM_Q009': 'Qtde. quartos',
    'NUM_Q010': 'Qtde. carros',
    'NUM_Q011': 'Qtde. motocicletas',
    'NUM_Q012': 'Qtde. geladeiras',
    'NUM_Q013': 'Qtde. freezers',
    'NUM_Q014': 'Qtde. máq. lavar roupa',
    'NUM_Q015': 'Qtde. máq. secar roupa',
    'NUM_Q016': 'Qtde. micro-ondas',
    'NUM_Q017': 'Qtde. máq. lavar louça',
    'BIN_Q018': 'Possui aspirador',
    
    # Questionário Socioeconômico - Tecnologia e Comunicação
    'NUM_Q019': 'Qtde. TVs',
    'BIN_Q020': 'Possui DVD',
    'BIN_Q021': 'Possui TV por assinatura',
    'NUM_Q022': 'Qtde. celulares',
    'BIN_Q023': 'Possui telefone fixo',
    'NUM_Q024': 'Qtde. computadores',
    'BIN_Q025': 'Possui internet'
}

# Variáveis do Censo Escolar - Infraestrutura e Organização das Escolas
nomes_descritivos_censo = {
    # Identificação Geográfica e Administrativa
    'CHA_CO_MUNICIPIO': 'Cód. município',
    'CAT_MODE_ORGAO_REGIONAL': 'Órgão regional',
    'CAT_MODE_REGIAO': 'Região geográfica',
    'CHA_DEPENDENCIA': 'Dependência administrativa',
    'CHA_LOCALIZACAO': 'Localização',
    'CAT_MODE_CATEGORIA_ESCOLA_PRIVADA': 'Categoria escola privada',
    'CAT_MODE_LOCALIZACAO_DIFERENCIADA': 'Localização diferenciada',
    
    # Infraestrutura Básica - Utilidades
    'NUM_PERC_AGUA_INEXISTENTE': 'Sem água',
    'NUM_PERC_AGUA_POTAVEL': 'Água potável',
    'NUM_PERC_ENERGIA_INEXISTENTE': 'Sem energia',
    'NUM_PERC_ESGOTO_INEXISTENTE': 'Sem esgoto',
    'CAT_MODE_TRATAMENTO_LIXO_INEXISTENTE': 'Sem tratamento lixo',
    
    # Infraestrutura Educacional - Espaços
    'NUM_PERC_AREA_VERDE': 'Área verde',
    'NUM_PERC_AUDITORIO': 'Auditório',
    'NUM_PERC_BANHEIRO': 'Banheiro',
    'NUM_PERC_BIBLIOTECA': 'Biblioteca',
    'NUM_PERC_LABORATORIO_CIENCIAS': 'Lab. ciências',
    'NUM_PERC_LABORATORIO_INFORMATICA': 'Lab. informática',
    'NUM_PERC_PISCINA': 'Piscina',
    'NUM_PERC_QUADRA_ESPORTES': 'Quadra esportes',
    'NUM_PERC_SALA_ATELIE_ARTES': 'Sala artes',
    'NUM_PERC_SALA_MUSICA_CORAL': 'Sala música',
    
    # Tecnologia e Conectividade
    'NUM_PERC_INTERNET_ALUNOS': 'Internet alunos',
    'NUM_PERC_INTERNET_APRENDIZAGEM': 'Internet ensino',
    'NUM_MEAN_COMP_PORTATIL_ALUNO': 'Qtde. notebooks alunos',
    'NUM_MEAN_DESKTOP_ALUNO': 'Qtde. desktop alunos',
    'NUM_MEAN_EQUIP_LOUSA_DIGITAL': 'Qtde. lousas digitais',
    'NUM_MEAN_EQUIP_MULTIMIDIA': 'Qtde. projetores',
    'NUM_MEAN_EQUIP_TV': 'Qtde. televisores',
    'NUM_MEAN_TABLET_ALUNO': 'Qtde. tablets alunos',
    
    # Localização de Funcionamento
    'NUM_PERC_LOCAL_FUNC_GALPAO': 'Funciona galpão',
    'NUM_PERC_LOCAL_FUNC_OUTROS': 'Funciona outros',
    'NUM_PERC_LOCAL_FUNC_PREDIO_ESCOLAR': 'Funciona prédio escolar',
    'NUM_PERC_LOCAL_FUNC_PRISIONAL_SOCIO': 'Funciona prisional/socio',
    'NUM_PERC_LOCAL_FUNC_SALAS_OUTRA_ESC': 'Funciona outra escola',
    'NUM_PERC_LOCAL_FUNC_SOCIOEDUCATIVO': 'Funciona socioeducativo',
    'NUM_PERC_LOCAL_FUNC_UNID_PRISIONAL': 'Funciona prisional',
    'CAT_MODE_OCUPACAO_GALPAO': 'Ocupação galpão',
    'CAT_MODE_OCUPACAO_PREDIO_ESCOLAR': 'Ocupação prédio escolar',
    
    # Mantenedoras (Escolas Privadas)
    'NUM_PERC_MANT_ESCOLA_PRIV_ONG_OSCIP': 'Mantened. ONG/OSCIP',
    'NUM_PERC_MANT_ESCOLA_PRIVADA_EMP': 'Empresa privada mantened.',
    'NUM_PERC_MANT_ESCOLA_PRIVADA_ONG': 'Mantened. ONG',
    'NUM_PERC_MANT_ESCOLA_PRIVADA_OSCIP': 'Mantened. OSCIP',
    'NUM_PERC_MANT_ESCOLA_PRIVADA_S_FINS': 'Mantened. sem fins lucr.',
    'NUM_PERC_MANT_ESCOLA_PRIVADA_SIND': 'Mantened. sindicato',
    'NUM_PERC_MANT_ESCOLA_PRIVADA_SIST_S': 'Mantened. sistema S',
    
    # Organização Pedagógica
    'CAT_MODE_EXAME_SELECAO': 'Exame seleção',
    'NUM_PERC_MATERIAL_PED_NENHUM': 'Sem material pedagógico',
    'NUM_PERC_MEDIACAO_EAD': 'Aulas EAD',
    'NUM_PERC_MEDIACAO_PRESENCIAL': 'Aulas presenciais',
    'NUM_PERC_MEDIACAO_SEMIPRESENCIAL': 'Aulas semipresenciais',
    'NUM_PERC_PROF_TEC': 'Educação profissional',
    'CAT_MODE_PROPOSTA_PEDAGOGICA': 'Proposta pedagógica atualizada',
    
    # Vínculos Institucionais
    'NUM_PERC_PODER_PUBLICO_PARCERIA': 'Parceria poder público',
    'NUM_PERC_VINCULO_OUTRO_ORGAO': 'Vínculo outro órgão',
    'NUM_PERC_VINCULO_SECRETARIA_EDUCACAO': 'Vínculo Sec. Educação',
    'NUM_PERC_VINCULO_SECRETARIA_SAUDE': 'Vínculo Sec. Saúde',
    'NUM_PERC_VINCULO_SEGURANCA_PUBLICA': 'Vínculo Seg. Pública',
    
    # Recursos Humanos
    'NUM_MEAN_DOC_MED': 'Docentes ens. médio',
    'NUM_MEAN_PROF_BIBLIOTECARIO': 'Qtde. bibliotecários',
    'NUM_MEAN_PROF_MONITORES': 'Qtde. monitores',
    'NUM_MEAN_PROF_PSICOLOGO': 'Qtde. psicólogos',
    'NUM_MEAN_PROF_PEDAGOGIA': 'Qtde. pedagogos',
    
    # Matrículas e Turmas
    'NUM_MEAN_MAT_MED': 'Matrículas ens. médio',
    'NUM_MEAN_MAT_MED_INT': 'Matrículas tempo integral',
    'NUM_MEAN_MAT_MED_NM': 'Matrículas normal/magistério',
    'NUM_MEAN_SALAS_UTILIZADAS': 'Qtde. salas aula',
    'NUM_MEAN_TUR_MED': 'Turmas ens. médio',
    'NUM_MEAN_TUR_MED_INT': 'Turmas tempo integral',
}

# Dicionário Completo - Combinação de todas as variáveis
nomes_descritivos = {**nomes_descritivos_enem, **nomes_descritivos_censo}

# =============================================================================
# CATEGORIZAÇÃO DAS VARIÁVEIS POR TIPO E ORIGEM
# =============================================================================

# Variáveis Alvo (Notas do ENEM)
colunas_alvo = ['NUM_NOTA_CH', 'NUM_NOTA_CN', 'NUM_NOTA_LC', 'NUM_NOTA_MT', 'NUM_NOTA_REDACAO']

# Variáveis Socioeconômicas (provenientes do questionário do ENEM)
colunas_socioeconomicas = [
    # Variáveis demográficas básicas
    "CAT_COR_RACA", "CAT_ESTADO_CIVIL", "CAT_FAIXA_ETARIA", "CAT_LINGUA", 
    "CAT_NACIONALIDADE", "CAT_SEXO",
    
    # Informações sobre os pais
    "BIN_Q001_DUMMY_H", "BIN_Q002_DUMMY_H", "NUM_Q001", "NUM_Q002", 
    "CAT_Q003", "CAT_Q004",
    
    # Composição familiar e trabalho doméstico
    "NUM_Q005", "NUM_Q006", "NUM_Q007",
    
    # Bens domésticos - estrutura da casa
    "NUM_Q008", "NUM_Q009",
    
    # Bens domésticos - veículos
    "NUM_Q010", "NUM_Q011",
    
    # Bens domésticos - eletrodomésticos
    "NUM_Q012", "NUM_Q013", "NUM_Q014", "NUM_Q015", "NUM_Q016", "NUM_Q017", 
    "BIN_Q018",
    
    # Bens domésticos - tecnologia e comunicação
    "NUM_Q019", "BIN_Q020", "BIN_Q021", "NUM_Q022", "BIN_Q023", "NUM_Q024", 
    "BIN_Q025"
]

# Variáveis Escolares (provenientes do Censo Escolar e dados de escola do ENEM)
colunas_escolares = [
    # Identificação geográfica da escola (comum ao ENEM e Censo)
    "CAT_CO_MUNICIPIO_ESC", "CAT_CO_UF_ESC", "CAT_DEPENDENCIA_ADM_ESC", 
    "CAT_LOCALIZACAO_ESC",
    
    # Características da escola (ENEM)
    "CAT_ENSINO", "CAT_ESCOLA", "CAT_SIT_FUNC_ESC",
    
    # Administração e organização (Censo Escolar)
    "CAT_MODE_CATEGORIA_ESCOLA_PRIVADA", "CAT_MODE_EXAME_SELECAO", 
    "CAT_MODE_LOCALIZACAO_DIFERENCIADA", "CAT_MODE_OCUPACAO_GALPAO",
    "CAT_MODE_OCUPACAO_PREDIO_ESCOLAR", "CAT_MODE_ORGAO_REGIONAL", 
    "CAT_MODE_PROPOSTA_PEDAGOGICA", "CAT_MODE_REGIAO",
    "CAT_MODE_TRATAMENTO_LIXO_INEXISTENTE",
    
    # Recursos tecnológicos e equipamentos
    "NUM_MEAN_COMP_PORTATIL_ALUNO", "NUM_MEAN_DESKTOP_ALUNO", 
    "NUM_MEAN_EQUIP_LOUSA_DIGITAL", "NUM_MEAN_EQUIP_MULTIMIDIA", 
    "NUM_MEAN_EQUIP_TV", "NUM_MEAN_TABLET_ALUNO",
    
    # Recursos humanos
    "NUM_MEAN_DOC_MED", "NUM_MEAN_PROF_BIBLIOTECARIO", "NUM_MEAN_PROF_MONITORES", 
    "NUM_MEAN_PROF_PEDAGOGIA", "NUM_MEAN_PROF_PSICOLOGO",
    
    # Matrículas e estrutura educacional
    "NUM_MEAN_MAT_MED", "NUM_MEAN_MAT_MED_INT", "NUM_MEAN_MAT_MED_NM", 
    "NUM_MEAN_SALAS_UTILIZADAS", "NUM_MEAN_TUR_MED", "NUM_MEAN_TUR_MED_INT",
    
    # Infraestrutura básica
    "NUM_PERC_AGUA_INEXISTENTE", "NUM_PERC_AGUA_POTAVEL", "NUM_PERC_AREA_VERDE",
    "NUM_PERC_AUDITORIO", "NUM_PERC_BANHEIRO", "NUM_PERC_BIBLIOTECA", 
    "NUM_PERC_ENERGIA_INEXISTENTE", "NUM_PERC_ESGOTO_INEXISTENTE",
    
    # Conectividade e tecnologia
    "NUM_PERC_INTERNET_ALUNOS", "NUM_PERC_INTERNET_APRENDIZAGEM",
    
    # Laboratórios e espaços especiais
    "NUM_PERC_LABORATORIO_CIENCIAS", "NUM_PERC_LABORATORIO_INFORMATICA",
    "NUM_PERC_PISCINA", "NUM_PERC_QUADRA_ESPORTES", "NUM_PERC_SALA_ATELIE_ARTES",
    "NUM_PERC_SALA_MUSICA_CORAL",
    
    # Locais de funcionamento
    "NUM_PERC_LOCAL_FUNC_GALPAO", "NUM_PERC_LOCAL_FUNC_OUTROS", 
    "NUM_PERC_LOCAL_FUNC_PREDIO_ESCOLAR", "NUM_PERC_LOCAL_FUNC_PRISIONAL_SOCIO", 
    "NUM_PERC_LOCAL_FUNC_SALAS_OUTRA_ESC", "NUM_PERC_LOCAL_FUNC_SOCIOEDUCATIVO", 
    "NUM_PERC_LOCAL_FUNC_UNID_PRISIONAL",
    
    # Mantenedoras (escolas privadas)
    "NUM_PERC_MANT_ESCOLA_PRIVADA_EMP", "NUM_PERC_MANT_ESCOLA_PRIVADA_ONG", 
    "NUM_PERC_MANT_ESCOLA_PRIVADA_OSCIP", "NUM_PERC_MANT_ESCOLA_PRIVADA_SIND",
    "NUM_PERC_MANT_ESCOLA_PRIVADA_SIST_S", "NUM_PERC_MANT_ESCOLA_PRIVADA_S_FINS", 
    "NUM_PERC_MANT_ESCOLA_PRIV_ONG_OSCIP",
    
    # Organização pedagógica
    "NUM_PERC_MATERIAL_PED_NENHUM", "NUM_PERC_MEDIACAO_EAD", 
    "NUM_PERC_MEDIACAO_PRESENCIAL", "NUM_PERC_MEDIACAO_SEMIPRESENCIAL",
    "NUM_PERC_PROF_TEC",
    
    # Parcerias e vínculos
    "NUM_PERC_PODER_PUBLICO_PARCERIA", "NUM_PERC_VINCULO_OUTRO_ORGAO", 
    "NUM_PERC_VINCULO_SECRETARIA_EDUCACAO", "NUM_PERC_VINCULO_SECRETARIA_SAUDE",
    "NUM_PERC_VINCULO_SEGURANCA_PUBLICA"
]

# =============================================================================
# CATEGORIZAÇÃO DAS VARIÁVEIS POR BASE DE DADOS
# =============================================================================

# Variáveis exclusivas dos Microdados do ENEM
colunas_microdados_enem = [
    # Dados demográficos e socioeconômicos do questionário
    "BIN_Q001_DUMMY_H", "BIN_Q002_DUMMY_H", "BIN_Q018", "BIN_Q020", "BIN_Q021", 
    "BIN_Q023", "BIN_Q025", "CAT_COR_RACA", "CAT_ENSINO", "CAT_ESCOLA", 
    "CAT_ESTADO_CIVIL", "CAT_FAIXA_ETARIA", "CAT_LINGUA", "CAT_NACIONALIDADE", 
    "CAT_Q003", "CAT_Q004", "CAT_SEXO", "CAT_SIT_FUNC_ESC",
    "NUM_Q001", "NUM_Q002", "NUM_Q005", "NUM_Q006", "NUM_Q007", "NUM_Q008", 
    "NUM_Q009", "NUM_Q010", "NUM_Q011", "NUM_Q012", "NUM_Q013", "NUM_Q014", 
    "NUM_Q015", "NUM_Q016", "NUM_Q017", "NUM_Q019", "NUM_Q022", "NUM_Q024"
]

# Variáveis exclusivas dos Microdados do Censo Escolar
colunas_microdados_censo_escolar = [
    # Administração e categorização
    "CAT_MODE_CATEGORIA_ESCOLA_PRIVADA", "CAT_MODE_EXAME_SELECAO", 
    "CAT_MODE_LOCALIZACAO_DIFERENCIADA", "CAT_MODE_OCUPACAO_GALPAO",
    "CAT_MODE_OCUPACAO_PREDIO_ESCOLAR", "CAT_MODE_ORGAO_REGIONAL", 
    "CAT_MODE_PROPOSTA_PEDAGOGICA", "CAT_MODE_REGIAO",
    "CAT_MODE_TRATAMENTO_LIXO_INEXISTENTE",
    
    # Recursos tecnológicos (médias por escola)
    "NUM_MEAN_COMP_PORTATIL_ALUNO", "NUM_MEAN_DESKTOP_ALUNO", "NUM_MEAN_DOC_MED", 
    "NUM_MEAN_EQUIP_LOUSA_DIGITAL", "NUM_MEAN_EQUIP_MULTIMIDIA", "NUM_MEAN_EQUIP_TV", 
    "NUM_MEAN_MAT_MED", "NUM_MEAN_MAT_MED_INT", "NUM_MEAN_MAT_MED_NM", 
    "NUM_MEAN_PROF_BIBLIOTECARIO", "NUM_MEAN_PROF_MONITORES", "NUM_MEAN_PROF_PEDAGOGIA",
    "NUM_MEAN_PROF_PSICOLOGO", "NUM_MEAN_SALAS_UTILIZADAS", "NUM_MEAN_TABLET_ALUNO", 
    "NUM_MEAN_TUR_MED", "NUM_MEAN_TUR_MED_INT",
    
    # Infraestrutura (percentuais por município)
    "NUM_PERC_AGUA_INEXISTENTE", "NUM_PERC_AGUA_POTAVEL", "NUM_PERC_AREA_VERDE",
    "NUM_PERC_AUDITORIO", "NUM_PERC_BANHEIRO", "NUM_PERC_BIBLIOTECA", 
    "NUM_PERC_ENERGIA_INEXISTENTE", "NUM_PERC_ESGOTO_INEXISTENTE", 
    "NUM_PERC_INTERNET_ALUNOS", "NUM_PERC_INTERNET_APRENDIZAGEM", 
    "NUM_PERC_LABORATORIO_CIENCIAS", "NUM_PERC_LABORATORIO_INFORMATICA",
    
    # Locais de funcionamento
    "NUM_PERC_LOCAL_FUNC_GALPAO", "NUM_PERC_LOCAL_FUNC_OUTROS", 
    "NUM_PERC_LOCAL_FUNC_PREDIO_ESCOLAR", "NUM_PERC_LOCAL_FUNC_PRISIONAL_SOCIO", 
    "NUM_PERC_LOCAL_FUNC_SALAS_OUTRA_ESC", "NUM_PERC_LOCAL_FUNC_SOCIOEDUCATIVO", 
    "NUM_PERC_LOCAL_FUNC_UNID_PRISIONAL",
    
    # Mantenedoras
    "NUM_PERC_MANT_ESCOLA_PRIVADA_EMP", "NUM_PERC_MANT_ESCOLA_PRIVADA_ONG", 
    "NUM_PERC_MANT_ESCOLA_PRIVADA_OSCIP", "NUM_PERC_MANT_ESCOLA_PRIVADA_SIND",
    "NUM_PERC_MANT_ESCOLA_PRIVADA_SIST_S", "NUM_PERC_MANT_ESCOLA_PRIVADA_S_FINS", 
    "NUM_PERC_MANT_ESCOLA_PRIV_ONG_OSCIP",
    
    # Organização pedagógica e recursos
    "NUM_PERC_MATERIAL_PED_NENHUM", "NUM_PERC_MEDIACAO_EAD", 
    "NUM_PERC_MEDIACAO_PRESENCIAL", "NUM_PERC_MEDIACAO_SEMIPRESENCIAL", 
    "NUM_PERC_PISCINA", "NUM_PERC_PODER_PUBLICO_PARCERIA", "NUM_PERC_PROF_TEC", 
    "NUM_PERC_QUADRA_ESPORTES", "NUM_PERC_SALA_ATELIE_ARTES", 
    "NUM_PERC_SALA_MUSICA_CORAL",
    
    # Vínculos institucionais
    "NUM_PERC_VINCULO_OUTRO_ORGAO", "NUM_PERC_VINCULO_SECRETARIA_EDUCACAO", 
    "NUM_PERC_VINCULO_SECRETARIA_SAUDE", "NUM_PERC_VINCULO_SEGURANCA_PUBLICA"
]

# Variáveis presentes em ambas as bases (para fazer o join)
colunas_ambas = [
    "CAT_CO_MUNICIPIO_ESC",      # Código do município da escola
    "CAT_CO_UF_ESC",             # UF da escola
    "CAT_DEPENDENCIA_ADM_ESC",   # Dependência administrativa
    "CAT_LOCALIZACAO_ESC",       # Localização (urbana/rural)
]

# =============================================================================
# METADADOS DAS VARIÁVEIS
# =============================================================================

# Mapeamento de cada variável para seu tipo (Socioeconômico ou Escolar)
origens_tipo = {}

for col in colunas_socioeconomicas:
    origens_tipo[col] = 'SOCIOECONOMICO'

for col in colunas_escolares:
    origens_tipo[col] = 'ESCOLARES'

# Mapeamento de cada variável para sua base de origem
origens_base = {}

for col in colunas_microdados_enem:
    origens_base[col] = 'ENEM'

for col in colunas_microdados_censo_escolar:
    origens_base[col] = 'CENSO ESCOLAR'

for col in colunas_ambas:
    origens_base[col] = 'AMBAS'

# =============================================================================
# FUNÇÕES AUXILIARES PARA FACILITAR O USO
# =============================================================================

def get_nome_descritivo(variavel):
    """
    Retorna o nome descritivo de uma variável.
    
    Args:
        variavel (str): Nome da variável
        
    Returns:
        str: Nome descritivo da variável ou a própria variável se não encontrada
    """
    return nomes_descritivos.get(variavel, variavel)

def get_tipo_variavel(variavel):
    """
    Retorna o tipo da variável (SOCIOECONOMICO ou ESCOLARES).
    
    Args:
        variavel (str): Nome da variável
        
    Returns:
        str: Tipo da variável ou None se não encontrada
    """
    return origens_tipo.get(variavel)

def get_origem_variavel(variavel):
    """
    Retorna a base de origem da variável (ENEM, CENSO ESCOLAR ou AMBAS).
    
    Args:
        variavel (str): Nome da variável
        
    Returns:
        str: Origem da variável ou None se não encontrada
    """
    return origens_base.get(variavel)

def listar_variaveis_por_tipo(tipo):
    """
    Lista todas as variáveis de um determinado tipo.
    
    Args:
        tipo (str): Tipo desejado ('SOCIOECONOMICO' ou 'ESCOLARES')
        
    Returns:
        list: Lista de variáveis do tipo especificado
    """
    if tipo.upper() == 'SOCIOECONOMICO':
        return colunas_socioeconomicas.copy()
    elif tipo.upper() == 'ESCOLARES':
        return colunas_escolares.copy()
    else:
        return []

def listar_variaveis_por_origem(origem):
    """
    Lista todas as variáveis de uma determinada origem.
    
    Args:
        origem (str): Origem desejada ('ENEM', 'CENSO ESCOLAR' ou 'AMBAS')
        
    Returns:
        list: Lista de variáveis da origem especificada
    """
    if origem.upper() == 'ENEM':
        return colunas_microdados_enem.copy()
    elif origem.upper() == 'CENSO ESCOLAR':
        return colunas_microdados_censo_escolar.copy()
    elif origem.upper() == 'AMBAS':
        return colunas_ambas.copy()
    else:
        return []