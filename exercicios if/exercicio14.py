nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media <= 10 and media >= 9.0:
    print(f'{media} conceito A')
    print('Aprovado')
elif media < 9.0 and media >= 7.5:
    print(f'{media} Conceito B')
    print('Aprovado')
elif media < 7.5 and media >= 6.0:
    print(f'{media} Conceito C')
    print('Aprovado')
elif media < 6.0 and media >= 4.0:
    print(f'{media} Conceito D')
    print('Reprovado')
elif  media < 4.0 and media >= 0:
    print(f'{media} Conceito E')
    print('Reprovado')