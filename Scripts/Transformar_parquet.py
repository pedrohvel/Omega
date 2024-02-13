import dask.dataframe as dd
import pyarrow as pa
import pyarrow.parquet as pq
from alive_progress import alive_bar

# Caminho para o arquivo CSV
csv_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE.csv"

# Leitura usando Dask
df = dd.read_csv(csv_file_path, assume_missing=True)

# Adicionar coluna alvo
df['Target'] = (df['Revenue'] > 800000).astype(int)

# Contagem de linhas para a barra de progresso
total_rows = len(df)

# Inicializar barra de progresso
with alive_bar(total_rows, title="Processando CSV") as bar:
    # Conversão para uma tabela Arrow
    table = pa.Table.from_pandas(df.compute(), preserve_index=False)

# Caminho para o arquivo Parquet
parquet_file_path = "C:/Users/Pedro/Documents/GitHub/Omega/Pentaho/DATAWAREHOUSE_Target.parquet"

# Salvar como formato Parquet
pq.write_table(table, parquet_file_path)

print(f'Arquivo Parquet salvo em: {parquet_file_path}')
