# Gerando estatísticas sobre colunas e linhas de um banco 
import pandas as pd


# Criando um df
notas = pd.DataFrame({
    'A1': [9.8, 7.2, 8],
    'A2': [5.3, 4, 3.5],
    'A3': [5.5, 8.1, 7.2],
    'A4': [7.0, 7.5, 6.5]
},
index = ['P1', 'P2', 'P3'])
print(notas)

# Gerando a média de cada aluno, ou seja, calculando a média de cada coluna 
print(notas.mean())

# Exibindo a maior nota de cada aluno 
print(notas.max())

# Usando o parâmetro axis = 1 para calcular a média por linha, ou seja, será então calculada a média de nota dos alunos em cada prova 
print(notas.mean(
    axis = 1
))

# Da mesma forma, mostrando qual foi a maior nota obtida por um aluno em cada uma das 3 provas
print(notas.max(
    axis = 1
))