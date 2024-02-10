import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_fake_data(num_rows=100, num_columns=15, company_name=None, industry_type=None):
    timestamps = [datetime.now() - timedelta(days=i) for i in range(num_rows)]
    
    columns_data = {
        'Timestamp': timestamps,
        'Company_Name': [company_name] * num_rows,
        'Industry_Type': [industry_type] * num_rows,
        'Revenue': np.random.randint(500000, 1000000, num_rows),
        'Expenses': np.random.randint(300000, 700000, num_rows),
        'Profit': np.random.randint(100000, 400000, num_rows),
        'Efficiency': np.random.uniform(0.7, 0.95, num_rows),
        'Quality': np.random.uniform(0.7, 0.95, num_rows),
        'Innovation': np.random.uniform(0.7, 0.95, num_rows),
        'Satisfaction': np.random.uniform(0.7, 0.95, num_rows),
        'Market_Share': np.random.uniform(5, 20, num_rows),
        'Key_Column': [f'Key_{i}' for i in range(num_rows)]
    }

    df = pd.DataFrame(columns_data)
    df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Adicionando estatísticas fictícias
    df['Mean_Value'] = df['Efficiency'] * df['Quality'] * df['Innovation']
    df['Max_Value'] = df[['Revenue', 'Expenses', 'Profit']].max(axis=1)
    df['Min_Value'] = df[['Revenue', 'Expenses', 'Profit']].min(axis=1)
    df['Total_Production'] = df['Market_Share'] * 1000

    return df

def create_csvs(output_folder, num_csvs_per_sector=10):
    setores_empresas = [
        ("Tecnologia", "TechGlobe"),
        ("Saúde", "HealthCare"),
        ("Manufatura", "ManufaturaCo"),
        ("Energia", "EnerTech"),
        ("Logística", "SwiftLogistics")
        # Adicione mais setores e empresas conforme necessário
    ]

    for setor, empresa in setores_empresas:
        for i in range(num_csvs_per_sector):
            num_rows = np.random.randint(10000, 50000)
            fake_company_name = fake.company()

            dados = generate_fake_data(num_rows, company_name=fake_company_name, industry_type=setor)

            csv_name = f'Dados_{setor}_{fake_company_name}_{i+1}'

            dados['Company_ID'] = f'{setor}_{fake_company_name}'

            filename = os.path.join(output_folder, f'{csv_name}.csv')

            dados.to_csv(filename, index=False)
            print(f'CSV para a empresa "{fake_company_name}", setor "{setor}", arquivo {i+1} criado em: {filename}')

if __name__ == "__main__":
    output_folder = "C:/Users/Pedro/Documents/GitHub/Omega/Csvs"
    create_csvs(output_folder)
