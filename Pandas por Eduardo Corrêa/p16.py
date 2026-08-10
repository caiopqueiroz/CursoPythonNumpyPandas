import pandas as pd
# Usando alguns parâmetros da função read_csv()


notas = pd.read_csv(
    'Pandas por Eduardo Corrêa/notas.csv',
    names = ['matricula', 'nota1', 'nota2'],
    sep = ';'
)
print(notas)

print(notas[notas['nota1'] > 7])

print(notas[
    (notas['nota1'] > 7) & (notas['nota2'] > 7)
])
