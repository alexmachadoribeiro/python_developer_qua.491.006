import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # setando os valores do usuário
    print("Insira os dados do usuário:\n")

    # métodos set
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.telefone = input("Informe o telefone: ").strip()
    usuario.endereco = input("Informe o endereço: ").strip().title()

    limpar()

    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ da empresa: ").strip()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip().title()

    limpar()

    # chamando os métodos get
    print("Dados do usuário:\n")
    print(f"Nome do usuário: {usuario.nome}")
    print(f"CPF do usuário: {usuario.cpf}")
    print(f"Telefone do usuário: {usuario.telefone}")
    print(f"Endereço do usuário: {usuario.endereco}")
    print("\nDados da empresa:\n")
    print(f"Nome da empresa: {empresa.nome_fantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Telefone da empresa: {empresa.telefone}")
    print(f"Endereço da empresa: {empresa.endereco}")

if __name__ == "__main__":
    main()