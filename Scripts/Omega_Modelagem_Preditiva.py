import h2o
from h2o.automl import H2OAutoML
import pandas as pd
from tqdm import tqdm

def sample_data(file_path, sample_fraction=0.1, random_state=42):
    print(f"Carregando dados do arquivo: {file_path}")
    # Carregue o DataFrame com a coluna alvo
    df = pd.read_parquet(file_path)
    
    print(f"Amostrando dados com {sample_fraction * 100}% da amostra...")
    # Amostragem direta no DataFrame
    sampled_data = df.sample(frac=sample_fraction, random_state=random_state)

    return sampled_data

def preprocess_data(df):
    print("Pré-processando dados...")
    # Adicione aqui seu pré-processamento, se necessário
    return df

def train_and_save_models(df, target_column, save_path, max_models=2):
    # Inicialize o H2O
    print("Iniciando o H2O...")
    h2o.init()

    print("Dividindo e pré-processando os dados...")
    # Pré-processamento dos dados
    data_processed = preprocess_data(df)

    # Converta o DataFrame para um H2OFrame
    h2o_data = h2o.H2OFrame(data_processed)

    # Defina as features e a variável alvo
    x = h2o_data.columns
    y = target_column
    x.remove(y)

    # Inicialize o H2O AutoML
    aml = H2OAutoML(max_models=max_models, max_runtime_secs=300, seed=42)

    print("Treinando os modelos...")

    # Use tqdm para indicador de progresso
    with tqdm(total=max_models, desc="Treinando Modelos") as pbar:
        # Treine o modelo
        aml.train(x=x, y=y, training_frame=h2o.H2OFrame(data_processed))
        pbar.update()

    # Veja os resultados
    lb = aml.leaderboard
    print(lb)

    # Salve os modelos
    for model_id in lb['model_id']:
        model = h2o.get_model(model_id)
        model_path = h2o.save_model(model=model, path=save_path, force=True)
        print(f"Modelo {model_id} salvo em: {model_path}")

    # Encerre o cluster H2O
    h2o.shutdown()
    print("Treinamento e salvamento de modelos concluídos.")

if __name__ == "__main__":
    # Caminho para o arquivo parquet
    data_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE_Target.parquet"
    
    # Nome da coluna alvo
    target_column = "Target"
    
    # Caminho para a pasta onde os modelos serão salvos
    save_models_path = "C:/Users/Pedro/Documents/GitHub/Omega/Modelos_ML"
    
    print("Amostrando dados e iniciando treinamento e salvamento de modelos...")
    # Amostrar dados, treinar e salvar modelos
    sampled_data = sample_data(data_file_path)
    train_and_save_models(sampled_data, target_column, save_models_path)
