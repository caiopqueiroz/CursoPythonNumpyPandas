import pandas as pd
import numpy as np


dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro'],
    'Idade': [18, np.nan, 19, 22],
    'Nota': [8.5, 7.2, np.nan, 6.4] 
}
df = pd.DataFrame(dados)
print(df)

# Teste 
df_novo = pd.DataFrame(dados)
print(df_novo)

# Excluindo a coluna de nomes com drop()
df_novo.drop(
    columns = ['Nome'],
    inplace = True
)

# Criando rótulos como os nomes dos alunos 
df_novo.index = ['Ana', 'João', 'Maria', 'Pedro']

# Acessando a idade de Ana usando loc
print(df_novo.loc[
    'Ana',      # Linha desejada: Ana
    'Idade'     # Coluna desejada: Idade
    ])

# Identificando valores ausentes com isna() ou isnull()
print(df.isna())
print(df.isnull())

# Contando valores ausentes com sum()
print(np.sum(df.isna())) # Soma total
print(df.isna().sum()) # Quantidade por coluna

# Removendo linhas com valores ausentes com dropna()
print(df.dropna())

# Removendo apenas quando todas as colunas são valores Nan - só remove linhas completamente vazias
print(df.dropna(
    how = 'all'
))

# Removendo colunas com o parâmetro axis = 1
print(df.dropna(
    axis = 1
))

# Preenchendo valores ausentes com valor fixo - no caso, 0 
print(df.fillna(
    0,
    inplace = False
    ))
print(df)

# Preenchendo com a média 
media = df['Idade'].mean()
df['Idade'] = df['Idade'].fillna(media)
print(df)

# Preenchendo com a moda 
moda = df['Idade'].mode()[0]
df['Idade'] = df['Idade'].fillna(moda)
print(df)

# Preenchendo com o valor anterior na coluna usando ffill()
df.fillna(
    method = 'ffill'
)

# Com o valor posterior usando bfill()
df.fillna(
    method = 'bfill'
)