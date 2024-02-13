import h2o
from h2o.automl import H2OAutoML
import pandas as pd

def load_data(file_path):
    print(f"Carregando dados do arquivo: {file_path}")
    # Carregar o DataFrame com a coluna alvo
    return pd.read_parquet(file_path)

def preprocess_data(df):
    # Adicione aqui seu pré-processamento, se necessário
    return df

def train_and_save_best_model(df, target_column, save_path):
    print("Amostrando os dados...")
    # Amostragem dos dados
    data_sample = df.sample(frac=0.1, random_state=42)  # Usando 10% dos dados como amostra

    print("Dividindo e pré-processando os dados...")
    # Divida e pré-processe os dados (se necessário)
    h2o.init()
    h2o_data = h2o.H2OFrame(data_sample)
    
    # Defina as features e a variável alvo
    x = h2o_data.columns
    y = target_column
    x.remove(y)

    # Inicialize o H2O AutoML
    aml = H2OAutoML(max_runtime_secs=300, seed=42)

    # Treine o modelo
    aml.train(x=x, y=y, training_frame=h2o_data)

    # Veja os resultados
    lb = aml.leaderboard
    print(lb)

    # Salve o modelo líder
    leader = aml.leader
    model_path = h2o.save_model(model=leader, path=save_path, force=True)
    print(f"Melhor modelo salvo em: {model_path}")

    # Encerre o cluster H2O
    h2o.shutdown()

if __name__ == "__main__":
    # Caminho para o arquivo parquet
    data_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE_Target.parquet"
    
    # Nome da coluna alvo
    target_column = "Target"
    
    # Caminho para a pasta onde o melhor modelo será salvo
    save_models_path = "C:/Users/Pedro/Documents/GitHub/Omega/Modelos_ML"
    
    print("Carregando os dados...")
    # Carregar os dados
    data = load_data(data_file_path)
    
    print("Treinando e salvando o melhor modelo...")
    # Treinar e salvar o melhor modelo
    train_and_save_best_model(data, target_column, save_models_path)
