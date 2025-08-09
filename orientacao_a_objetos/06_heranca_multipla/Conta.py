import IConta as i

# superclasse
class Conta(i.IConta):
    # construtor
    def __init__(self, agencia, numero, saldo):
        # atributos private
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    # set e get
    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    # métodos da interface
    def exibir_dados(self):
        print(f"Agência: {self.agencia}.")
        print(f"Número da conta: {self.numero}.")
        print(f"Saldo: R$ {self.saldo:.2f}.")
    
    def fazer_deposito(self, valor):
        self.saldo += valor
        return self.saldo
    
    def fazer_saque(self, valor):
        self.saldo -= valor
        return self.saldo