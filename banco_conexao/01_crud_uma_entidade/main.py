# importa a biblioteca sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import entidades as ent
import modulo as md

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()
    Pessoa = ent.criar_tb_pessoa(engine, Base)
    Session = sessionmaker(bind=engine)
    session = Session()

    md.limpar()
    while True:
        print(f"{'-'*20} CRUD DA SERPENTE {'-'*20}")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")
        print("3 - Pesquisar pessoas")
        print("4 - Alterar dados de uma pessoa")
        print("5 - Excluir uma pessoa")
        print("6 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        md.limpar()
        match opcao:
            case "1":
                md.cadastrar_pessoa(session, Pessoa)
                continue
            case "2":
                md.listar_pessoas(session, Pessoa)
                continue
            case "3":
                md.pesquisar_pessoas(session, Pessoa)
                continue
            case "4":
                pass
            case "5":
                pass
            case "6":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

    session.close()

if __name__ == "__main__":
    main()