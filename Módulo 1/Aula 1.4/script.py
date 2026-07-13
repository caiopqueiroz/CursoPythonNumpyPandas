import numpy as np 


# Operações com escalares
a = np.array([10, 20, 30, 40])
print(a + 5)
print(a - 10)
print(a * 2)
print(a / 10) # Resultado sempre float 
print(a // 10) # Resultado inteiro
print(a ** 2)
print(np.sqrt(a))

# Operações entre arrays 
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a * b) # Importante: não é multiplicação de matrizes

# Valor absoluto
a = np.array([-2, -5, 3])
print(np.abs(a))

# Exponencial (calcula e^x para cada elemento)
a = np.array([1, 2])
print(np.exp(a))

# Comparações
a = np.array([10, 20, 30, 40])
print(a > 20) # Retorna um array com valores booleanos
print((a > 10) & (a < 40))
print((a < 15) | (a > 35))

# Operação in-place 
a *= 2 
print(a)

# Operação que não altera o array original
b = a * 2
print(b)
print(a)

# Ex 1:
a = np.array([2, 4, 6])
print(a * 3)

# Ex 2:
a = np.array([5, 10, 15])
print(a >= 10)

# Ex 3:
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a * b)

# Ex 4:
a = np.array([10, 20, 30, 40])
print((a >= 20) & (a < 40))

# Ex 5:
a = np.array([3, 6, 9, 12, 15])
print(a * 4)
print(a ** 2)
print(np.sqrt(a))
print(a % 3 == 0)
print((a >= 5) & (a <= 13))