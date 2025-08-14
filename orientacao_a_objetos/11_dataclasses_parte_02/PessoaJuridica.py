import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaJuridica(Pessoa.Pessoa):
    razao_social: str
    nome_fantasia: str
    cnpj: str

    def __str__(self):
        return f"{'-'*20} Dados da empresa: {'-'*20}:\n\nRazão Social: {self.razao_social}\nNome da empresa: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nE-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"