# Criação do projeto prático utilizando o banco de dados com informações sobre 195 países
import pandas as pd


# Importando o banco 
bandeiras = pd.read_csv(
    'Pandas por Eduardo Corrêa/flags.csv',
    index_col = 'name'
)

# Verificando informações iniciais
print(bandeiras.shape)
print(bandeiras.columns)
print(bandeiras.loc['Brazil'])

# Verificando quais países possuem em sua bandeira as cores green, gold, white, blue 
print(bandeiras.index[
    (bandeiras['green'] == 1) &
    (bandeiras['gold'] == 1) &
    (bandeiras['white'] == 1) &
    (bandeiras['blue'] == 1)
])
