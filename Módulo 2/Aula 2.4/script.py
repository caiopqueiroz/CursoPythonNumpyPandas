import pandas as pd 


dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Lucas'],
    'Idade': [18, 20, 19, 22, 21],
    'Nota': [8.5, 7.2, 9.8, 6.4, 7.9],
    'Cidade': ['BH', 'SP', 'BH', 'RJ', 'SP']
}
df = pd.DataFrame(dados)
print(df)

# Exibindo uma linha do banco pelo índice usando iloc
print(df.iloc[0])

# Criando rótulos e exibindo uma linha através dele usando loc
df.index = ['A', 'B', 'C', 'D', 'E']
print(df.loc['A'])
print(df.loc['E'])

# Selecionando várias linhas 
print(df.iloc[[0, 2, 4]])
print(df.loc['A', 'B', 'E'])

# Selecionando um intervalo de linhas 
print(df.iloc[0:3])

# Selecionando todas as linhas de uma coluna
print(df.iloc[:, 3])
print(df.loc[:, 'Idade'])

# Selecionando linhas e colunas - um elemento específico

# Usando o iloc (posição numérica)
print(df.iloc[0, 0]) # Ana
print(df.iloc[3, 3]) # RJ

# Usando o loc (rótulo e nome da coluna)
print(df.loc['A', 'Nome']) # Ana
print(df.loc['E', 'Idade']) # 21