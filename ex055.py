maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pessoa (Kg)? '.format(p)))
    if p == 1: # aqui está lendo a primeira pessoa/primeiro laço.
        # o primeiro laço sempre será o maior e o menor valor porque não foi lido nada diferente disso.
        maior = peso
        menor = peso
    else:
        if peso > maior: #Se o peso que acabei de ler for maior do que o peso que eu tenho...
            maior = peso #Então o maior peso passa a ser o peso que acabei de ler.
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
