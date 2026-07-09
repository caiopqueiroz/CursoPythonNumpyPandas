import numpy as np


# Criando um array
a = np.array([10, 20, 30, 40])
print(a)

# Criando um array bidimensional 
matriz = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])
print(matriz)

# Verificando a quantidade de linhas e colunas de um array
print(matriz.shape)

# Verificando a dimensão de um array
print(a.ndim)
print(matriz.ndim)

# Verificando a quantidade de elementos 
print(matriz.size)

# Verificando o tipo do elemento
matriz2 = np.array([
    [1.5, 2.5],
    [3.5, 4.5]
])
matriz3 = np.array([1, 2, 3.2])
print(matriz3.dtype)
print(matriz2.dtype)
print(matriz.dtype)

# Criando arrays especiais

# Array com 5 zeros 
print(np.zeros(5))

# Matriz (2, 3) apenas com zeros
print(np.zeros((2, 3)))

# Matriz (3, 2) apenas com o número 1
print(np.ones((3, 2)))

# Array com números de 0 a 4 com passo 1
print(np.arange(0, 5, 1))

# Array com 5 números equidistantes de 0 a 10
print(np.linspace(0, 10, 5))

# Ex 1:
array = np.array([
    5, 10, 15, 20
])
print(array.shape, array.size, array.dtype)

# Ex 2:
a = np.zeros((3, 2))
print(a.shape)

# Ex 3:
a = np.array([
    1, 
    2,
    3.5
])
print(a.dtype)

# Ex 4:
np.arange(0, 10, 2)
np.linspace(0, 10, 5)

# Desafio:
matriz = np.zeros((4, 5))
print(matriz)
print(matriz.shape, matriz.size, matriz.ndim, matriz.dtype)