import pandas as pd
import time
start = time.time()

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None


    def carregar_csv(self):
            self.df = pd.read_csv(self.file_path)

    def filtrar_por_estado(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]
        

arquivo_csv = 'data/exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

print(arquivo_CSV.filtrar_por_estado(filtro,limite))

stop = time.time()

print(stop - start)
