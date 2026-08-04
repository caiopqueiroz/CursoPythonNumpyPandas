import pandas as pd
import numpy as np


dados = {
    'Pedido': [101, 102, 103, 104],
    'Data': [
        '2026-01-10',
        '2026-02-15',
        '2026-03-20',
        '2026-03-01'
        ],
    'Valor': [120, 250, 80, 500]
}
df = pd.DataFrame(dados)

# Convertendo a coluna Data para o formato de datas usando to_datetime()
df['Data'] = pd.to_datetime(df['Data'])
print(df['Data'])

# Checando o tipo de dado da coluna Data
print(df.dtypes)

# Extraindo componentes da coluna Data - ano 
df['Ano'] = df['Data'].dt.year
print(df)

# Mês 
df['Mês'] = df['Data'].dt.month

# Dia
df['Dia'] = df['Data'].dt.day

# Dia da semana
df['Dia da semana'] = df['Data'].dt.day_name()

# Ordenando o df pela coluna ano - do mais antigo até o mais novo
print(df.sort_values('Ano'))

# Inserindo uma nova coluna Nome do mês na posição 5
df.insert(
    5,
    'Nome do mês',
    df['Data'].dt.month_name()
)
print(df)

# Filtrando por data - posteriores a 1º de fevereiro de 2026
print(df[
    df['Data'] >= '2026-02-01'
])

# Filtrando por intervalos de datas 
print(df[
    (df['Data'] >= '2026-02-01') & (df['Data'] <= '2026-02-28')
])

# Calculando intervalo entre datas - primeiro e último pedido
# Primeiro pedido
primeiro = df.iloc[df['Data'].idxmin(), 1]
# Último pedido
ultimo = df.iloc[df['Data'].idxmax(), 1]
# Cálculo 
print(ultimo - primeiro) # 69 dias 

# Criando uma nova coluna com datas - coluna Entrega com a data da compra + 7 dias usando pd.Timedelta(days = 7) 
df['Entrega'] = df['Data'] + pd.Timedelta(days = 7)
print(df)

# Exibindo a data e hora atuais 
print(pd.Timestamp.now())

# Ordenando o df cronologicamente 
print(df.sort_values('Data'))

# Formatando a coluna Data e a coluna Entrega - mas ao utilizar essa função, strftime(), o resultado obtido volta a ser texto, impossibilitando ordenações ou operações 
# df['Data'] = (
#    df['Data'].dt.strftime('%d/%m/# %Y')
# )
# df['Entrega'] = df['Entrega'].dt.# strftime('%d/%m/%Y')
# print(df)

# Ex 1:
df['Data'] = pd.to_datetime(df['Data'])
print(df)

# Ex 2:
df.drop(
    columns = ['Dia', 'Mês', 'Ano'],
    inplace = True
)
df['Ano'] = df['Data'].dt.year
df['Mês'] = df['Data'].dt.month
df['Dia'] = df['Data'].dt.day
print(df)

# Ex 3:
print(df[
    df['Data'] >= '2026-02-15'
])

# Ex 4:
df.drop(
    columns = 'Entrega',
    inplace = True
)
df.insert(
    2,
    'Entrega',
    df['Data'] + pd.Timedelta(days = 10)
)
print(df)

# Desafio:
relatorio = df.drop(
    columns = ['Nome do mês', 'Dia da semana', 'Ano', 'Mês', 'Dia', 'Entrega']
)
print(relatorio)
relatorio['Nome do mês'] = df['Data'].dt.month_name()
relatorio['Dia da semana'] = df['Data'].dt.day_name()
relatorio['Data formatada'] = relatorio['Data'].dt.strftime('%d/%m/%Y')
relatorio = relatorio.sort_values('Data', ignore_index = True)
relatorio.drop(
    columns = 'Data',
    inplace = True
)
print(relatorio)