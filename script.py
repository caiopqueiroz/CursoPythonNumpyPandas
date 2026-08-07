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


