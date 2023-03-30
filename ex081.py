lista = list()
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1 # or len(lista) no print
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in perg:
        break
print('-=' * 30)
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não não foi encontrado na lista!')
