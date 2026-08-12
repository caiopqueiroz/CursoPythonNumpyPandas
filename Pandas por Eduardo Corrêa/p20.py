# Salvando o conteúdo de um df em um arquivo csv 
import pandas as pd 


dados = {
    'codigo': [1001, 1002, 1003, 1004, 1005],
    'nome': ['Leite', 'Café', 'Biscoito', 'Chá', 'Torradas']
}
produtos = pd.DataFrame(dados)

# Usando a função to_csv() para exportar o banco de dados - o nome do arquivo criado será produtos.csv
# O parâmetro index = False é muito importante para não bagunçar os índices quando for feita uma nova leitura a partir do arquivo csv criado
produtos.to_csv(
    'Pandas por Eduardo Corrêa/produtos.csv',
    sep = ';',
    index = False 
)
