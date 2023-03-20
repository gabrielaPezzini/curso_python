total = 0
totprod1000 = 0
menor = 0
cont = 0
barato = ''
print('---' * 20)
print('LOJA SUPER BARATÃO')
print('---' * 20)
while True:
    produto = str(input('Nome do Produto: ')).upper().strip()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totprod1000 += 1
    if cont == 1 #or preço < menor:
        menor = preço
        barato = produto
    else: # dá para retirar esse bloco
        if preço < menor:
            menor = preço
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break
    print('---' * 20)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totprod1000} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')



