from learnclasses.pessoa_fisica import Pessoa_Fisica
from learnclasses.pessoa_juridica import Pessoa_Juridica

dados = Pessoa_Fisica(CPF='012.167.443-35', RG='224523-14', nome='Cláudia Dias',dtnascimento='22/01/1980')


print('CPF:', dados.getCPF())
print('RG:',dados.getRG())
print('Nome:', dados.getNome())
print('DT Nascimento:', dados.getDtnascimento())

dadospj = Pessoa_Juridica(CNPJ= '04.234.765/0001-62', nome='Marília S/A',dtnascimento='12/08/1966')

print('CNPJ:', dadospj.getCNPJ())
print('Razão Social', dadospj.getNome())
print('Dt. Criação:', dadospj.getDtnascimento())
