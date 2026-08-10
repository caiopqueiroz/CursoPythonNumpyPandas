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

# Exibindo as principais características do banco 
print('-'*20)
print('Número de linhas: ', paises.shape[0])
print('Número de colunas: ', paises.shape[1])
print('Índices: ', paises.index)
print('Colunas: ', paises.columns)
print('Tipos das colunas: ', paises.dtypes)
print('Tipo dos rótulos: ', paises.index.dtype)

# Filtrando um elemento específico no df
print(paises.loc['BR', 'continente']) # América
print(paises.iloc[1, 1]) # América
print(paises.loc['UK', 'extensao']) # 244
print(paises.iloc[4, 2]) # 244

# Filtrando linhas e colunas simultaneamente usando a forma [inicio:fim, inicio:fim]
print(paises.iloc[0:3, 0:2])
print(paises.loc['FR':'IT', 'nome':'extensao'])

# Verificando se um determinado rótulo de linha ou coluna existe em um df - para isso, usamos expressões lógicas: 'XX' in df.index / 'XX' in df.columns - que retornam True ou False
print('Existe BR? ', 'BR' in paises.index)
print('Existe US? ', 'US' in paises.index)

print('Existe a coluna corVerde? ', 'corVerde' in paises.columns)

print('Existe Brasil? ', paises['nome'].isin(['Brasil']))

# Inserindo um novo país ao df
paises.loc['JP'] = {
    'nome': 'Japão',
    'continente': 'Ásia',
    'extensao': 372,
    'corVerde': 0
}

# Alterando um elemento do df - extensão do Brasil
paises.loc['BR', 'extensao'] = 8512

# Removendo países - Argentina
paises.drop(
    ['AR'],
    inplace = True
)

print(paises)

