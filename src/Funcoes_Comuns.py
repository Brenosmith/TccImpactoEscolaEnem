# Este arquivo contém funções comuns utilizadas em diferentes partes do projeto.

import mlflow
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from typing import Union

# Função para calcular as métricas
def avaliar_modelo(y_true, y_pred, grupo):
    """
    Avalia o desempenho do modelo utilizando as métricas MAE, RMSE e R2.
    Parametros:
        y_true: array-like, valores reais
        y_pred: array-like, valores previstos pelo modelo
        grupo: str, nome do grupo para identificação na saída: 'teste', 'validação', 'treino'
    Retorna:
        None
    """
    mae = mean_absolute_error(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"MAE ({grupo}): {mae:.4f}")
    print(f"RMSE ({grupo}): {rmse:.4f}")
    print(f"R2 ({grupo}): {r2:.4f}")

# Função para registrar o modelo no MLflow
def registrar_modelo(experimento: str, 
                     parametros: dict, 
                     X_train: pd.DataFrame, 
                     y_train: Union[pd.DataFrame, pd.Series], 
                     y_test: Union[pd.DataFrame, pd.Series], 
                     y_pred: Union[pd.DataFrame, pd.Series], 
                     variavel_alvo: str, 
                     modelo: object, 
                     nome_modelo: str,
                     descricao_modelo: str):
    """
    Registra o modelo no MLflow com os parâmetros, métricas e assinatura.
    Parametros:
        experimento: str, nome do experimento no MLflow
        parametros: dict, parâmetros do modelo
        X_train: pd.DataFrame, dados de treino
        y_train: pd.DataFrame ou pd.Series, rótulos de treino
        y_test: pd.DataFrame ou pd.Series, dados de teste
        y_pred: pd.DataFrame ou pd.Series, previsões do modelo
        variavel_alvo: str, nome da variável alvo (usado apenas se y_train/y_test forem DataFrames)
        modelo: object, modelo treinado
        nome_modelo: str, nome do modelo a ser registrado
        descricao_modelo: str, descrição do modelo
    Retorna:
        None
    """

    try:
        # Iniciar o servidor de rastreamento do MLflow
        mlflow.set_tracking_uri(uri="http://127.0.0.1:9080")

        # Criar experimento no MLflow
        mlflow.set_experiment(experimento)

        # Iniciar o rastreamento do MLflow
        with mlflow.start_run() as run:

            # Registrar os parâmetros
            for param, value in parametros.items():
                mlflow.log_param(param, value)

            # Tratamento para aceitar DataFrame ou Series
            # Se for DataFrame, acessar pela coluna; se for Series, usar diretamente
            if isinstance(y_test, pd.DataFrame):
                y_test_values = y_test[variavel_alvo]
            else:
                y_test_values = y_test
            
            if isinstance(y_train, pd.DataFrame):
                y_train_values = y_train[variavel_alvo]
            else:
                y_train_values = y_train

            if isinstance(y_pred, pd.DataFrame):
                y_pred_values = y_pred[variavel_alvo]
            else:
                y_pred_values = y_pred

            # Registrar as métricas
            r2 = r2_score(y_test_values, y_pred_values)
            mae = mean_absolute_error(y_test_values, y_pred_values)
            rmse = root_mean_squared_error(y_test_values, y_pred_values)

            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("rmse", rmse)

            # Definir uma TAG para o modelo
            mlflow.set_tag("model_type", descricao_modelo)

            # Inferir assinatura do modelo
            signature = mlflow.models.infer_signature(X_train, y_train_values)

            # Detectar tipo de modelo e usar a função MLflow apropriada
            modelo_type = type(modelo).__module__
            modelo_class = type(modelo).__name__
            
            if 'tensorflow' in modelo_type or 'keras' in modelo_type or hasattr(modelo, 'predict') and hasattr(modelo, 'fit') and 'tensorflow' in str(type(modelo)):
                # Modelo TensorFlow/Keras
                mlflow.tensorflow.log_model(model=modelo,
                                            artifact_path=nome_modelo,
                                            signature=signature,
                                            registered_model_name=nome_modelo)
                
            elif hasattr(modelo, 'predict') and (hasattr(modelo, 'fit') or hasattr(modelo, 'get_params')):
                # Modelo sklearn-compatible (sklearn, lightgbm, xgboost, etc.)
                mlflow.sklearn.log_model(sk_model=modelo,
                                         artifact_path=nome_modelo,
                                         signature=signature,
                                         registered_model_name=nome_modelo)
                
            else:
                # Fallback para modelos genéricos
                mlflow.pyfunc.log_model(python_model=modelo,
                                        artifact_path=nome_modelo,
                                        signature=signature,
                                        registered_model_name=nome_modelo)

            print(f"Modelo registrado com sucesso no MLflow: {nome_modelo}")
            
    except Exception as e:
        # Cores ANSI para texto vermelho
        RED = '\033[91m'
        RESET = '\033[0m'
        print(f"{RED}Erro ao registrar o modelo no MLflow: {e}{RESET}")

    finally:
        # Finalizar o rastreamento do MLflow
        mlflow.end_run()
        print("Rastreamento do MLflow finalizado.")
