num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

print("\nNúmeros em ordem decrescente:")

# CASO 1: num1 > num2 > num3
if num1 >= num2 and num2 >= num3:
    print(f'{num1}')
    print(f'{num2}')
    print(f'{num3}')

# CASO 2: num1 > num3 > num2
elif num1 >= num3 and num3 >= num2:
    print(f'{num1}')
    print(f'{num3}')
    print(f'{num2}')

# CASO 3: num2 > num1 > num3
elif num2 >= num1 and num1 >= num3:
    print(f'{num2}')
    print(f'{num1}')
    print(f'{num3}')

# CASO 4: num2 > num3 > num1
elif num2 >= num3 and num3 >= num1:
    print(f'{num2}')
    print(f'{num3}')
    print(f'{num1}')

# CASO 5: num3 > num1 > num2
elif num3 >= num1 and num1 >= num2:
    print(f'{num3}')
    print(f'{num1}')
    print(f'{num2}')

# CASO 6: num3 > num2 > num1 (ou qualquer outra combinação restante, incluindo números iguais)
else:
    print(f'{num3}')
    print(f'{num2}')
    print(f'{num1}')
