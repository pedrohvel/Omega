import os
import pandas as pd
from pycaret.classification import *

def load_data(file_path):
    print(f"Carregando dados do arquivo: {file_path}")
    # Carregar o DataFrame com a coluna alvo
    return pd.read_parquet(file_path)

def train_and_save_best_model(df, target_column, save_path):
    print("Inicializando ambiente PyCaret...")
    # Inicializar o ambiente PyCaret
    exp1 = setup(df, target=target_column, session_id=123)

    print("Comparando modelos para classificação binária...")
    # Comparar modelos para classificação binária
    best_model = compare_models(sort='AUC', n_select=1)

    print(f"Treinando o melhor modelo: {best_model}...")
    try:
        # Treinar o melhor modelo
        trained_model = create_model(best_model)

        print("Avaliando o melhor modelo...")
        # Avaliar o modelo
        evaluate_model(trained_model)

        model_save_path = f"{save_path}/{best_model}"
        print(f"Salvando o melhor modelo treinado em {model_save_path}...")
        # Criar o diretório de salvamento se não existir
        os.makedirs(model_save_path, exist_ok=True)
        # Salvar o modelo treinado na pasta especificada
        save_model(trained_model, model_name=best_model, model_only=True, verbose=False, system=True, 
                   model_path=model_save_path)
        print(f"Melhor modelo treinado e salvo com sucesso!")

    except Exception as e:
        print(f"Erro ao treinar ou salvar o melhor modelo. Detalhes: {str(e)}")

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
