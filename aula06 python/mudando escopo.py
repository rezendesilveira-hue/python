# Escopo Global
nome = 'Fernanda' 

def minha_funcao():
		global nome # Informando que queremos utilizar a variavel global
        nome = 'Carlos' # Ele irá alterar a variável "nome" global
        print(nome) # Carlos

minha_funcao() # Carlos
print(nome) # Carlos