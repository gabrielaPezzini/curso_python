from datetime import date
atual = date.today().year
nasc = int(input('Ano do nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('Você tem {} anos e de acordo com a sua idade você pertence a categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e de acordo com a sua idade você pertence a categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e de acordo com a sua idade você pertence a categoria JUNIOR.'.format(idade))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos e de acordo com a sua idade você pertence a categoria SÊNIOR.'.format(idade))
elif idade > 20:
    print('Você tem {} anos e de acordo com a sua idade você pertence a categoria MASTER.'.format(idade))
