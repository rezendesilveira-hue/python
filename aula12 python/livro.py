from typing import Optional
class Livro:
    def __init__(
            self,
            titulo: str, 
            editora: str, 
            ano: Optional[int], 
            autor: Optional[str]
            ):
        
        self.titulo = titulo
        self.editora = editora
        self.ano = ano
        self.autor = autor

livro1 = Livro('Biblia', 'Céu', 1000, 'Deus')
print(livro1.titulo)
print(livro1.ano)
print(livro1.autor)
