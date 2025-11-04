#Tendo como dados de entrada um arquivo em Gigabytes, 
# construa um algoritmo que faça a conversão para Megabytes e Kilobytes, 
# usando as seguintes fórmulas:

#Para Megabytes: Gigabytes * 1024
#Para Kilobytes: Gigabytes * 1024 * 1024
#Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
giga = float(input('Digite a quantidade de gigabytes: '))
mega = giga * 1024
kilo = giga *124 *1024
print(f'A quantidade de megabytes tem dentro é: {mega :.2f}')
print(f'A quantidade de Kilobytes que tem dentro é: {kilo :.2f}')