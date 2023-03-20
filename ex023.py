'''frase = str(input('Escreva um número de 0000 à 9999: '))
print('unidade: {}'.format(frase[3]))
print('dezena: {}'.format(frase[2]))
print('centena: {}'.format(frase[1]))
print('milhar: {}'.format(frase[0]))'''

num = int(input('Informe um número de 0 à 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
