'''maioridade = 0
tothomem = 0
totmulher20 = 0
cont = ' '
sexo = ' '
while True:
    print('---' * 20)
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo in 'M':
        tothomem += 1
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('---' * 20)
    cont = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {tothomem} homens cadastrados.')
print(f'E temos {totmulher20} mulheres com menos de 20 anos.')'''

tot18 = 0
tothomem = 0
totmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tothomem} homens cadastrados.')
print(f'E temos {totmulher20} mulheres com menos de 20 anos.')