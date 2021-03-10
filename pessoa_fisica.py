from learnclasses.pessoa import Pessoa

class Pessoa_Fisica(Pessoa):
    def __init__(self, CPF, RG, nome, dtnascimento, end):
        super().__init__(nome, dtnascimento,end)
        self.CPF = CPF
        self.RG = RG

    def setCPF(self, CPF):
        self.CPF = CPF

    def setRG(self, RG):
        self.RG = RG

    def getCPF(self):
        return self.CPF

    def getRG(self):
        return self.RG





