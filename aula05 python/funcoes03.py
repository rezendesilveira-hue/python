# Definindo Funções com Parâmetros Opcionais.
def saudacao(nome = "Usuário"):
    print(f"Olá, {nome}, seja bem-vindo!")

# Chamando a função sem argumento
saudacao() # Olá, Usuário, seja bem-vindo!

# Chamando a função com argumento
saudacao("Bruno") # Olá, Bruno, seja bem-vindo!