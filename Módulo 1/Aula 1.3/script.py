import numpy as np 


# Criando um array 
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Criando um array (com 1 dimensão)
v = np.array([10, 20, 30, 40])

# Acessando elementos do vetor
print(v[0]) # 10
print(v[2]) # 30

# Acessando elementos usando índices negativos
print(v[-1]) # 40
print(v[-2]) # 30

# Acessando elementos de um array matriz (2 dimensões)
print(a[1, 2]) # 60
print(a[2, 1]) # 80

# Acessando uma linha
print(a[0]) # [10 20 30]

# Acessando uma coluna
print(a[:, 1]) # [20 50 80]

# Acessando recorte de um array vetor (1 dimensão)
# print(v[inicio:fim])
print(v[1:3]) # [20 30]

# Acessando recorte de um array matriz
# print(a[inicio:fim, inicio:fim])
print(a[0:2, 1:3])
print(a[1:, 1:])

# Criando uma visualização (mesmo espaço na memória)
# A matriz b será uma matriz com todas as linhas de a (:), porém apenas com os elementos da primeira coluna (0)
b = a[:, 0]

# Veja:
b[0] = 999
print(a) 
# Se alterarmos um elementos de b, a matriz a também será alterada

# Criando uma cópia
b = a[:, 0].copy()

# Ex 1:
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a[2, 1])

# Ex 2:
print(a[1, :])

# Ex 3:
print(a[:, 2])

# Ex 4:
print(a[1:, 0:2])

# Desafio:
a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])
print(a[2])
print(a[:, 1])
print(a[2, 2])
print(a[1:3, 1:3])
b = a[:, 3].copy()
print(b)