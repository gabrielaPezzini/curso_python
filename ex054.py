'''from datetime import date
count = 0
for c in range(1, 8):
    nasc = int(input('Informe o ano do seu nascimento: '))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 21:
        count += 1
print('{} são maiores de idade e {} não são.'.format(count, 7 - count))'''

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
