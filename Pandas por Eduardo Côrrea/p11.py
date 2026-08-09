import pandas as pd 


# Criando o dataframe paises
dados = {
    'nome': ['Argentina', 'Brasil', 'França', 'Itália', 'Reino Unido'],
    'continente': ['América', 'América', 'Europa', 'Europa', 'Europa'],
    'extensao': [2780, 8511, 644, 301, 244],
    'corVerde': [0, 1, 0, 1, 0]
}
siglas = ['AR', 'BR', 'FR', 'IT', 'UK']
paises = pd.DataFrame(
    dados,
    index = siglas
    )
print(paises.sort_values('extensao', ascending = False))

# Filtrando um elemento específico no df
print(paises.loc['BR', 'continente']) # América
print(paises.iloc[1, 1]) # América
print(paises.loc['UK', 'extensao']) # 244
print(paises.iloc[4, 2]) # 244

# Exibindo as principais características do banco 
print('-'*20)
print('Número de linhas: ', paises.shape[0])
print('Número de colunas: ', paises.shape[1])
print('Índices: ', paises.index)
print('Colunas: ', paises.columns)
print('Tipos das colunas: ', paises.dtypes)
print('Tipo dos rótulos: ', paises.index.dtype)


