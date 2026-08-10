# Índices datetime
import pandas as pd


# Criando uma série com rótulos temporais 
dias = ['10/02/2019', '11/02/2019', '12/02/2019', '13/02/2019', '14/02/2019', '15/02/2019']
temperatura_maxima = [31, 35, 34, 28, 27, 27]
serie_temporal = pd.Series(
    temperatura_maxima,
    index = dias 
)

# Convertendo o tipo do rótulo para datetime usando to_datetime(format = '%d/%m/%Y')
serie_temporal.index = pd.to_datetime(
    serie_temporal.index,
    format = '%d/%m/%Y'
)

# Fazendo uma operação entre datas 
print(serie_temporal.index[-1] - serie_temporal.index[0])
