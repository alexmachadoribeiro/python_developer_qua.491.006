class Pessoa:
    # construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"Olá, meu nome é {self.nome} e tenho {len(self)} anos."
    
    def __len__(self):
        return self.idade
    
    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso.")