class Curso:
    def __init__(self,nome_curso):
        self.__nome_curso = nome_curso
        self.alunos_inscritos = []
    
    @property
    def nome_curso(self):
        return self.__nome_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso
    
    # métodos de ação
    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            # FIXME: aluno.inscrever_curso(self)  # deletar
    
    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome_aluno)
        return lista