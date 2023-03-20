print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Digite o primeiro termo de sua PA:'))
razão = int(input('Digite a razão de sua PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais # total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Prograssão finalizada com {} termos mostrados. '.format(total))
