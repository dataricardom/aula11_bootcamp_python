import time
from csv_class_load import CsvProcessor

start = time.time()

arquivo_csv = 'data/exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

print(arquivo_CSV.filtrar_por_estado(filtro,limite))

stop = time.time()

print(stop - start)