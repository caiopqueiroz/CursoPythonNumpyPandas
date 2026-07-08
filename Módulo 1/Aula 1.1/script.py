# Multiplicando uma lista de valores por 2
numeros = [10, 20, 30, 40, 50, 60, 70, 80]
dobros = [numero * 2 for numero in numeros]
print(numeros, dobros)

# Ex 1:
# Porque as listas de Python foram definidas com objetivos diferentes dos arrays em NumPy. Uma lista pode gerar vários atalhos para programação de modo geral, mas, quando o assunto é eficiência para computação numérica, arrays são os mais indicados.

# Ex 2:
# Array NumPy, porque uma lista guardaria informações desnecessárias sobre os elementos, como o tipo do objeto, por exemplo, que é igual para todos. Além disso, para computação científica, haveria muito ganho de performace ao usar um array, que é melhor otimizado para fazer operações numéricas.

# Ex 3:
# O código B, porque nele acontece uma operação diretamente na lista, o que só é possível se ela estiver vetorizada.

# Ex 4:
# Porque ele contém menos informações sobre cada elemento, e então exige menos do computador

# Ex 5:
# Para esse caso, a melhor opção seria com certeza utilizar um array em NumPy para coletar esses dados. Isso porque, todos são números reais, assim, um vetor homogêneo otimizaria a capacidade do computador responsável. Além disso, trabalhando com arrays, uma lista vetorizada, ainda seria possível realizar operações numéricas diretamente com os objetos. 