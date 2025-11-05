dia = int(input('Digite o dia: '))


if dia > 31 or dia < 0:
        print('Data invalida ')
else:
    mes = int(input('Digite o mês: '))
if mes > 12 or mes < 0:
     print('Data invalida ')  
else:
    ano = int(input('Digite o ano: '))
if ano > 9999 or ano < 0:
       print('Data invalida ')
else:
    print(f'A data que digitou é: {dia}/{mes}/{ano}')
