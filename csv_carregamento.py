import time
from Class.csv_class_load import CsvProcessor
from datetime import datetime

# Definindo o caminho do arquivo e os parâmetros de filtro
start = time.time()
arquivo_csv = "data/exemplo.csv"
filtro = "estado"
limite = "MG"

# Instanciando o objeto CsvProcessor e carregando o arquivo CSV
arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

# Filtrando os dados
df_filtrado = arquivo_CSV.filtrar_por_estado(filtro, limite)

# Verificando o conteúdo filtrado (opcional)
print(df_filtrado)

# Gerando horario
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Salvando os dados filtrados em um novo arquivo
arquivo_CSV.salvar_dados(f"data/exemplo_filtrado-{timestamp}.csv")

# Medindo o tempo de execução
stop = time.time()
print(f"Tempo de execução: {stop - start} segundos")
