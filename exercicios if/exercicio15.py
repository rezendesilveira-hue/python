lado1 = float(input('Digite o primeiro lado do trinagulo: '))
lado2 = float(input('Digite o segundo lado do trinagulo: '))
lado3 = float(input('Digite o terceiro lado do triangulo: '))

if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('O triangulo é Equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triangulo é Isósceles')
elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3:
    print('O triangulo é Escaleno')