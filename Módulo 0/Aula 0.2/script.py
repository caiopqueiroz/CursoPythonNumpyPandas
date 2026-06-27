# Com variáveis comuns: é criado outro objeto e a etiqueta x passa a apontar para ele
x = 10 
x += 1 
print(x)

# Com listas: não é criado outro objeto, a etiqueta lista continua apontada para a mesma variável, que agora mudou
lista = [1, 2]
lista.append(3)

# Nesse exemplo, não é criada uma lista independente
a = [1, 2, 3]
b = a 

# Já nesses, são criadas cópias, desde que a lista contenha apenas elementos simples
b = a.copy()
b = list(a)
b = a[:]
b.append(4)
print(a, b)

# Exemplo de shallow copy, apenas a matriz externa é copiada, enquanto as listas internas continuam sendo referenciadas pelas duas etiquetas a e b
a = [
    [1, 2],
    [3, 4]
]
b = a.copy()
b[0].append(99)
print(a)

# Exemplo de deep copy, aqui as etiquetas apontam para matrizes diferentes com elementos internos indepedentes também
from copy import deepcopy
b = deepcopy(a)
b[0].append(99)
print(a, b)

# Ex 1:
a = [1, 2]
b = a.copy()
b.append(3)
print(a, b)

# Ex 2:
a = [
    [1],
    [2]
]
b = a.copy()
b[0].append(99)
print(a, b)

# Ex 3:
x = 5
y = x
y = 8
print(x)
# Porque a única etiqueta redirecionada foi y.

# Desafio:
a = [
    [1],
    [2]
]
b = a[:]
b.append([3])
b[0].append(99)
print('\n', a, b)