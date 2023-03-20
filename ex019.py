'''from random import choice
nome = choice(['Elena', 'Gustavo', 'Priscila', 'Beth', 'Arthur'])
print(nome)'''

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceito aluno: '))
n4 = str(input('Quarto aluno: '))
nomes = choice([n1, n2, n3, n4])
print('O aluno escolhido foi {}'.format(nomes))
