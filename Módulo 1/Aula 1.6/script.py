import numpy as np


# Criando um array
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Somando todos os elementos 
print(np.sum(a))

# Calculando a média de todos os elementos 
print(np.mean(a))

# Mostrando o maior e menor valor 
print(np.max(a))
print(np.min(a))

# Mostrando o desvio padrão
print(np.std(a))

# Mostrando a variança
print(np.var(a))

# Utilizando o parâmetro axis 
# axis=0 retorna os valores por coluna
# axis=1 retorna os valores por lina 

# Somando os elementos de cada coluna 
print(np.sum(a, axis=0))

# Somando os elementos de cada linha
print(np.sum(a, axis=1))

# Calculando a média por coluna
print(np.mean(a, axis=0))

# Mostrando o maior valor de cada linha
print(np.max(a, axis=1))

# Mostrando o índice do maior e menor valor 
b = np.array([5, 8, 2, 15, 9])
print(np.argmax(b))
print(np.argmin(b))

# Utilizando argmax e argmin com o parâmetro axis
print(np.argmax(a, axis=0))
print(np.argmin(a, axis=1))

# Ex 1:
a = np.array([
    [1, 2],
    [3, 4]
])
print(a.sum())
print(np.sum(a))

# Ex 2:
print(a.sum(axis=0))
print(np.sum(a, axis=0))

# Ex 3:
print(np.sum(a, axis=1))

# Ex 4:
b = np.array([12, 8, 20, 15])
print(np.argmax(b), b.argmin())

# Desafio:
a = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])
print(np.mean(a), np.mean(a, axis=0), a.mean(axis=1), a.max(axis=0), np.min(a, axis=1), a.argmax())