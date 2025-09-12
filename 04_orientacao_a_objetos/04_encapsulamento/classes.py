# superclasse
class Pessoa:
    def __init__(self, telefone, endereco):
        self.__telefone = telefone # private
        self.__endereco = endereco # private

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(telefone, endereco)
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, telefone, endereco):
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        super().__init__(telefone, endereco)
    
    @property
    def nome_fantasia(self):
        return self.__nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj