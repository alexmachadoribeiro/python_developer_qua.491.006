# biblioteca
import os

# lista
nomes = []

while True:
    # menu
    print("1 - Cadastre novo nome na lista")
    print("2 - Liste todos os nomes na lista")
    print("3 - Pesquise por um nome na lista")
    print("4 - Altere um nome na lista")
    print("5 - Exclua um nome na lista")
    print("6 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                novo_nome = input("Informe novo nome: ").title().strip()
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!")
            except Exception as e:
                print(f"Não foi possível inserir novo nome. {e}.")
            finally:
                continue
        case "2":
            try:
                for i in range(len(nomes)):
                    print(f"{i}: {nomes[i]}")
                print('-'*40)
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}.")
            finally:
                continue
        case "3":
            nome_pesquisado = input("Informe o nome a ser pesquisado: ").title().strip()
            os.system("cls" if os.name == "nt" else "clear")
            qtde = nomes.count(nome_pesquisado)
            print(f"{nome_pesquisado} foi encontrado {qtde} vezes.")
            continue
        case "4":
            try:
                i = int(input("Informe o índice a ser alterado: "))
                if i >= 0 and i < len(nomes):
                    nomes[i] = input("Informe o novo nome: ").title().strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Nome alterado com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar. {e}.")
            finally:
                continue
        case "5":
            try:
                i = int(input("Informe o índice que deseja excluir: "))
                if i >= 0 and i < len(nomes):
                    del(nomes[i])
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Nome deletado com sucesso!")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível deletar. {e}.")
            finally:
                continue
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue

"""
# TODO - atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista = []
"""