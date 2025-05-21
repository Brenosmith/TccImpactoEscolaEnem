# Este arquivo contém funções comuns utilizadas em diferentes partes do projeto.

from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error

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
    print(f"MAE ({grupo}): {mae:.2f}")
    print(f"RMSE ({grupo}): {rmse:.2f}")
    print(f"R2 ({grupo}): {r2:.2f}")


import mlflow
import pandas as pd

# Função para registrar o modelo no MLflow
def registrar_modelo(experimento: str, 
                     parametros: dict, 
                     X_train: pd.DataFrame, 
                     y_train: pd.DataFrame, 
                     y_test: pd.DataFrame, 
                     y_pred: pd.DataFrame, 
                     varivel_alvo: str, 
                     modelo: object, 
                     nome_modelo: str,
                     descricao_modelo: str):
    """
    Registra o modelo no MLflow com os parâmetros, métricas e assinatura.
    Parametros:
        experimento: str, nome do experimento no MLflow
        parametros: dict, parâmetros do modelo
        X_train: pd.DataFrame, dados de treino
        y_train: pd.DataFrame, rótulos de treino
        y_test: pd.DataFrame, dados de teste
        y_pred: pd.DataFrame, previsões do modelo
        varivel_alvo: str, nome da variável alvo
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

            # Registrar as métricas
            r2 = r2_score(y_test[varivel_alvo], y_pred)
            mae = mean_absolute_error(y_test[varivel_alvo], y_pred)
            rmse = root_mean_squared_error(y_test[varivel_alvo], y_pred)

            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("rmse", rmse)

            # Definir uma TAG para o modelo
            mlflow.set_tag("model_type", descricao_modelo)

            # Inferir assinatura do modelo
            signature = mlflow.models.infer_signature(X_train, y_train[varivel_alvo])

            # Registrar modelo
            mlflow.sklearn.log_model(sk_model=modelo,
                                    artifact_path=nome_modelo,
                                    signature=signature,
                                    registered_model_name=nome_modelo)
            
            # Finalizar o rastreamento do MLflow
            mlflow.end_run()

            print(f"Modelo registrado com sucesso no MLflow: {nome_modelo}")
            
    except Exception as e:
        print(f"Erro ao registrar o modelo no MLflow: {e}")

    finally:
        # Finalizar o rastreamento do MLflow
        mlflow.end_run()
        print("Rastreamento do MLflow finalizado.")
