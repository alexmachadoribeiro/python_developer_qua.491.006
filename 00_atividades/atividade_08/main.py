import os

notas = []

while True:
    print("1 - Informe uma nota do aluno de 0 a 10.")
    print("2 - Tirar a média e sair do programa.")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                nova_nota = float(input("Insira a nova nota: ").replace(",", "."))
                if nova_nota >= 0 and nova_nota <= 10:
                    os.system("cls" if os.name == "nt" else "clear")
                    notas.append(nova_nota)
                    print("Nota inserida com sucesso!")
                else:
                    print("Nota inválida.")
            except Exception as e:
                print(f"Não foi possível inserir a nota. {e}.")
            finally:
                continue
        case "2":
            try:
                media = sum(notas) / len(notas)
                print(f"Média: {media:.2f}")
                if media >= 7:
                    print("Aluno está aprovado.")
                elif media >= 5:
                    print("Aluno está de recuperação.")
                else:
                    print("Aluno está reprovado.")
            except Exception as e:
                print(f"Não foi possível calcular a média.")
            finally:
                break
        case _:
            print("Opção inválida.")
            continue
"""
# TODO - atividade: Crie um programa que receba de um professor várias notas de um aluno de 0 a 10 (não importa quantas notas). Ao final do programa, a média das notas deverá ser calculada e informada, e em seguida, o programa irá informar se o aluno:
- Foi aprovado, caso média for maior ou igual a 7
- Ficou de recuperação, caso média for entre 5 e 7
- Foi reprovado, caso média for menor que 5.
"""