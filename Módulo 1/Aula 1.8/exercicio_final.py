import numpy as np


temperaturas = np.array([
    22, 24, 21, 19, 26, 28, 30, 18, 20, 23, 25, 27, 29, 31
])

# Total de temperaturas
print(temperaturas.size) # 14

# Média
print(temperaturas.mean()) # 24.5 

# Maior e menor 
print(np.max(temperaturas), np.min(temperaturas)) # 31 e 18

# Total de dias com temperatura >= 25
print(np.sum(temperaturas >= 25))  # 7

# Temperatuas abaixo de 20 
print(temperaturas[temperaturas < 20])

# Criando um novo array
novas_temperaturas = temperaturas.copy()
novas_temperaturas[novas_temperaturas < 20] = 20 
print(novas_temperaturas)

# Criando um array com textos 
status = np.where(temperaturas >= 25, 'Quente', 
                  np.where(temperaturas > 20, 'Amena', 'Fria'))
print(status)
