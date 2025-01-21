# Exemplo sem utilização de classe.

import pandas as pd
import time

start = time.time()

path = "data/campeonato-brasileiro-gols.csv"

df = pd.read_csv(path)

# df_filtrado = df.query('estado == "SP"') #Execution time = 0.009
df_filtrado = df[df["clube"] == "Vasco"]  # Execution time = 0.008
df_filtrado_minuto = df_filtrado[df_filtrado["minuto"] <= "42"]
df_filtrado_minuto_ordenado = df_filtrado_minuto.sort_values(
    by="partida_id", ascending=False
)
ascending = [True]
# print(df)
print(df_filtrado_minuto_ordenado.head(10))

stop = time.time()

print(stop - start)
