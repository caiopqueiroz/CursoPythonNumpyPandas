import pandas as pd 


dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Lucas'],
    'Idade': [18, 20, 19, 22, 21],
    'Nota': [8.5, 7.2, 9.8, 6.4, 7.9]
}
df = pd.DataFrame(dados)

# Ex 1:
print(df.iloc[0]) # Primeira linha
print(df.iloc[-1]) # Última linha

# Ex 2:
print(df.iloc[1:4]) # Linhas 1, 2 e 3
print(df.iloc[:, 2]) # Coluna Nota

# Ex 3:
df.index = ['A', 'B', 'C', 'D', 'E']
print(df.loc['C'])
print(df.loc['D', 'Nota']) # 6.4

# Ex 4:
print(df.loc[:, ['Nome', 'Nota']])
print(df[['Nome', 'Nota']])

# Desafio:
print(df.iloc[0:3, [0, 2]])