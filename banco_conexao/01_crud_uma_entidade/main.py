# importa a biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)
        
        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar ao banco. {e}")

def cadastrar_pessoa(session, Pessoa):
    nome = input("Digite o nome do usuário: ").strip().title()
    email = input("Digite o e-mail do usuário: ").strip().lower()
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

    session.add(nova_pessoa)
    session.commit()

    print(f"Pessoa {nome} cadastrada com sucesso.")

def listar_pessoas(session, Pessoa):
    pessoas = session.query(Pessoa).all()

    print("\nPessoas cadastradas:\n")
    for pessoa in pessoas:
        print(f"ID: {pessoa.id_pessoa}")
        print(f"Nome: {pessoa.nome}")
        print(f"E-mail: {pessoa.email}")
        print(f"Data de nascimento: {pessoa.data_nascimento.strftime("%d/%m/%Y")}")
        print(f"{'-'*40}")

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()

    Pessoa = criar_tb_pessoa(engine, Base)

    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    while True:
        print(f"{'-'*20} CRUD DA SERPENTE {'-'*20}")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")
        print("3 - Alterar dados de uma pessoa")
        print("4 - Excluir uma pessoa")
        print("5 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                listar_pessoas(session, Pessoa)
                continue
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

    session.close()

if __name__ == "__main__":
    main()