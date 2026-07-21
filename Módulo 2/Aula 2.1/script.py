# Importando a biblioteca pandas
import pandas as pd


# Criando uma series
idades = pd.Series([18, 20, 19, 22])

# Criando uma series com índices personalizados
idades2 = pd.Series(
    [18, 20, 19],
    index = ['Ana', 'João', 'Maria']
)
print(idades)

# Acessando valores pelo índice numérico
print(idades[0])

# Pelo índice personalizado
print(idades2['Ana'])

# Criando um dataframe
dados = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [18, 20, 19],
    'Nota': [8.5, 7.2, 9.8]
}
df = pd.DataFrame(dados)
print(df)

# Obtendo uma ou mais colunas 
print(df['Nome'])
print(df[['Nome', 'Nota']])

# Obtendo informações sobre o dataframe 
print(df.shape) # Quantidade de linhas e colunas
print(df.columns) # Nomes das colunas
print(df.index) # Índice de início e de parada
print(df.dtypes) # Tipos de dados

# Recuperando o array numpy interno
print(df.to_numpy())

# Ex 1:
series = pd.Series([5, 10, 15, 20])
print(series)

# Ex 2:
notas = pd.Series([8.0, 6.5, 9.3], index = ['Ana', 'Bruno', 'Carla'])
print(notas)