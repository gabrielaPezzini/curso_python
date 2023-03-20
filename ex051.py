primeiro = int(input('Digite o primeiro termo de sua PA: '))
razão = int(input('Digite a razão de sua PA: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='> ')
print('ACABOU')
