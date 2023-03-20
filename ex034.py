salario = float(input('Informe o valor do seu salário atual: '))
if salario > 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print('PARABÉNS! Você irá receber um aumento de 10%, ou seja, R${:.2f}.'.format(aumento))
    print('No total seu novo salário será de R${:.2f}.'.format(novo_salario))
if salario <= 1250:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print('PARABÉNS! Você irá receber um aumento de 15%, ou seja, R${:.2f}.'.format(aumento))
    print('No total seu novo salário será de R${:.2f}.'.format(novo_salario))
