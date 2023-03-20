peso = float(input('Qual é o seu peso em Kg? '))
altura = float(input('Qual é a sua altura em m? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc <= 25:
    print('Você está com o PESO IDEAL!')
elif imc <= 30:
    print('Você está com SOBREPESO!')
elif imc <= 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')