import modulo as mo

if __name__ == "__main__":
    while True:
        print("1 - Calcular equação do 1º grau.")
        print("2 - Calcular equação do 2º grau.")
        print("3 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        mo.limpar_tela()
        match opcao:
            case "1":
                try:
                    a = float(input("Informe o valor de A: ").replace(",", "."))
                    b = float(input("Informe o valor de B: ").replace(",", "."))
                    mo.limpar_tela()
                    x = mo.primeiro_grau(a, b)
                    print(f"O valor de x é {x}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                    a = float(input("Informe o valor de A: ").replace(",", "."))
                    b = float(input("Informe o valor de B: ").replace(",", "."))
                    c = float(input("Informe o valor de C: ").replace(",", "."))
                    mo.limpar_tela()
                    x = mo.segundo_grau(a, b, c)
                    for result in x:
                        print(f"{result}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue