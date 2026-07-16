import numpy as np 


# Exibindo apenas idades maiores ou iguais a 18 
idades = np.array([15, 18, 22, 16, 30, 40, 12])
print(idades[idades >= 18])

# Exibindo apenas notas maiores ou iguais a 6
notas = np.array([4, 6, 8, 3, 10, 7])
print(notas[notas >= 6])

# Exibindo apenas idades entre 18 e 30 (inclusive)
idades = np.array([12, 15, 18, 21, 30, 45])
print(idades[(idades >= 18) & (idades <= 30)])

# Utilizando o operador 'ou', para exibir idades menores que 18 e maiores que 40
print(idades[(idades < 18) | (idades > 40)])

# Utilizando o operador 'não'
print(idades[~(idades >= 18)])

# Modificando apenas parte do array
salarios = np.array([1800, 2500, 3200, 1500, 5000])
salarios[salarios < 2000] = salarios[salarios < 2000] * 1.1
print(salarios)

# Substituindo números negativos por 0
a = np.array([-3, 5, -2, 8, -1])
a[a < 0] = 0
print(a)

# Usando a função np.where()
idades = np.array([12, 18, 25, 16])
print(np.where(idades >= 18, 'Maior', 'Menor'))

notas = np.array([4, 5, 7, 9])
print(np.where(notas >= 6, 'Aprovado', 'Reprovado'))

# Contando elementos 
idades = np.array([10, 25, 18, 30, 15])
# idades > 20 retorna um array apenas com elementos booleanos, nesse caso, o papel da função np.sum() é contar o número de valores True e exibir a quantidade em que apareçeram
print(np.sum(idades > 20))

# Verificando condições - há algum?
a = np.array([10, -1, 2, -6])
print(np.any(a < 0)) # Retorna True porque há números negativos no array

# Todos são?
print(np.all(a < 0)) # Retorna Falsee porque não há só números negativos

# Ex 1:
a = np.array([5, 10, 15, 20])
print(a[a > 10])

# Ex 2:
print(a[a <= 10])

# Ex 3:
a = np.array([8, 12, 18, 25, 30])
print(a[(a >= 10) & (a < 30)])

# Ex 4:
a = np.array([-5, 3, -2, 8, 9])
a[a < 0] = 100
print(a)

# Desafio:
notas = np.array([4.5, 6.0, 7.8, 5.9, 9.2, 3.7])
print(notas[notas >= 6])
print(notas[~(notas >= 6)])
print(np.sum(notas >= 6))
print(np.all(notas >= 6))
resultado = np.where(notas >= 6, 'Aprovado', 'Reprovado')
print(resultado)