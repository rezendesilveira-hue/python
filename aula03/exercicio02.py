nota1 = input('Digite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')
nota3 = input('Digite a terceira nota: ')

media = (nota1 + nota2 + nota3) /3

if media >= 6:
    print('Aprovado')
elif media >= 4:
    print('Recuperação') 
else:
    print('Reprovado')       