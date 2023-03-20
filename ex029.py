'''distância = int(input('Digite a sua velocidade em km/h: '))
if distância > 80:
    n1 = distância - 80
    print('Você excedeu o limite de velocidade em {}km/h.' .format(n1))
    print('Sua multa será de R${}.'.format(n1 * 7))
else:
    print('Você está dentro da velocidade permitida. Dirija com cuidado.')'''

velocidade = float(input('Qual é a velocidade atual do seu carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!' .format(multa))
print('Tenha um bom dia! Dirija com segurança!')
