# criar um acumulador - soma os valores
soma = 0
# criar um contador - soma 1
cont = 0
for c in range(1, 501, 2):
    # 2 no final para apenas apresentar os números ímpares.
    if c % 3 == 0:
        cont = cont + 1
        # ou soma += 1
        soma = soma + c
        # ou soma += c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
