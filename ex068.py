'''from random import randint
computador = randint(0, 10)
print('-=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 30)
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    par = (jogador + computador) % 2 == 0
    if opcao == 'P':
        if par:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR')
            print('Você GANHOU')
            vitorias += 1
            print('---' * 30)
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU ÍMPAR')
            print('Você PERDEU')
            print('---' * 30)
            break
    if opcao == 'I':
        if par:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU PAR')
            print('Você PERDEU')
            print('---' * 30)
            break
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} DEU ÍMPAR')
            print('Você GANHOU')
            print('---' * 30)
            vitorias += 1
print(f'GAME OVER! Você venceu {vitorias} vezes.')
print('-=-' * 30)'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
