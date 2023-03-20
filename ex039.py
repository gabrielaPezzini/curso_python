'''from datetime import date
nasc = float(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você tem {:.0f} anos.'.format(idade))
if idade < 18:
    print('Faltam {:.0f} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você está dentro do tempo para se alistar.')
else:
    print('Seu tempo de alistamento passou do prazo em {:.0f} anos.'.format(idade - 18))'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamente será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
