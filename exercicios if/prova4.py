vlr_salario = float(input('Digite o salário: '))
atraso = int(input('Digite o número de dias de atraso: '))
multa_total = 0
dias = 0

if atraso >5:
    dias = atraso - 5
    for total in range(dias):
        multa = vlr_salario * 0.02
        multa_total = multa_total + multa
        
    print(f'Salário: {vlr_salario}')
    print(f'Dias de atraso: {dias}')
    print(f'Multa diária: {multa_total}')
else:
    print('Não tem multa')


