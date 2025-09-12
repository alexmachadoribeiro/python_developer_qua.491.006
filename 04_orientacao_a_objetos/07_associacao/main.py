import Curso
import Aluno

def main():
    # instancia as classes
    curso1 = Curso.Curso(nome_curso="Python")
    curso2 = Curso.Curso(nome_curso="Java")
    aluno1 = Aluno.Aluno(nome_aluno="Fulano", matricula="1")
    aluno2 = Aluno.Aluno(nome_aluno="Cicrano", matricula="2")
    aluno3 = Aluno.Aluno(nome_aluno="Beltrano", matricula="3")
    aluno4 = Aluno.Aluno(nome_aluno="João", matricula="4")
    aluno5 = Aluno.Aluno(nome_aluno="Maria", matricula="5")
    aluno6 = Aluno.Aluno(nome_aluno="José", matricula="6")

    # inscrevendo alunos no curso 1
    aluno1.inscrever_curso(curso1)
    aluno2.inscrever_curso(curso1)
    aluno3.inscrever_curso(curso1)
    aluno4.inscrever_curso(curso1)

    # inscrevendo alunos no curso 2
    aluno5.inscrever_curso(curso2)
    aluno6.inscrever_curso(curso2)

    # lista de alunos do curso 1
    print(f"Curso: {curso1.nome_curso}")
    print("Lista de alunos:")
    for aluno in curso1.listar_alunos():
        print(aluno)

if __name__ == "__main__":
    main()