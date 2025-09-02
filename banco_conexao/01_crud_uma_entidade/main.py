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
        print("6 - Exportar dados para Excel")
        print("7 - Sair do programa")
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
                md.alterar_dados(session, Pessoa)
                continue
            case "5":
                md.excluir_pessoa(session, Pessoa)
                continue
            case "6":
                md.exportar_excel(session, Pessoa)
                continue
            case "7":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue

    session.close()

if __name__ == "__main__":
    main()