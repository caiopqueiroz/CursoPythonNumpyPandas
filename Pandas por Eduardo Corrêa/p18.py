# Importando uma planilha do excel como banco de dados 
import pandas as pd


capitais = pd.read_excel(
    'capitais.xlsx'
)

print(capitais)