# classe
class Pessoa:
    # atributos
    nome = "Alex Machado"
    idade = 40
    telefone = "(61) 98765-4321"
    cpf = "123.456.789-12"
    email = "alex@gmail.com"

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}.")
    
# programa principal
if __name__ == "__main__":
    # instanciar classe
    usuario = Pessoa()

    # objeto se apresenta
    usuario.apresentar()