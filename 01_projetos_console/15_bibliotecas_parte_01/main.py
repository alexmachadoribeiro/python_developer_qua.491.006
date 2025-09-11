# importa biblioteca
import os

while True:
    nome = input("Informe seu nome: ")
    os.system("cls")
    print(f"Seja bem vindo, {nome}!")

    prosseguir = input("Deseja inserir outro nome? (s/n) ").lower().strip()

    match prosseguir:
        case "s":
            os.system("cls")
            continue
        case "n":
            break
        case _:
            print("Opção inválida.")
            break