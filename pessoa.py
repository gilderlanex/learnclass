class Pessoa:
    def __init__(self, nome, dtnascimento):
        self.nome = nome
        self.dtnascimento = dtnascimento

    def setNome(self, nome): # Método para modificar.
        self.nome = nome

    def setDtnascimento(self, dtnascimento):
        self.dtnascimento = dtnascimento

    def getNome(self): ## Método para capturar.
       return self.nome

    def getDtnascimento(self):
        return self.dtnascimento
