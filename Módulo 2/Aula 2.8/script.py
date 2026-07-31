import pandas as pd
import numpy as np 


dados = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Webcam', 'Headset'],
    'Preço': [80, 150, 900, 250, 320],
    'Estoque': [12, 7, 4, 10, 5]
}
df = pd.DataFrame(dados)

# Ordendando o banco pela coluna Preço - menor para maior 
print(df.sort_values('Preço'))

# Maior para menor, pelo estoque, usando asceding = False
print(df.sort_values(
    'Estoque',
    ascending = False
))

# Usando duas ou mais colunas - primeiro parâmetro: preço, depois estoque, para caso de empate
print(df.sort_values(
    ['Preço', 'Estoque'],
    ascending = False
))

# Ordendando pelo índice 
print(df.sort_index())

# Mostrando estatísticas básicas
print(df['Preço'].mean())       # Média
print(np.mean(df['Preço']))     # Média
print(df['Estoque'].sum())      # Soma
print(df['Preço'].max())        # Máximo
print(df['Preço'].min())        # Mínimo
print(df['Preço'].mode())       # Moda
print(df['Estoque'].median())   # Mediana
print(df['Preço'].std())        # Desvio padrão

# Mostrando índice do maior e menor preço 
print(df['Preço'].idxmax())
print(df['Preço'].idxmin())

# Mostrando todas as colunas da linha com o maior preço usando loc 
print(df.loc[
    df['Preço'].idxmax()
])

# Mostrando apenas os 2 maiores valores da coluna Preço usando nlargest() 
print(df.nlargest(
    2, 
    'Preço'
))

# 3 menores valores usando nsmallest()
print(df.nsmallest(
    3,
    'Preço'
))

# Mostrando um resumo das principais estatísticas numéricas 
print(df.describe())

# Ex 1:
print(df.sort_values('Preço'))
print(df.sort_values(
    'Preço',
    ascending = False
    ))

# Ex 2:
print(df['Preço'].mean())
print(np.mean(df['Preço']))
print(np.sum(df['Estoque']))

# Ex 3:
print(df['Preço'].max())
print(np.min(df['Preço']))
print(np.median(df['Estoque']))

# Ex 4:
print(df.nlargest(
    2,
    'Preço'
))
print(df.nsmallest(
    3,
    'Estoque'
))

# Desafio:
print(df['Preço'].max()) # Maior preço: 900
print(df.loc[ # Monitor 
    df['Preço'].idxmax()
])
print(df['Estoque'].min()) # Menor estoque: 4
print(df.loc[ # Monitor
    df['Estoque'].idxmin()
])