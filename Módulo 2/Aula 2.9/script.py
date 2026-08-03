import pandas as pd 


dados = {
    'Vendedor': ['Ana', 'Ana', 'João', 'João', 'Maria', 'Maria'],
    'Cidade': ['BH', 'BH', 'SP', 'SP', 'BH', 'RJ'],
    'Produto': ['Mouse', 'Monitor', 'Mouse', 'Teclado', 'Monitor', 'Mouse'],
    'Valor': [80, 900, 80, 150, 900, 80]
}
df = pd.DataFrame(dados)

# Usando a estrutura do groupby() - agrupando pelo vendedor
df.groupby('Vendedor')

# Calculando a soma dos valores por vendedor - pegue o banco de dados, agrupe de acordo com a coluna Vendedor e some os valores
print(df.groupby('Vendedor')['Valor'].sum())

# Calculando a média dos valores por cidade - pegue o banco, agrupe por cidades iguais e calcule a média dos valores dos produtos
print(df.groupby('Cidade')['Valor'].mean())

# Calculando a média por vendedor
print(df.groupby('Vendedor')['Valor'].mean())

# Contando regitros - quantas vendas fez cada vendedor - contando quantas vezes aparece o nome de cada vendedor com size()
print(df.groupby('Vendedor').size())

# Mostrando a maior e menor venda por vendedor usando max() e min()
print(df.groupby('Vendedor')['Valor'].max())
print(df.groupby('Vendedor')['Valor'].min())

# Calculando múltiplas estatísticas de uma vez usando describe() ou agg()
print(df.groupby('Vendedor')['Valor'].describe())
print(df.groupby('Vendedor')['Valor'].agg(
    ['sum', 'mean', 'max', 'min']
))
print(df.groupby('Cidade')['Valor'].describe())

# Usando agg() nomeando agregações
print(df.groupby('Vendedor').agg(
    Total_vendas = ('Valor', 'sum'),
    Média_vendas = ('Valor', 'mean'),
    Maior_venda = ('Valor', 'max')
))

# Agrupando por mais de uma coluna - nesse caso, agrupando valores de produtos iguais da mesma cidade
print(df.groupby(
    ['Cidade', 'Produto']
)['Valor'].sum())

# Recuperando o data frame agrupado com os índices corrigidos usando reset_index() 
resultado = (
    df.groupby('Vendedor')['Valor'].sum()
    .reset_index()
)
print(resultado)

# Ex 1:
print(df.groupby('Vendedor')['Valor'].sum())
print(df.groupby('Vendedor')['Valor'].mean())

# Ex 2:
print(df.groupby('Cidade')['Produto'].count())
print(df.groupby('Cidade').size())
print(df.groupby('Cidade')['Valor'].describe())

# Ex 3:
print(df.groupby('Vendedor')['Valor'].max())
print(df.groupby('Vendedor')['Valor'].min())

# Ex 4:
print(df.groupby('Cidade')['Valor'].sum())

# Desafio:
novo_df = (
    df.groupby('Vendedor').agg(
    Total_vendido = ('Valor', 'sum'),
    Média_vendas = ('Valor',  'mean'),
    Maior_venda = ('Valor', 'max'),
    Menor_venda = ('Valor', 'min'),
    Quantidade_vendas = ('Valor', 'size'))
    .reset_index()
    )
print(novo_df)