import pandas as pd
import numpy as np 


# Carregando o banco de dados 
df = pd.read_csv('Módulo 2/Aula 2.12 - Projeto prático/banco_vendas_2026.csv')

# Exibindo o df
print(df)

# Parte 1 
print(df.shape) # 500 linhas e 13 colunas 
print(df.dtypes)
print(np.sum(df.isnull())) # Não existem NaN
# Registro duplicados 
df['Data'] = pd.to_datetime(df['Data'])
df_cronologico = df.sort_values('Data',
                                ignore_index = True)
data_primeira_venda = df_cronologico.iloc[0, 1]
data_ultima_venda = df_cronologico.iloc[499, 1]
print(data_ultima_venda - data_primeira_venda) # Período: 180 dias 

# Parte 2 
print(df['Valor_Total'].mean()) # Valor médio das vendas: R$1.802,34
print(df.iloc[
    df['Valor_Total'].idxmax(),
    10    
]) # Maior venda: R$17.500
print(df.nsmallest(
    1,
    'Valor_Total'
)['Valor_Total']) # Menor venda: R$32
print(df['Valor_Total'].sum()) # Total faturado: R$901.172,5
print(df['Quantidade'].sum()) # 1544 produtos vendidos

# Parte 3
print(df.groupby('Cidade')['Valor_Total'].sum().sort_values(
    ascending = False
)) # Maior: Salvador 
print(df.groupby('Estado')['Valor_Total'].sum().sort_values(
    ascending = False
)) # Maior: BA
print(df.groupby('Categoria')['Valor_Total'].sum().sort_values(
    ascending = False
)) # Maior: informática
print(df.groupby('Produto')['Quantidade'].sum().sort_values(
    ascending = False
)) # Maior: webcam
print(df.groupby('Vendedor')['Valor_Total'].mean().sort_values(
    ascending = False
)) # Maior: Alice

# Parte 4
df['Mês'] = df['Data'].dt.month
print(df.groupby('Mês')['ID_Venda'].count().sort_values(
    ascending = False
))
# Melhor mês: Março
# Pior mês: Maio
df['Dia da semana'] = df['Data'].dt.day_name()
print(df.groupby('Dia da semana')['ID_Venda'].count().sort_values(
    ascending = False
)) # Mais vendas na quarta-feira

# Parte 5
print(df.groupby('Produto')['Quantidade'].sum().sort_values(
    ascending = False
)) # Webcam foi o produto mais vendido
print(df.groupby('Produto')['Valor_Total'].sum().sort_values(
    ascending = False
)) # Notebook foi o que mais faturou
print(df.groupby('Cidade')['Valor_Total'].sum().sort_values(
    ascending = False
)) # Salvador foi a cidade que mais faturou 
print(df.groupby('Cliente')['Quantidade'].sum().sort_values(
    ascending = False
)) # Paula foi a cliente que mais comprou em quantidade
print(df.groupby('Cliente')['Valor_Total'].sum().sort_values(
    ascending = False
)) # Bruno foi o cliente que mais gastou dinheiro na loja
print(df['Forma_Pagamento'].value_counts())  # Forma de pagamento mais utilizada foi o pix

# Parte 6
print(df[['Data', 'Cliente', 'Cidade', 'Produto', 'Quantidade', 'Valor_Total']].sort_values('Valor_Total', ascending = False))