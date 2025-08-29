from datetime import datetime
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome do usuário: ").strip().title()
        email = input("Digite o e-mail do usuário: ").strip().lower()
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

        nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

        session.add(nova_pessoa)
        session.commit()

        print(f"Pessoa {nome} cadastrada com sucesso.")
    except Exception as e:
        print(f"Não foi possível cadastrar pessoa. {e}.")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("\nPessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}")
    except Exception as e:
        print(f"Não foi possível listar pessoas. {e}.")

def pesquisar_pessoas(session, Pessoa):
    print("Filtrar pessoas por campo:")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-mail")
    print("4 - Data de nascimento")
    print("5 - Retornar")
    campo = input("Escolha o campo a ser pesquisado: ").strip()
    limpar()
    match campo:
        case "1":
            valor = input("Digite o ID para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa.like(f"{valor}")).all()
        case "2":
            valor = input("Digite o nome para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o e-mail para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a data de nascimento (dd/mm/aaaa) para buscar: ").strip()
            data_nascimento = datetime.strptime(valor, "%d/%m/%Y").date()
            pessoas = session.query(Pessoa).filter(Pessoa.data_nascimento == data_nascimento).all()
        case "5":
            pass
        case _:
            print("Campo inexistente.")

    limpar()
    print("\nResultado da pesquisa:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
            print(f"{'-'*40}")
    else:
        print("Nenhuma pessoa foi encontrada.")