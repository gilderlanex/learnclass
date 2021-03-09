class Pessoa:
    def __init__(self, nome, dtnascimento, end):
        self.nome = nome
        self.dtnascimento = dtnascimento
        self.end = end

    def setNome(self, nome): # Método para modificar.
        self.nome = nome

    def setDtnascimento(self, dtnascimento):
        self.dtnascimento = dtnascimento

    def setend(self, end):
        self.end = end

    def getNome(self): ## Método para capturar.
       return self.nome

    def getDtnascimento(self):
        return self.dtnascimento

    def getEndereco(self):
        return self.end
