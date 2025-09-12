# importações
import modulo as m

# algoritmo principal
if __name__ == "__main__":
    while True:
        print("1 - Calcular quadrado.")
        print("2 - Calcular retângulo.")
        print("3 - Calcular triângulo.")
        print("4 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        m.limpar_tela()
        match opcao:
            case "1":
                try:
                    l = int(input("Informe o lado do quadrado: "))
                    a = m.area_quadrado(l)

                    print(f"Área do quadrado: {a}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                    b = int(input("Informe a base do retângulo: "))
                    h = int(input("Informe a altura do retângulo: "))
                    a = m.area_retangulo(b, h)

                    print(f"Área do retângulo: {a}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "3":
                try:
                    b = int(input("Informe a base do triângulo: "))
                    h = int(input("Informe a altura do triângulo: "))
                    a = m.area_triangulo(b, h)

                    print(f"Área do triângulo: {a}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "4":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                continue
        