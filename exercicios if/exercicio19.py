num = int(input('Digite um número inteiro, até 1000: '))

if num >= 1000:
    print('Digite um número menor')
else:
    c = int(num / 100)
    d = int((num % 100) /10)
    u = (num % 10)
if c > 1 and d > 1 and u > 1:
    print(f'{c} Centenas, {d} Dezenas e {u} unidades')
else:
    print(f'{c} Centena, {d} Dezena e {u} unidade')
