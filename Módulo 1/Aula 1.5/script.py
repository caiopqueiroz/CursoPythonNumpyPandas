import numpy as np 


# Somando 5 a todos os elementos de um vetor (exemplo de broadcasting)
a = np.array([10, 20, 30, 40])
print(a + 5)

# Broadcasting - Regra 1: Shapes iguais 
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(np.shape(a), np.shape(b)) # Ambos os vetores possuem shape = (3, )

# Regra 2: Um dos eixos vale 1 
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
print(a + b)

# Fazendo broadcasting por coluna
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([
    [100],
    [200]
])
print(a + b)
print(np.shape(b))

# Para o broadcasting funcionar, é necessário que: todos os eixos (x, y, z, ...) correspondentes possuem o mesmo tamanho ou um deles possua tamanho 1
# Exemplo: (2, 3) / (2, ) -> (1, 2) 
# Comparando: 3 - 2 Incompatível 
# 2 - 1 Compatível 
# Logo, não é possível realizar operações entre esses arrays com broadcasting 
a = np.zeros((2, 3))
b = np.ones(2)
#print(a + b)

# Exemplo: (3, 2) / (2, ) -> (1, 2)
# Comparando: 2 - 2 Compatível
# 3 - 1 Compatível 
# Logo, é possível realizar operações 
a = np.ones((3, 2))
b = np.zeros(2)
print(a + b)

# Ex 1:
a = np.array([10, 20, 30])
print(a + 100)

# Ex 2:
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([10, 20])
print(a + b)

# Ex 3:
a = np.ones((4, 5))
b = np.zeros(5)
print(a + b) # Funciona

# Ex 4:
a = np.zeros((3, 4))
b = np.ones(3)
#print(a + b) Não funciona

# Desafio:
a = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
b = np.array([
    [100],
    [200],
    [300]
])
print(a.shape)
print(b.shape)
print(a + b)