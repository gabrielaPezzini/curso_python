'''casa = float(input('Qual o valor da casa que você gostaria de comprar? '))
salario = float(input('Qual é o seu salário atual? '))
anos = float(input('Em quantos anos você planeja quitar o valor? '))
print('-=-' * 20)
meses = anos * 12
prestacao = casa / meses
print('Valor da casa: R${:.2f}'.format(casa))
print('Sálario do comprador: R$ {:.2f}'.format(salario))
print('Tempo estimado para o pagamento: {} anos'.format(anos))
print('-=-' * 20)
print('O valor da PRESTAÇÃO MENSAL é de R${:.2f}.'.format(prestacao))
print('-=-' * 20)
if prestacao > 0.30 * salario:
    print('Sentimos muito! Seu pedido de empréstimo foi NEGADO!')
elif prestacao <= 0.30 * salario:
    print('Parabéns! Seu pedido de empréstimo foi APROVADO!')'''

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

