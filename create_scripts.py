import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_fake_data(num_rows=100):
    # Seed para garantir a reprodutibilidade dos dados gerados
    np.random.seed(42)
    
    # Variáveis
    timestamps = [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_rows)]
    temperatura = np.random.uniform(10, 40, num_rows)
    pressao = np.random.uniform(900, 1100, num_rows)
    velocidade = np.random.uniform(0, 10, num_rows)
    producao = np.random.randint(100, 1000, num_rows)

    # Criando DataFrame
    data = {
        'Timestamp': timestamps,
        'Temperatura': temperatura,
        'Pressao': pressao,
        'Velocidade': velocidade,
        'Producao': producao
    }

    df = pd.DataFrame(data)
    df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

    return df

def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)
    print(f'Dados salvos em {filename}')

def create_script(setor, empresas, output_folder):
    script_content = (
        "import pandas as pd\n"
        "import numpy as np\n"
        "import random\n"
        "from datetime import datetime, timedelta\n"
        "import os\n\n"
        
        "def generate_fake_data(num_rows=100):\n"
        "    np.random.seed(42)\n"
        "    timestamps = [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_rows)]\n"
        "    temperatura = np.random.uniform(10, 40, num_rows)\n"
        "    pressao = np.random.uniform(900, 1100, num_rows)\n"
        "    velocidade = np.random.uniform(0, 10, num_rows)\n"
        "    producao = np.random.randint(100, 1000, num_rows)\n\n"

        "    data = {\n"
        "        'Timestamp': timestamps,\n"
        "        'Temperatura': temperatura,\n"
        "        'Pressao': pressao,\n"
        "        'Velocidade': velocidade,\n"
        "        'Producao': producao\n"
        "    }\n\n"

        "    df = pd.DataFrame(data)\n"
        "    df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')\n\n"

        "    return df\n\n"

        "def save_to_csv(dataframe, filename):\n"
        "    dataframe.to_csv(filename, index=False)\n"
        "    print(f'Dados salvos em {filename}')\n\n"

        "if __name__ == \"__main__\":\n"
        "    min_rows = 5000\n"
        "    max_rows = 25000\n\n"

        f"    setores_empresas = {empresas}\n\n"

        f"    output_folder = \"{output_folder}\"\n\n"

        "    for setor, empresas in setores_empresas:\n"
        "        for empresa in empresas:\n"
        "            num_rows = np.random.randint(min_rows, max_rows)\n"
        "            dados = generate_fake_data(num_rows)\n"
        "            filename = os.path.join(output_folder, f'{setor}_{empresa}_dados_desempenho_industrial.csv')\n"
        "            save_to_csv(dados, filename)\n"
        "            file_size_mb = os.path.getsize(filename) / (1024 * 1024)\n"
        "            print(f'CSV para a empresa \"{empresa}\" no setor \"{setor}\" criado em: {filename}')\n"
        "            print(f'Tamanho do arquivo: {file_size_mb:.2f} MB\\n')\n\n"

        "    script_path = os.path.join(output_folder, f\"{setor}_script.py\")\n"
        "    with open(script_path, 'w') as script_file:\n"
        "        script_file.write(script_content)\n\n"

        "    print(f'Script para o setor \"{setor}\" criado em: {script_path}')"
    )

    exec(script_content)

if __name__ == "__main__":
    setores_empresas = [
        ("Manufatura", [
            "InovaTech", "EcoPower", "TechGlobe", "FreshHarvest", "SwiftLogistics",
            "MegaFabrica", "GreenMachining", "SmartAssembly", "SteelCraft", "PrecisionWorks",
            "NanoMaterials", "AgileManufacture", "FutureFoundry", "PioneerProduction", "DynamicMachines"
        ]),
        ("Energia", [
            "EcoPower", "CleanEnergyCorp", "WindInnovations", "SolarHarvest", "HydroTech",
            "EnergyDynamics", "EcoEnergize", "RenewaGen", "SunSolutions", "WindForce",
            "FusionEra", "SustainablePower", "QuantumEnergy", "EcoFuel", "FutureGrid"
        ]),
        ("Tecnologia", [
            "TechGlobe", "InnoSoft", "DataDynamics", "CodeCrafters", "FutureTech",
            "QuantumSolutions", "DigitalPulse", "NeuralTech", "SmartSystems", "CyberInnovate",
            "NanoCode", "InnoHub", "InfoNex", "TechStorm", "DigitalFrontiers"
        ]),
        ("Alimentos", [
            "FreshHarvest", "EcoFoods", "AgriInnovate", "NutriNectar", "GreenHarvest",
            "OrganicFeast", "FarmFresh", "BioBites", "NatureNourish", "PureHarvest",
            "FlavorFusion", "FarmToTable", "HealthyHarvest", "OrganicEats", "FoodRevolution"
        ]),
        ("Logística", [
            "SwiftLogistics", "AgileShipping", "TechTransport", "DynamicDelivery", "ExpressCargo",
            "SwiftFreight", "LogiConnect", "EcoHaul", "SmartShipping", "FutureLogistics",
            "RapidTransit", "GreenCargo", "LogisticsHub", "QuickShip", "InnoMovers"
        ])
    ]

    create_script("DesempenhoIndustrial", setores_empresas, "C:/Users/Pedro/Projetos/Omega/Csvs")
