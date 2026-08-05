import pandas as pd 


dados = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'Preço': [80, 150, 900, 250],
    'Quantidade': [12, 7, 4, 10]
}
df = pd.DataFrame(dados)

# Criando uma nova coluna 
df['Categoria'] = 'Informática'
print(df)

# Criando uma coluna usando uma lista
df['Marca'] = ['Logitech', 'Redragon', 'LG', 'Logitech']
print(df)

# Criando uma coluna a partir de outras - valor total em estoque 
df['Valor total'] = df['Preço'] * df['Quantidade']
print(df)

# Criando uma coluna a partir de operações matemáticas - preço com desconto
df['Preço com desconto'] = df['Preço'] * 0.7
print(df)

# Preço com frete
df['Preço com frete'] = df['Preço'] + 20
print(df)

# Alterando uma coluna existente - reajuste de preço
df['Preço'] *= 1.1
print(df)

# Alterando a coluna apenas em linhas específicas - monitores com aumento
df.loc[
    df['Produto'] == 'Monitor', # Linha que deve ser alterada
    'Preço'                     # Coluna que deve ser alterada
] = 950
print(df)

# Renomeando colunas - inplace = False não altera o dataframe original
df.rename(
    columns = {
        'Preço': 'Preco',
        'Quantidade': 'Qtd'
    },
    inplace = True
)
print(df)

# Removendo colunas 
df.drop(
    columns = ['Preço com frete', 'Preço com desconto'],
    inplace = True
)
print(df)

# Inserindo uma coluna em uma posição específica com insert - código na posição 1
df.insert(
    1,
    'Código',
    [101, 102, 103, 104]
)
print(df)

# Ex 1:
df['Fornecedor'] = 'Tech Store'

# Ex 2:
df['Valor total'] = df['Preco'] * df['Qtd']

# Ex 3:
df['Preço promocional'] = df['Preco'] * 0.85

# Ex 4:
df = df.rename(
    columns = {
        'Qtd': 'Estoque',
        'Preco': 'Preco'
    }
)

# Desafio:
df['Frete'] = 30
df['Preço final'] = df['Preco'] + df['Frete']
df = df.drop(
    columns = ['Frete']
)

print(df)
