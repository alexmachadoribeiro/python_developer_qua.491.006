# importa módulo
from modulo import limpar_tela, velocidade_media, aceleracao_media

# algoritmo principal
if __name__ == "__main__":
    v = 0
    
    while True:
        print("1 - Calcular velocidade média.")
        print("2 - Calcular aceleração média.")
        print("3 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        limpar_tela()
        match opcao:
            case "1":
                try:
                    vi = float(input("Informe a velocidade inicial: ").replace(",", "."))
                    vf = float(input("Informe a velocidade final: ").replace(",", "."))
                    v = velocidade_media(vi, vf)

                    limpar_tela()
                    print(f"Velocidade média: {v}.")
                except Exception as e:
                    print(f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                    t = float(input("Informe o tempo: ").replace(",", "."))
                    limpar_tela()
                    if v is not 0:
                        a = aceleracao_media(v, t)
                        print(f"Aceleração média: {a}.")
                    else:
                        print("Sem informação da velocidade média.")
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