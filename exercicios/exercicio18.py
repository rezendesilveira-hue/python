 #Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
 # velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
 # de download do arquivo usando este link (em minutos).
 

tamanho_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade_net = float(input('Digite a velocidade da internet: '))
formula = tamanho_arquivo * 8
tempo = formula / velocidade_net  
tempo_segundos = tempo / 60
print(f'O tempo em minutos é: {tempo_segundos :.2f}')

