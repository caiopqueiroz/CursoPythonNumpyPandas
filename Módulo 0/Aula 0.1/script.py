# Criando um vínculo entre as listas (2 etiquetas apontando para o mesmo objeto)
a = [1, 2, 3]
b = a # Vínculo
a.append(4)
print(b)

# Criando um vínculo e depois desfazendo 
a = [5, 6]
b = a # Vínculo
a = [50, 60] # Desfazendo o vínculo
print(a, b)

# Exercício 1: 
a = [1, 2]
b = a 
b.append(3)
print(a)
# [1, 2, 3] porque existe uma única lista que está sendo apontada pelas variáveis a e b.

# Exercício 2:
a = [1, 2]
b = a
b = [5, 6]
print(a)
# [1, 2] porque com a atribuição de [5, 6] à variável b, a etiqueta a continua apontando para a mesma lista de antes.

# Exercício 3:
x = [10]
y = x
x.append(20)
x = [30]
print(y)
# [10, 20] porque a etiqueta y continua vinculada à lista criada pela etiqueta x, mesmo que ela agora aponte para [30].

# Exercício 4:
a = [1]
b = a
c = b
c.append(2)
b = [10]
print(a, b, c)
# As etiquetas a e c irão exibir [1, 2] porque ainda continuam apontando para a primeira lista. Já a etiqueta b passou a pontar para uma nova lista [10].