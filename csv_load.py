#Exemplo sem utilização de classe.

import pandas as pd
import time
start = time.time()

path = 'data/exemplo.csv'

df = pd.read_csv(path)

# df_filtrado = df.query('estado == "SP"') #Execution time = 0.009
df_filtrado = df[df['estado'] == 'SP'] #Execution time = 0.008

print(df_filtrado)

stop = time.time()

print(stop - start)