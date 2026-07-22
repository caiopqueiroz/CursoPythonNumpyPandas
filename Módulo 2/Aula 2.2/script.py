import pandas as pd


# Lendo um arquivo csv
df = pd.read_csv('Módulo 2/Aula 2.2/dados.csv')
print(df)

# Lendo um arquivo csv usando o separador ponto e vírgula
df_pontoevirgula = pd.read_csv('Módulo 2/Aula 2.2/dados_pv.csv', sep = ';')
print(df_pontoevirgula)

# Lendo um arquivo csv que não possui cabeçalho usando o parâmetro header
df_semcabecalho = pd.read_csv('Módulo 2/Aula 2.2/dados_sc.csv', header = None)
print(df_semcabecalho)

# Definindo o nome das colunas com o parâmetro names
df_cabecalho = pd.read_csv('Módulo 2/Aula 2.2/dados_sc.csv',
                           header = None,
                           names = ['Nome', 'Idade', 'Nota'])
print(df_cabecalho)

# Importando apenas algumas colunas com usecols
# df = pd.read_csv('vendas.csv', usecols = ['Produto', 'Preço'])

# Lendo um arquivo xlsx (excel)
# df = pd.read_excel('vendas.xlsx')

# Importando apenas uma planilha com sheet_name
# df = pd.read_excel('vendas.xlsx', sheet_name = 'Janeiro')

# Criando um novo csv depois de modificar os dados
df['Nota'] -= 2.5
df.to_csv('Módulo 2/Aula 2.2/resultado.csv', index = False)

# Criando um novo excel depois de modificar os dados
# df.to_excel('resultado.xlsx', index = False)

# Ex 1:
# read_csv()

# Ex 2:
# index = False

# Ex 3:
# df = pd.read_csv('funcionarios.csv', sep=';')

# Ex 4:
# df = pd.read_csv('empresa.csv', usecols = ['Nome', 'Salário'])

# Desafio:
# df = pd.read_excel('vendas_2025.xlsx', sheet_name = 'Março')
# print(df)
# df.to_csv('marco.csv', index = False)