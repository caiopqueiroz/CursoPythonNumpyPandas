import pandas as pd
import numpy as np 


dados = pd.Series([0, 1, 2, 3], index = ['A', 'B', 'C', 'D'])
dados.index = [100, 101, 102, 103]
print(dados.shape, dados.dtypes)

notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])
alunos = pd.Series(
    ['Bob', 'Dayse', 'Bill', 'Cris', 'Jimi'],
    index = ['M02', 'M05', 'M13', 'M14', 'M19']
)
print(notas)
print(alunos)

# Definindo e exibindo propriedades básicas das Series 
alunos.name = 'alunos'
alunos.index.name = 'matrículas'

print('-'*20)
print(alunos)
print('-'*20)
tamanho = alunos.size
dados = alunos.values
rotulos = alunos.index
alunos_tipo = type(alunos)
alunos_dtype = alunos.dtype
alunos_index_dtype = alunos.index.dtype

print('Número de elementos: ', tamanho)
print('Vetor de dados: ', dados)
print('Vetor de rótulos: ', rotulos)
print('Tipo (de acordo com o Python): ', alunos_tipo)
print('Dtype da Series: ', alunos_dtype)
print('Dtype do vetor de rótulos: ', alunos_index_dtype)

print(alunos['M02']) # Indexação tradicional
print(alunos['M02':'M14']) # Indexação por fatiamento
print(alunos[
    (alunos != 'Bob') & 
    (alunos != 'Bill')
    ]) # Indexação booleana

# Exibindo apenas os alunos com nota igual ou superior a 7 
alunos.index = [0, 1, 2, 3, 4]
print(alunos[notas[notas >= 7].index])

# Testando se determinados índices ou valores estão presentes em uma Series
alunos.index = ['M02', 'M05', 'M13', 'M14', 'M19']
print('M99' in alunos)
print('M02' in alunos)
# Usando a função isin() para verificar valores
print(alunos.isin(['Bob']))

# Inserindo elementos em uma Series 
alunos['M55'] = 'Rakesh'

# Alterando elementos de uma Series
alunos[['M13', 'M14', 'M19']] = ['Billy', 'Cristy', 'Jimmy']

# Removendo o aluno Bob da Series com a função drop() - se remove pelo rótulo 
alunos.drop(
    'M02',
    inplace = True
)

print(alunos)

# Fazendo operações numéricas com Series 
print(notas * 2)
print(notas - 5)
print(notas[notas < 6] + 1.5) # Somando + 1.5 nas notas menores que 6
print(notas[notas >= 9]) # Exibindo notas maiores ou iguais a 9

# Criando mais Series numéricas para operações 
serie1 = pd.Series([2, 4, 6])
serie2 = pd.Series([1, 3, 5])

# Fazendo operações entre duas Series 
print(serie1 * serie2)
print(np.sqrt(serie1) - serie2 ** 2) # Raiz da serie1 subtraída da serie2 elevada ao quadrado