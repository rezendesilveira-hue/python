def ler_dados_arquivo():
    arquivo = open ('dados.txt' , 'r')
    numeros_string = arquivo.read()
    arquivo.close()
    numeros = numeros_string.split(';')
    return int(numeros[0], int(numeros[1]))
    
def soma(a, b):
    return a + b


num1, num2 = ler_dados_arquivo()
print(soma(num1, num2))