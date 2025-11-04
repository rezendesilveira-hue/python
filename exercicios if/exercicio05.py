nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print('======================')
    print('Aprovado')
    print('======================')
elif media == 10 :
    print('======================')
    print('Aprovado com distinção')
    print('======================')
else:
    print('======================')
    print('Reprovado')
    print('======================')