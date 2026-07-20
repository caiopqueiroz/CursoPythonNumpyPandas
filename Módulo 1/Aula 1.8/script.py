import numpy as np 


notas = np.array([
    8.5, 6.0, 4.5, 9.2, 7.8, 5.5, 10.0, 3.8, 6.7, 8.1
])

# Conhecendo os dados - quantidade de alunos 
print(np.size(notas)) # São 10 alunos no total

# Maior nota 
print(np.max(notas)) # 10.0

# Menor nota
print(np.min(notas)) # 3.8

# Média da turma
print(np.mean(notas)) # 7.01

# Desvio padrão 
print(np.std(notas)) # 1.94

# Descobrindo os alunos aprovados 
total_aprovados = np.sum(notas >= 6) # 7
aprovados = notas[notas >= 6] 
print(total_aprovados, aprovados)

# Descobrindo os alunos reprovados 
total_reprovados = notas.size - total_aprovados # 3
reprovados = notas[~(notas >= 6)]
print(total_reprovados, reprovados)

# Aumentando em 0.5 ponto a nota dos alunos abaixo da média 
novas_notas = notas.copy()
novas_notas[novas_notas < 6] += 0.5
print(novas_notas)

# Classificando os alunos 
status = np.where(notas < 6, 'Reprovado', 'Aprovado')
print(status)

# Verificando qual o índice do aluno que teve a maior nota 
indice_maior = np.argmax(notas) # Índice 6 -> aluno 7

# Índice da menor nota
indice_menor = np.argmin(notas)
print(indice_maior, indice_menor) # Índice 7 -> aluno 8
print(notas[indice_maior], notas[indice_menor]) # 10.0 e 3.8

# Verificando quem ficou acima da média 
media = np.mean(notas)
acima_media = notas[notas > media]
quantidade_acima_media = np.sum(notas > media)
print(quantidade_acima_media, acima_media) # 5

# Montando um relatório final 
# Total de alunos: 10 
# Aprovados: 7
# Maior nota: 10.0
# Menor nota: 3.8
# Valor da média: 7.01
# Quantidade acima da média: 5
# Desvio padrão: 1.94 (médio-baixo)
