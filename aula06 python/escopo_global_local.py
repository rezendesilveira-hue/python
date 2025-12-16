# Escopo Global
nome = 'Fernanda' 

def minha_funcao():
		# Escopo Local
    nome = 'Carlos' # Aqui ele cria uma nova variável, e não altera a global
    print(nome) # Carlos

minha_funcao() # Carlos
print(nome) # Fernanda