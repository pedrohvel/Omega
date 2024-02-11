import os
import pandas as pd
from pycaret.classification import *

def load_data(file_path):
    print(f"Carregando dados do arquivo: {file_path}")
    # Carregar o DataFrame com a coluna alvo
    return pd.read_parquet(file_path)

def train_and_save_models(df, target_column, models_to_select, save_path):
    print("Inicializando ambiente PyCaret...")
    # Inicializar o ambiente PyCaret
    exp1 = setup(df, target=target_column, session_id=123)

    print("Comparando modelos específicos para classificação binária...")
    # Comparar modelos específicos para classificação binária
    best_models = compare_models(include=models_to_select, sort='AUC')

    print(f"Iterando sobre {len(best_models)} melhores modelos e treinando/salvando cada um...")
    # Iterar sobre todos os melhores modelos e treinar/salvar cada um
    for model in best_models:
        print(f"Treinando o modelo {model}...")
        try:
            # Treinar o modelo
            trained_model = create_model(model)

            print(f"Avaliando o modelo {model}...")
            # Avaliar o modelo
            evaluate_model(trained_model)

            model_save_path = f"{save_path}/{model}"
            print(f"Salvando o modelo {model} treinado em {model_save_path}...")
            # Criar o diretório de salvamento se não existir
            os.makedirs(model_save_path, exist_ok=True)
            # Salvar o modelo treinado na pasta especificada
            save_model(trained_model, model_name=model, model_only=True, verbose=False, system=True, 
                       model_path=model_save_path)
            print(f"Modelo {model} treinado e salvo com sucesso!")

        except Exception as e:
            print(f"Erro ao treinar ou salvar o modelo {model}. Detalhes: {str(e)}")

if __name__ == "__main__":
    # Caminho para o arquivo parquet
    data_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE_Target.parquet"
    
    # Nome da coluna alvo
    target_column = "Target"
    
    # Modelos específicos para classificação binária (adicione/remova conforme necessário)
    specific_models = ['lr', 'dt', 'rf', 'et', 'lightgbm']
    
    # Caminho para a pasta onde os modelos serão salvos
    save_models_path = "C:/Users/Pedro/Documents/GitHub/Omega/Modelos_ML"
    
    print("Carregando os dados...")
    # Carregar os dados
    data = load_data(data_file_path)
    
    print("Amostrando os dados...")
    # Amostragem dos dados
    data_sample = data.sample(frac=0.1, random_state=42)  # Usando 10% dos dados como amostra
    
    print("Treinando e salvando modelos...")
    # Treinar e salvar modelos
    train_and_save_models(data_sample, target_column, specific_models, save_models_path)
