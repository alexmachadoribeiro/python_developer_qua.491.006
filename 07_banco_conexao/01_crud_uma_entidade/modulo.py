from datetime import datetime
import os
import pandas as pd

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome do usuário: ").strip().title()
        email = input("Digite o e-mail do usuário: ").strip().lower()
        pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"{email}")).all()

        if email in [pessoa.email for pessoa in pessoas]:
            print("E-mail já cadastrado.")
        else:
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

def alterar_dados(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email = ""
    nova_data_nascimento = ""

    try:
        print("Escolha o campo para pesquisar a pessoa a ter os dados alterados:")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Retornar")
        opcao = input("Escolha o campo que deseja pesquisar: ").strip()
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                print("Opção inválida")
        if pessoa:
            while True:
                print("Qual campo deseja alterar:\n")
                print(f"ID {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
                print("4 - Finalizar")
                campo = input("Informe o campo que deseja alterar: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        print(f"Nome a ser cadastrado: {novo_nome}.")
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if email in [pessoa.email for pessoa in pessoas]:
                            print("E-mail já cadastrado.")
                        else:
                            print(f"E-mail a ser cadastrado: {novo_email}.")
                        continue
                    case "3":
                        nova_data_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        print(f"Data de nascimento a ser cadastrada: {nova_data_nascimento}.")
                        continue
                    case "4":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        nova_data_nascimento = datetime.strptime(nova_data_nascimento, "%d/%m/%Y").date() if nova_data_nascimento != "" else pessoa.data_nascimento
                        break
                    case _:
                        print("Campo inexistente")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.data_nascimento = nova_data_nascimento

            session.commit()

            print("Pessoa cadastrada com sucesso!")
        else:
            print("Pessoa não encontrada.")
    except Exception as e:
        print(f"Não foi possível alterar. {e}.")

def excluir_pessoa(session, Pessoa):
    id_pessoa = ""
    email = ""
    pessoa = ""

    print("Escolha o campo que deseja pesquisar a pessoa a ser excluída.")
    print("1 - ID")
    print("2 - E-mail")
    print("3 - Desistir")
    opcao = input("Informe o campo que deseja pesquisar: ").strip()
    limpar()
    match opcao:
        case "1":
            id_pessoa = input("Informe o ID da pessoa a ser excluída: ").strip()
            pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
        case "2":
            email = input("Informe o e-mail da pessoa a ser excluída: ").strip().lower()
            pessoa = session.query(Pessoa).filter_by(email=email).first()
        case "3":
            return ""
        case _:
            print("Opção inválida.")

    if pessoa:
        limpar()
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"E-mail: {pessoa.email}")
        print(f"Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
        print("1 - Sim")
        print("2 - Não")
        excluir = input("Tem certeza de que deseja excluir?").strip()
        match excluir:
            case "1":
                session.delete(pessoa)
                session.commit()

                print("Pessoa excluída com sucesso.")
            case "2":
                pass
            case _:
                print("Opção inválida.")
    else:
        print("Pessoa não encontrada.")

# NOTE: para essa função funcionar, precisa do pandas e do openpyxl instalados na .venv
def exportar_excel(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()
        # Cria uma lista de dicionários com os dados das pessoas
        dados = [
            {
                "ID": pessoa.id_pessoa,
                "Nome": pessoa.nome,
                "E-mail": pessoa.email,
                "Data de nascimento": pessoa.data_nascimento.strftime("%d/%m/%Y")
            }
            for pessoa in pessoas
        ]
        df = pd.DataFrame(dados)
        df.to_excel("01_crud_uma_entidade/planilhas_exportadas/pessoas.xlsx", index=False)
        print("Dados exportados para pessoas.xlsx com sucesso.")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")