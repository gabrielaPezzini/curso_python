print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Digite o primeiro termo de sua PA: '))
razão = int(input('Digite a razão de sua PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
