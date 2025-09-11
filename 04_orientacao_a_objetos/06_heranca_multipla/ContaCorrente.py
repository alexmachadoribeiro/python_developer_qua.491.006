import Pessoa as p
import Conta as c

# subclasse
class ContaCorrente(p.Pessoa, c.Conta):
    def __init__(self, nome, cpf, email, profissao, telefone, endereco, salario, agencia, numero, saldo):
        p.Pessoa.__init__(self, nome, cpf, email, profissao, telefone, endereco, salario)
        c.Conta.__init__(self, agencia, numero, saldo)
    
    def exibir_dados(self):
        print("DADOS DA CONTA:\n")
        p.Pessoa.exibir_dados(self)
        c.Conta.exibir_dados(self)