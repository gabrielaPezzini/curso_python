'''ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))'''

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
    # esse comando é para pegar o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
# o ano deve ser divisível por 4 e 400, mas não pode ser divisível por 100.
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
