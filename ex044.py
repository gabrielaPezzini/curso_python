'''num = float(input('Preço do produto: R$'))
print('[ 1 ] à vista dinheiro/cheque.')
print('[ 2 ] à vista no cartão.')
print('[ 3 ] em até 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
pagamento = int(input('Qual a forma de pagamento? '))
if pagamento == 1:
    print('Com essa forma de pagamento, o seu produto terá 10% de desconto.')
    print('Seu produto irá custar R${:.2f}'.format(num - (num * 0.10)))
elif pagamento == 2:
    print('Com essa forma de pagamento, o seu produto terá 5% de desconto.')
    print('Seu produto irá custar R${:.2f}'.format(num - (num * 0.05)))
elif pagamento == 3:
    print('Com essa forma de pagamento, o seu produto continuará com o preço atual de R${}.'.format(num))
elif pagamento == 4:
    print('Com essa forma de pagamento, o seu produto terá um acréscimo de 20% de juros.')
    print('Seu produto irá custar R${:.2f}'.format((num * 0.20) + num))
else:
    print('Forma de pagamento inválida! Tente novamente.')'''

print('{:=^40}'.format(' LOJAS CACHAPUZ '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela ))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

