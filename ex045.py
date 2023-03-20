from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
print('Vamos jogar JOKENPÔ!')
print('=' * 40)
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('=' * 40)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
if computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    elif jogador == 3:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 1:
        print('COMPUTADOR VENDEU!')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 3:
    if jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    elif jogador == 3:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')