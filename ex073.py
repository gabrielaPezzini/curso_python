times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=-' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=-' * 20)
print(f'Os cinco primeiros são: {times[:5]}')
print('-=-' * 20)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=-' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 20)
print(f'O Chapecoense está na posição {times.index("Chapecoense") + 1}')
