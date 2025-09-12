import Pessoa
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia a classe Pessoa
    usuario = Pessoa.Pessoa(
        nome="", 
        email="", 
        cpf="", 
        idade=0, 
        altura=0.0
    )

    # inputs
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.email = input("Informe seu email: ").strip().lower()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua idade: "))
    usuario.altura = float(input("Informe sua altura em metros: ").replace(",", "."))

    limpar()

    # output
    print(usuario)

if __name__ == "__main__":
    main()