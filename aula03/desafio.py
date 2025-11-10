ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 100) or (ano % 400 == 0):
    print('O ano e bisexto')
else:
    print('O ano não e bisexto')    