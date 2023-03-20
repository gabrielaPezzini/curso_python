'''from random import randint
# O randint serve para renderizar um número inteiro.
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
n1 = int(input('Em que número pensei: '))
if randint(0, 5):
    print('Você acertou! PARABÉNS!')
else:
    print('Vish! Não foi dessa vez. Tente de novo!.')'''

from random import randint
from time import sleep
# o método sleep faz o computador esperar por alguns segundos.
computador = randint(0, 5) #Faz o computador "PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar
print('PRECESSANDO..')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
