import pandas as pd


# Criando um data frame de clientes 
clientes = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nome': ['Ana', 'João', 'Maria']
})

# Criando um data frame de pedidos
pedidos = pd.DataFrame({
    'ID_Cliente': [1, 2, 1, 4],
    'Produto': ['Mouse', 'Monitor', 'Teclado', 'Fone de ouvido'],
    'Valor': [80, 900, 150, 20]
})

# Unindo os dois bancos de dados com merge() - o novo banco está sendo organizado com base nas colunas de ID presentes em ambos, por isso Maria não aparece uma vez que seu ID só é visto no df de clientes
df = pd.merge(
    clientes,
    pedidos,
    left_on = 'ID',
    right_on = 'ID_Cliente'
)
print(df)

# Usando o parâmetro how = 'left' para unir de forma a mostrar todos os ID's presentes do banco dos clientes, mesmo que não tenham nenhum pedido 
print(pd.merge(
    clientes,
    pedidos,
    left_on = 'ID',
    right_on = 'ID_Cliente',
    how = 'left'
))

# Fazendo o mesmo, mas agora com how = 'right' para mostrar os ID's no banco dos pedidos, que 'entra' à direita
print(pd.merge(
    clientes,
    pedidos,
    left_on = 'ID',
    right_on = 'ID_Cliente',
    how = 'right'
))

# Mantendo todas as linhas de ambas os df's com how = 'outer'
print(pd.merge(
    clientes,
    pedidos,
    left_on = 'ID',
    right_on = 'ID_Cliente',
    how = 'outer'
))

# Se ambas as colunas de identificação possuem o mesmo nome em ambos os data frames, o código pode ser escrito da forma: 
# pd.merge(
#     clientes,
#     pedidos,
#     on = 'ID'
# )

# Unindo dois bancos de dados usando o índice como coluna chave com join() - nesse caso, a união fica equivocada
print(clientes.join(pedidos))

# Empilhando tabelas sem usar uma coluna chave com concat() - o parâmetro axis = 0 indica que queremos empilhar as linhas, caso quiséssemos empillhar colunas, usaríamos axis = 1
vendas_janeiro = pd.DataFrame({
    'Produtos': ['Mouse', 'Teclado'],
    'Valor': [90, 120]
})
vendas_fevereiro = pd.DataFrame({
    'Produtos': ['Mouse', 'Monitor'],
    'Valor': [85, 1100]
})
print(
    pd.concat([vendas_janeiro, vendas_fevereiro],
              axis = 0,
              ignore_index = True)
)

# Ex 1:
print(pd.merge(
        clientes,
        pedidos,
        left_on = 'ID',
        right_on = 'ID_Cliente'
    ))

# Ex 2:
print(pd.merge(
    clientes, 
    pedidos,
    how = 'left',
    left_on = 'ID',
    right_on = 'ID_Cliente'
))
# Maria aparece assim porque ela está presente no df de clientes (que está à esquerda), mas não apresenta nenhum pedido no outro banco 

# Ex 3:
A = pd.DataFrame({
    'Número': [1, 2]
})
B = pd.DataFrame({
    'Número': [3, 4]
})
print(pd.concat([A, B], axis = 0,
                ignore_index = True))

# Ex 4:
nomes = pd.DataFrame({
    'Nome': ['Ana', 'João']
})
idades = pd.DataFrame({
    'Idade': [20, 25]
})
print(pd.concat([nomes, idades], axis = 1))

# Desafio:
clientes = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nome': ['Ana', 'João', 'Maria', 'Lucas']
})
pedidos = pd.DataFrame({
    'ID': [1, 2, 2, 5],
    'Valor': [100, 200, 300, 400]
})
print(pd.merge(
    clientes,
    pedidos,
    how = 'left',
    on = 'ID'
)) # left join - Maria e Lucas geraram registros NaN na coluna valor uma vez que essas pessoas não compraram nada  
print(pd.merge(
    clientes,
    pedidos,
    how = 'outer',
    on = 'ID'
)) # outer join - O pedido no valor de 400 gerou NaN na coluna Nome porque não existe um cliente com o ID que realizou esse pedido

