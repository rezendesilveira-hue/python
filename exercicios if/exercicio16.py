vlr1 = float(input('Digite o valor de a: '))

if vlr1 != 0:
    vlr2 = float(input('Digite o valor de b: '))
    vlr3 = float(input('Digite o valor de c: '))
    delta = (vlr2 **2) - (4 * vlr1 * vlr3)
    if delta < 0:
        print(f'{delta} Não possui raizes reais')
    elif delta == 0:
        print(f'{delta} Possui apenas uma raiz real')
    elif delta > 0:
        print(f'{delta} Possui 2 raizes reais')
else:
    print ('Programa encerrado número zero não possui raizes') 


