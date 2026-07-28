import pandas as pd 


dados = {
    'Nome': ['Caio', 'Júlia'],
    'Idade': [19, 20]
}
df = pd.DataFrame(dados)

# Selecionando uma linha 
print(df.iloc[0])
print(df.iloc[1])

# Criando rótulos 
df.index = ['Namorado', 'Namorada']

# Selecionando uma linha pelo rótulo 
print(df.loc['Namorado'])

# Selecionando um elemento pelo rótulo 
print(df.loc['Namorado', 'Idade']) # 19
print(df.loc['Namorada', 'Nome']) # Júlia

# Criando um dataframe 
dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Lucas', 'Carla'],
    'Idade': [18, 20, 19, 22, 21, 29],
    'Nota': [8.5, 7.2, 9.8, 6.4, 7.9, 9.1],
    'Cidade': ['BH', 'SP', 'BH', 'RJ', 'SP', 'BH']
}
df = pd.DataFrame(dados)

# Filtrando uma coluna - alunos com nota maior que 8
print(df['Nota'] > 8)

# Aplicando a máscara booleana de filtragem
print(df[df['Nota'] > 8])

# Filtrando uma coluna e exibindo apenas algumas colunas - nesse caso: exibindo apenas nome e nota de indivíduos com idade menor que 20
print(df[df['Idade'] < 20].iloc[:, [0, 2]])

# Filtrando por texto - apenas alunos de BH 
print(df[df['Cidade'] == 'BH'])

# Exceto alunos de BH
print(df[~(df['Cidade'] == 'BH')])

# Múltiplas condições - nota maior que 8 e cidade BH
print(df[
    (df['Nota'] > 8) & 
    (df['Cidade'] == 'BH')
    ])

# Cidade BH ou cidade RJ
print(df[
    (df['Cidade'] == 'BH') |
    (df['Cidade'] == 'RJ') 
])

# Filtrando várias colunas 
print(df[
    df['Nota'] > 7
].loc[:, ['Nome', 'Nota']])
print(df.loc[
    df['Nota'] > 7,
    ['Nome', 'Nota']
])

# Usando o método isin() - filtrando alunos de BH e RJ
print(df[
    df['Cidade'].isin(['BH', 'RJ'])
])

# Usando o método between() - filtrando alunos com nota entre 7 e 9 (inclusive)
print(df[
    df['Nota'].between(7, 9)
])

# Ex 1:
print(df[
    df['Nota'] >= 8
])
print(df[
    ~(df['Idade'] >= 20)
])

# Ex 2:
print(df[
    df['Cidade'] == 'SP'
])

# Ex 3:
print(df[
    (df['Nota'] > 8) &
    (df['Idade'] <= 20)
])

# Ex 4:
print(df[
    df['Cidade'].isin(['BH', 'RJ'])
])

# Desafio:
print(df[
    (df['Nota'].between(7, 9)) &
    (df['Cidade'].isin(['SP', 'BH']))
].loc[:, ['Nome', 'Nota']])