'''from random import randint
from time import sleep
palpites = 0
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1)
while jogador != computador:
    jogador = int(input('GANHEI!! Tente de novo! Em que número pensei? '))
    palpites += 1
print('PARABÉNS! Com {} palpites você conseguiu me vencer!'.format(palpites))'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou: # quando 'not acertou' se tornar False ele sai do looping
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Teste mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas. PARABÉNS!'.format(palpites))
