import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os
import pickle
from faker import Faker

fake = Faker()

def generate_fake_data(num_rows=100, num_columns=20, industries=None, seed=42):
    np.random.seed(seed)

    if industries is None:
        industries = ["Industry1", "Industry2", "Industry3", "Industry4", "Industry5"]

    # Geração de dados para as colunas
    timestamps = [datetime.now() - timedelta(days=i) for i in range(num_rows)]

    # Verificar se existe um arquivo de estado
    state_file = 'state.pkl'
    if os.path.exists(state_file):
        with open(state_file, 'rb') as f:
            state = pickle.load(f)
    else:
        state = {
            'row_index': 0,
            'col_index': 0
        }

    # Nome fictício da empresa e setor
    company_names = [fake.company() for _ in range(num_rows)]
    industry_names = [fake.bs() for _ in range(num_rows)]

    # Adicionar coluna de índice de linha e coluna
    columns_data = {
        'Timestamp': timestamps,
        'Company_Name': company_names,
        'Industry_Type': industry_names,
        'Temperature': np.random.uniform(10, 40, num_rows),
        'Pressure': np.random.uniform(900, 1100, num_rows),
        'Velocity': np.random.uniform(0, 10, num_rows),
        'Production': np.random.randint(100, 1000, num_rows),
        'Row_Index': range(state['row_index'], state['row_index'] + num_rows),
        'Col_Index': state['col_index']
    }

    for i in range(5, num_columns):
        col_name = f'Column_{i+1}'
        columns_data[col_name] = np.random.random(size=num_rows)

        # Introduzindo erros propositais
        error_indices = random.sample(range(num_rows), num_rows // 10)
        for idx in error_indices:
            columns_data[col_name][idx] = np.nan

    # Criando DataFrame
    df = pd.DataFrame(columns_data)
    df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Salvar estado
    state['row_index'] += num_rows
    with open(state_file, 'wb') as f:
        pickle.dump(state, f)

    return df

def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    print(f'Dados salvos em {filename}')

if __name__ == "__main__":
    industries = [
        "Industry1", "Industry2", "Industry3", "Industry4", "Industry5"
    ]

    min_rows = 10000
    max_rows = 50000
    num_columns = 20
    output_folder = "C:/Users/Pedro/Documents/GitHub/Omega/Csvs"

    for industry in industries:
        for i in range(50):
            num_rows = np.random.randint(min_rows, max_rows)
            dados = generate_fake_data(num_rows, num_columns, industries)
            filename = os.path.join(output_folder, f'{industry}_{i+1}_performance_data.csv')
            
            # Garante que o CSV tenha pelo menos 3MB e no máximo 6MB
            while True:
                dados.to_csv(filename, index=False)
                file_size_mb = os.path.getsize(filename) / (1024 * 1024)
                if 3 <= file_size_mb <= 6:
                    break

            save_to_csv(dados, filename)
            print(f'CSV para a indústria "{industry}", arquivo {i+1} criado em: {filename}')
            print(f'Tamanho do arquivo: {file_size_mb:.2f} MB\n')
