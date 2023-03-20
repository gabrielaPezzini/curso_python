'''frase = str(input('Digite um nome: ')).strip()
p = frase.split()[0]
print('Primeiro = {}'.format(p))
u = frase.split()[-1]
print('Último = {}'.format(u))'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
