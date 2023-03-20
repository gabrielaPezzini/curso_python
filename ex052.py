num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1): # precisa colocar mais 1 porque no for sempre conta uma casa a menos
    if num % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')

