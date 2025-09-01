"""
Módulo de Funções SHAP - Análise de Explicabilidade de Modelos

Este módulo contém funções consolidadas para análise SHAP (SHapley Additive exPlanations),
uma técnica avançada de explicabilidade para modelos de machine learning.

Funcionalidades principais:
- Calcular valores SHAP para diferentes tipos de modelos
- Extrair e padronizar arrays SHAP
- Analisar importância por grupos de features
- Visualizar resultados com nomes descritivos
"""

import pandas as pd
import numpy as np
import shap
from Dicionarios_Listas_Auxiliares import get_nome_descritivo

# Funções consolidadas para análise SHAP
def calculate_shap_values(model, X_sample):
    """
    Calcular valores SHAP para um modelo de machine learning.
    
    Args:
        model: Modelo de ML treinado (sklearn, xgboost, lightgbm, etc.)
        X_sample: DataFrame ou array com amostras para calcular SHAP
    
    Returns:
        shap_values: Objeto SHAP com valores de importância calculados
    
    Exemplo:
        shap_values = calculate_shap_values(meu_modelo, X_teste)
    """
    explainer = shap.Explainer(model)
    shap_values = explainer(X_sample)
    return shap_values

def extract_shap_array(shap_values):
    """
    Extrair array SHAP de forma consistente, tratando diferentes formatos.
    
    Args:
        shap_values: Objeto SHAP (pode ter estruturas diferentes dependendo do modelo)
    
    Returns:
        shap_array: Array numpy padronizado com valores SHAP
    
    Nota:
        - Trata arrays 3D (multi-target) pegando apenas o primeiro target
        - Garante formato consistente para análises posteriores
    """
    if hasattr(shap_values, 'values'):
        shap_array = shap_values.values
        if shap_array.ndim == 3:  # (amostras, targets, features)
            shap_array = shap_array[:, 0, :]  # Usar primeiro target
    else:
        shap_array = shap_values
    return shap_array

def analyze_shap_by_group(shap_values, feature_names, group_function, group_name):
    """
    Analisar importância SHAP agrupada por critério específico.
    
    Args:
        shap_values: Valores SHAP calculados
        feature_names: Lista com nomes das features
        group_function: Função ou dicionário que define como agrupar features
        group_name: Nome da coluna de agrupamento no resultado
    
    Returns:
        DataFrame: Importância SHAP por grupo (absoluta e percentual), 
                  ordenado por importância decrescente
    
    Exemplo:
        # Usando função
        def agrupar_por_tipo(feature):
            if 'escola' in feature: return 'Escolar'
            elif 'socio' in feature: return 'Socioeconômico'
            else: return 'Outros'
        
        resultado = analyze_shap_by_group(shap_values, features, 
                                        agrupar_por_tipo, 'Tipo')
        
        # Usando dicionário
        mapeamento = {'var1': 'Grupo A', 'var2': 'Grupo B'}
        resultado = analyze_shap_by_group(shap_values, features, 
                                        mapeamento, 'Grupo')
    """
    shap_array = extract_shap_array(shap_values)
    mean_abs_shap = np.abs(shap_array).mean(axis=0)
    
    df_shap = pd.DataFrame({
        'Feature': feature_names,
        'SHAP_Importance': mean_abs_shap
    })
    
    # Verificar se group_function é um dicionário ou uma função
    if isinstance(group_function, dict):
        df_shap[group_name] = df_shap['Feature'].map(group_function)
    else:
        df_shap[group_name] = df_shap['Feature'].apply(group_function)
    
    # Agrupar e calcular porcentagem
    df_grouped = df_shap.groupby(group_name)['SHAP_Importance'].sum().reset_index()
    df_grouped['SHAP_Importance (%)'] = 100 * df_grouped['SHAP_Importance'] / df_grouped['SHAP_Importance'].sum()
    
    return df_grouped.sort_values('SHAP_Importance (%)', ascending=False)

def plot_shap_values(shap_values, feature_names, max_display=20):
    """
    Plotar valores SHAP com nomes descritivos das features.
    
    Args:
        shap_values: Valores SHAP para visualização
        feature_names: Lista com nomes originais das features
        max_display: Número máximo de features a exibir (padrão: 20)
    
    Funcionalidade:
        - Converte nomes técnicos para nomes descritivos usando get_nome_descritivo()
        - Gera summary plot do SHAP para interpretação do modelo
    
    Exemplo:
        plot_shap_values(shap_values, feature_names, max_display=15)
    """
    feature_names_desc = [get_nome_descritivo(f) for f in feature_names]
    shap.summary_plot(shap_values, feature_names=feature_names_desc, max_display=max_display)