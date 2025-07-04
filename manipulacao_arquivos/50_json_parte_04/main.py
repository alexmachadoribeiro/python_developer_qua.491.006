import json
import os

usuarios = []
novo_arquivo = ""

while True:
    usuario = {}
    print("1 - Cadastrar novo usuário.")
    print("2 - Salvar arquivo JSON.")
    print("3 - Fazer leitura do JSON.")
    print("4 - Sair do programa.")
    opcao = input("Informe a opção desejada: ")
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            usuario['nome'] = input("Informe o nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade: "))
            usuario['email'] = input("Informe o e-mail: ").strip().lower()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            print("Usuário cadastrado com sucesso.")
            continue
        case "2":
            novo_arquivo = input("Informe o nome do arquivo: ").strip().lower()
            with open(f"50_json_parte_04/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            os.system("cls" if os.name == "nt" else "clear")
            print("Arquivo salvo com sucesso.")
            continue
        case "3":
            if not novo_arquivo:
                novo_arquivo = input("Informe o nome do arquivo: ").strip().lower()
            with open(f"50_json_parte_04/{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
            print(f"{'-'*20} USUÁRIOS {'-'*20}\n")
            for usuario in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print("-"*40)
            continue
        case "4":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue
    