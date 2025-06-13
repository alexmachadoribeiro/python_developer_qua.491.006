# laço de reptição
while True:
    # tratamento de exceção
    try:
        # entrada de dados
        etanol = float(input("Informe o valor do etanol: R$ ").replace(",", "."))
        gasolina = float(input("Informe o valor da gasolina: R$ ").replace(",", "."))
        calculo = (etanol/gasolina)*100
        result = "gasolina" if calculo > 70 else "etanol"

        print(f"Resultado = {calculo:.2f}%. Compensa abastecer com {result}.")

        opcao = input("Deseja refazer o cálculo? (s/n)").lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
        continue

"""
# TODO - atividade:
# Crie um programa que receba do usuário o valor do etanol e da gasolina em reais, e informe para o usuário qual o melhor combustível para abastecer.
# NOTE - o usuário poderá informar várias vezes os valores, e irá encerrar o programa quando desejar.
# NOTE - compensa etanol caso ele tenha até 70% do valor da gasolina.
# NOTE - DIVIRTAM-SE!!!! =D
"""