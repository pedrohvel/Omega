import h2o
from h2o.automl import H2OAutoML
import pandas as pd
from tqdm import tqdm

def load_and_sample_data(file_path, sample_fraction=0.2, random_state=42):
    print(f"Amostrando dados do arquivo: {file_path}")
    # Carregar o DataFrame com a coluna alvo
    df = pd.read_parquet(file_path)
    # Amostrar os dados
    sampled_data = df.sample(frac=sample_fraction, replace=False, random_state=random_state)
    return sampled_data

def preprocess_data(df):
    # Adicione aqui seu pré-processamento, se necessário
    return df

def train_and_save_models(df, target_column, save_path):
    # Inicialize o H2O
    h2o.init()

    print("Dividindo e pré-processando os dados...")
    # Pré-processamento dos dados
    data_processed = preprocess_data(df)

    # Defina as features e a variável alvo
    x = list(data_processed.columns)
    y = target_column

    # Converta DataFrame Pandas para H2OFrame
    h2o_data = h2o.H2OFrame(data_processed)

    # Treine o modelo
    model = H2OAutoML(max_runtime_secs=300, seed=42)
    model.train(x=x, y=y, training_frame=h2o_data)

    # Salve o modelo
    model_id = model.leader.model_id
    model_path = h2o.save_model(model=model.leader, path=save_path, force=True)
    print(f"Modelo {model_id} salvo em: {model_path}")

    # Encerre o cluster H2O
    h2o.shutdown()

if __name__ == "__main__":
    # Caminho para o arquivo parquet
    data_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE_Target.parquet"
    
    # Nome da coluna alvo
    target_column = "Target"
    
    # Caminho para a pasta onde os modelos serão salvos
    save_models_path = "C:/Users/Pedro/Documents/GitHub/Omega/Modelos_ML"
    
    print("Treinando e salvando modelos...")
    # Treinar e salvar modelos
    train_and_save_models(load_and_sample_data(data_file_path), target_column, save_models_path)
