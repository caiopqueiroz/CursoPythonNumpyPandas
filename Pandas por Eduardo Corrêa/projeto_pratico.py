# Criação do projeto prático utilizando o banco de dados com informações sobre 195 países
import pandas as pd
import numpy as np


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

# Verificando quais são os tipos de dados existentes no df 
# Criando um vetor booleano tipos_int que verifica quais colunas tem o tipo de dado int64 e retorna o valor True para elas 
tipos_int = bandeiras.dtypes.values == 'int64'
# Usando a função np.sum() para somar a quantidade de valores True, que retorna o número total de colunas com tipo de dado int64 - assim, descobrimos que o banco de dados possui 26 atributos (colunas) do tipo numérico
print('Número de colunas int64: ', np.sum(tipos_int))
# Usando a mesma função, agora com o operador ~, que inverte a series, logo serão contadas as colunas que contém str - dessa forma, percebemos que são 3 atributos (colunas) apenas do tipo categórico
print('Número de colunas str: ', np.sum(~(tipos_int)))

# Verificando quais os maiores e menores valores de população no banco de dados 
print(bandeiras['population'].nlargest(
    3
))
print(bandeiras.nsmallest(
    3,
    'population'
))