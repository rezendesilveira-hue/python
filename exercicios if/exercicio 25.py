pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para a vítima? ')
pergunta5 = input('Já trabalhou com a vítima?')
total_sim = 0


if pergunta1 == 'sim':
    total_sim = total_sim + 1
if pergunta2 == 'sim':
    total_sim = total_sim + 1
if pergunta3 == 'sim':
    total_sim = total_sim + 1
if pergunta4 == 'sim':
    total_sim = total_sim + 1
if pergunta5 == 'sim': 
    total_sim = total_sim + 1

if total_sim == 2:
    print('suspeito')
elif total_sim >=3 and total_sim <=4:
    print('Cumplice')
elif total_sim == 5:
    print('ASSASSINO')
