# Necessidade: atualizar o lucro, a receita, os gastos, a lista de pedidos e de encomendas a cada nova pessoa que comprar

# Importando o dataframe 
import pandas as pd 
import numpy as np


df = pd.read_csv('dados_cookies.csv')
gastos = pd.read_csv('dados_gastos_cookies.csv')

# Criando o restante das colunas 
df['Valor_50g'] = df['Quantidade_50g'] * 5
df['Valor_100g'] = df['Quantidade_100g'] * 8
df.loc[
    df['Quantidade_50g'] >= 3,
    'Desconto'
] += 3
df['Valor_total'] = df['Valor_50g'] + df['Valor_100g'] - df['Desconto']
df['Créditos'] = df['Valor_pago'] - df['Valor_total']
df['Data'] = pd.to_datetime(df['Data'])

# Calculando estatísticas 
receita = df['Valor_pago'].sum()
gasto = gastos['Valor_pago'].sum()
lucro = receita - gasto
# print(lucro)

# Verificando créditos - da Érica
# print(df.loc[
#    df['Cliente'] == 'Érica Mansur',
#    'Créditos'
# ].sum())

# Programa 
print('Bem-vindo')
comando = 1
while comando != 5:
    print('\nEscolha uma opção:\n1 ) Ver receita/gasto/lucro\n2 ) Verificar créditos\n3 ) Ver quantidade de cookies vendida\n4 ) Verificar encomendas pendentes\n5 ) Sair')
    comando = int(input('Digite aqui: '))
    
    if comando == 1:
        print(f'\nReceita: R${receita:.2f}\nGasto: R${gasto:.2f}\nLucro total: R${lucro:.2f}')

    if comando == 2:
        cliente = str(input('\nNome do cliente: ')).title().strip()
        creditos = df.loc[
            df['Cliente'] == cliente,
            'Créditos'
        ].sum()
        print(f'Total de créditos: {creditos}')

    if comando == 3:
        quantidade_50g = df['Quantidade_50g'].sum()
        quantidade_100g = df['Quantidade_100g'].sum()
        print(f'\n50g: {quantidade_50g} unidades\n100g: {quantidade_100g} unidades')
    
    if comando == 4:
        df_pendente = df[df['Situação'] == 'Pendente']
        if not df_pendente.empty:
            print()
            print(df_pendente[['Cliente', 'Quantidade_50g', 'Quantidade_100g']])
        else:
            print('\nNenhuma encomenda pendente')