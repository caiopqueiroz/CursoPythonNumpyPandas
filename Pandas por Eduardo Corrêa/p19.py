# Importando um banco de dados de um arquivo JSON
import pandas as pd
import json


# Importando um arquivo JSON para a memória
with open(
    'Pandas por Eduardo Corrêa/notas.json'
) as f:
    j_notas = json.load(f)

# Transferindo as informações para um dataframe
notas = pd.DataFrame(
    j_notas,
    columns = ['matricula', 'notas']
)

print(notas)