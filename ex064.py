'''n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [digite 999 para parar]: '))
    cont += 1
    soma += n
soma -= 999
cont -= 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999: #flag
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
    # o flag não vai ser somado se ele for igual a 999,
    # pois ele irá sair direto.
print('Você digitou {} números e a soma entre eles foi {}!'.format(cont, soma))


