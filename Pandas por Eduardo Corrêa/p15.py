# Importando um banco de um arquivo externo 
import pandas as pd 


# Importando o banco com a coluna sigla funcionando como índice para as linhas 
paises = pd.read_csv(
    'Pandas por Eduardo Corrêa/paises.csv',
    index_col = 'sigla'
)
print(paises)

# Mostrando parâmetros úteis para a função read_csv()
# sep (mudar separador)
# index_col (definir uma coluna para ser índice das linhas)
# na_values (valores que deverão ser substituídos por NA)