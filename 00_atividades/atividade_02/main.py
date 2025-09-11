while True:
    try:
        # entrada de dados
        nome = input("Informe seu nome: ").title().strip()
        peso = float(input("Informe seu peso em kg: ").replace(",", "."))
        altura = float(input("Informe sua altura em metros: ").replace(",", "."))
        imc = peso / altura**2

        print(f"O valor do IMC de {nome} é {imc:.2f}.")

        if imc < 18.5:
            print(f"{nome} está abaixo do peso.")
        elif imc < 25:
            print(f"{nome} está no peso ideal.")
        elif imc < 30:
            print(f"{nome} está acima do peso.")
        elif imc < 35:
            print(f"{nome} está obeso.")
        elif imc < 40:
            print(f"{nome} está com obesidade nível II.")
        else:
            print(f"{nome} está com obesidade mórbida.")
        
        while True:
            prosseguir = input("Deseja refazer? (s/n) ").lower().strip()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida.")
                continue
            
        match prosseguir:
            case "s":
                continue
            case "n":
                break

    except Exception as e:
        print(f"Não foi possível calcular o IMC. {e}.")
        continue

"""
# TODO - atividade: Crie um programa que receba do usuário, o nome, o peso em kg, e a altura em metros, e calcule o valor do IMC (Índice de Massa Corporal).
O programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o diagnóstico do usuário com base nos seguintes valores:
- Caso o IMC seja menor que 18.5 = abaixo do peso.
- Caso o IMC seja maior ou igual a 18.5 e menor que 25 = peso ideal.
- Caso o IMC seja maior ou igual a 25 e menor que 30 = acima do peso.
- Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso.
- Caso o IMC seja maior ou igual a 35 e menor que 40 = obesidade nível 2.
- Caso o IMC seja maior ou igual a 40 = obesidade mórbida.
# NOTE - o usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo quantas vezes quiser.
"""