import PessoaFisica
import PessoaJuridica
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica.PessoaFisica(
        email="", telefone="", endereco="",
        nome="", cpf="", idade=0
    )
    empresa = PessoaJuridica.PessoaJuridica(
        email="", telefone="", endereco="",
        razao_social="", nome_fantasia="", cnpj=""
    )

    # input do usuário
    print("Informe os dados do usuário:\n")
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.cpf = input("Informe seu CPF: ").strip()
    usuario.idade = int(input("Informe sua idade: "))
    usuario.email = input("Informe seu e-mail: ").strip().lower()
    usuario.telefone = input("Informe seu telefone: ").strip()
    usuario.endereco = input("Informe seu endereco: ").strip()

    limpar()

    print("Informe os dados da empresa:\n")
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.email = input("Informe o e-mail da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip()

    limpar()

    # output
    print(usuario)
    print(empresa)

if __name__ == "__main__":
    main()