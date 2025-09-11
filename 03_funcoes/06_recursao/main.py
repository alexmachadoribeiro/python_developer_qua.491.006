import modulo as mo

if __name__ == "__main__":
    while True:
        try:
            print("1 - Calcular fatorial")
            print("2 - Sair do programa")
            opcao = input("Escolha: ").strip()
            match opcao:
                case "1":
                    n = int(input("Informe um número inteiro: "))
                    print(f"{n}! = {mo.fatorial(n)}")
                    continue
                case "2":
                    print("Programa encerrado.")
                    break
                case _:
                    print("Opção inválida.")
                    continue
        except Exception as e:
            print(f"Erro. {e}.")
            continue