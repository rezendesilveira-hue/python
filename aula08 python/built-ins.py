import random as rd
import time

nomes = ['Ricardo' , 'Thiago' , 'Mellina']

print(nomes)
print('Escolhendo um nome...')
time.sleep(3)

nome_escolhido = rd.choice(nomes)
print(nome_escolhido)