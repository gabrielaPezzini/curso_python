n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('A média atingida foi {}.'.format(media))
if 7 > media >= 5.0:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO!')
elif media < 5.0:
    print('Média abaixo de 5.0: REPROVADO!')
elif media >= 7.0:
    print('Média 7.0 ou superior: APROVADO!')
