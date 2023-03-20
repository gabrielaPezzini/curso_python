dias = int(input('Por quantos dias você alugou o carro? '))
dist = float(input('Quantos km andou com o carro? '))
valor = (dias * 60) + (dist * 0.15)
print('O total que deve pagar pelo aluguém do carro será de R${}.'.format(valor))