# Verificando atributos e tipos de dados 
import pandas as pd


# Criando um df
dados = {
    'renda': [6.46, 1.5, 0, 2.57, 9.9, 6.22],
    'empregos': [1, 1, 0, 1, 2, 3],
    'sexo': ['F', 'M', 'F', 'M', 'M', 'F'],
    'escolaridade': ['pós-graduação', 'fundamental', 'médio', 'médio', 'superior', 'médio']
}
pme = pd.DataFrame(dados)
print(pme)

# Exibindo o nome de cada atributo (coluna) e seu tipo com a propriedade dtypes
print(pme.dtypes)