pessoas = {}

while True:
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    peso = float(input('Digite o peso: '))
    
    pessoas[nome] = [idade, altura, peso] #lista dentro do dicionario
    resp = input('Deseja continuar?  [S/N]')
    if resp.upper() == 'N':
        break
print('Nomes cadastrados: ')

for pessoas, dados in pessoas.items():
    print(f'- Nome: {pessoas} | idade: {dados[0]} Anos | Peso: {dados[1]} KG | Altura: {dados[2]} M  ')