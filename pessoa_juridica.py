from learnclasses.pessoa import Pessoa

class Pessoa_Juridica(Pessoa):

    def __init__(self, nome, dtnascimento, CNPJ):
        super().__init__(nome, dtnascimento)
        self.CNPJ = CNPJ

    def setCNPJ(self, CNPJ):
            self.CNPJ = CNPJ

    def getCNPJ(self):
        return self.CNPJ








