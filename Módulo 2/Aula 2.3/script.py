import pandas as pd
import numpy as np


# Importando um banco de dados do campeonato brasileiro
futebol = pd.read_csv('Módulo 2/Aula 2.3/campeonato-brasileiro-full.csv',
                      usecols = ['mandante', 'visitante', 'mandante_Placar', 'visitante_Placar', 'vencedor', 'data'])

# Verificando informações sobre o banco de dados
# print(df.shape, df.columns, df.index, df.dtypes)

# Criando um dataframe
dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Lucas'],
    'Idade': [18, 20, 19, 22, 31],
    'Nota': [8.5, 7.2, 9.8, 6.4, 7.9],
    'Cidade': ['BH', 'SP', 'BH', 'RJ', 'SP']
}
df = pd.DataFrame(dados)
print(df)

# Exibindo as primeiras 3 linhas com a head()
print(df.head(3))

# Primeiras 10 linhas
print(futebol.head(10))

# Exibindo as últimas 2 linhas com tail()
print(df.tail(2))

# Exibindo informações do banco de dados com info()
df.info()
futebol.info()

# Exibindo várias estatísticas numéricas usando describe()
print(df.describe())
print(futebol.describe())

# Calculando estatísticas de colunas str também com o parâmetro include = 'all'
print(df.describe(include='all'))
print(futebol.describe(include='all'))

# Calculando quantos alunos existem em cada cidade com value_counts()
print(df['Cidade'].value_counts())

# Calculando quantos jogos cada time venceu (calculando quantas vezes cada valor aparece em determinada coluna)
print(futebol['vencedor'].value_counts())

# Vendo quais cidades diferentes existem usando unique()
print(df['Cidade'].unique())

# Vendo quantas cidades diferentes existem com nunique()
print(df['Cidade'].nunique())

# Selecionando 2 linhas aleatórias com sample()
print(df.sample(2))
print(futebol.sample(2))

# Verificando o shape, as colunas, o tamanho e os tipos de dados
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)