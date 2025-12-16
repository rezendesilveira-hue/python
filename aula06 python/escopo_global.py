# Escopo Global
nome = 'Fernanda' 
print(nome) # Fernanda

def minha_funcao():
    # "nome" tem escopo global, logo pode ser acessado dentro de funções.
    print(nome) 

minha_funcao() # Fernanda
