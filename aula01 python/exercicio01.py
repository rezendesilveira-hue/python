qtde_vogal = 0
texto = input('Digite o seu texto: ')

for vogal in texto:
    if vogal in ['a', 'e', 'i', 'o', 'u']:
        qtde_vogal += 1 

    #.lower serve para unificar as letras entre maisucla e minuscula
    #vogal = vogal.lower()
    #if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u' :
        #qtde_vogal += 1    
print(f'A quentidade de vogal é: {qtde_vogal}')