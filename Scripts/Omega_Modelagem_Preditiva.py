import pandas as pd
from pycaret.classification import *

def load_data(file_path):
    # Carregar o DataFrame com a coluna alvo
    return pd.read_feather(file_path)

def train_and_save_models(df, target_column, models_to_select, save_path):
    # Inicializar o ambiente PyCaret
    exp1 = setup(df, target=target_column)

    # Comparar todos os modelos disponíveis
    best_models = compare_models(n_select=models_to_select)

    # Iterar sobre todos os melhores modelos e treinar/salvar cada um
    for model in best_models:
        # Treinar o modelo
        trained_model = create_model(model)
        
        # Avaliar o modelo
        evaluate_model(trained_model)
        
        # Salvar o modelo treinado na pasta especificada
        save_model(trained_model, model_name=model, model_only=True, verbose=False, system=True, 
                   model_path=f"{save_path}/{model}")

if __name__ == "__main__":
    # Caminho para o arquivo feather
    data_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE_Target.feather"
    
    # Nome da coluna alvo
    target_column = "Target"
    
    # Número de modelos para selecionar
    num_models_to_select = 10
    
    # Caminho para a pasta onde os modelos serão salvos
    save_models_path = "C:/Users/Pedro/Documents/GitHub/Omega/Modelos_ML"
    
    # Carregar os dados
    data = load_data(data_file_path)
    
    # Treinar e salvar modelos
    train_and_save_models(data, target_column, num_models_to_select, save_models_path)
