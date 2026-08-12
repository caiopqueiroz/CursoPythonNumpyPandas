# Importando outro banco de dados 
import pandas as pd 


# Importando o df
gols = pd.read_csv(
    'Pandas por Eduardo Corrêa/gols.csv',
    sep = ' ',
    index_col = 'dia',
    )

# Tornando ele em uma series com a função squeeze()
gols = gols.squeeze()

# Convertendo os rótulos para o formato de data - pd.to_datetime()
gols.index = pd.to_datetime(
    gols.index,
    format = '%d/%m/%Y'
)

print(gols)