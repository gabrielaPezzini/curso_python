'''soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma dos número pares vale {} '.format(soma))'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))