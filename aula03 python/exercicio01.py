#Crie um dicionário com 3 frutas e seus preços. 
#Exiba o preço de uma fruta específica.
#Adicione mais uma fruta ao dicionário.
#Atualize o preço de uma fruta já existente.
frutas = {
    'Maça' : 4.50,
    'Melancia' : 5.99,
    'Laranja' : 6.80
    
}
print(f'O preço da Maça é: R$ {frutas['Maça']}')
frutas['Uvas'] = 7.80
print(frutas)
frutas['Laranja'] = 12.90
print(frutas)

