'''pessoas = list()
dados = list()
totpessoas = maiorpes = menorpes = 0
while True:
    dados.append(str(input('Nome: ')))
    totpessoas += 1
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in resp:
        break
for p in pessoas:
    if p == 0:
        maiorpes = menorpes = pessoas[p]
    else:
        if pessoas[p] > maiorpes:
            maiorpes = pessoas[p]
        if pessoas[p] < menorpes:
            menorpes = pessoas[p]
print(f'Ao todo, você cadastrou {totpessoas} pessoas.')
print(f'O maior peso foi de {maiorpes}. Peso de {maiorpes[p:]}')'''

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1] # 1 - peso
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()


