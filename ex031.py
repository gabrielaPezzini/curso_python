'''distancia = float(input('Digite a distância que você percorreu em Km: '))
if distancia <= 200:
    print('Você percorreu {}Km. Sua passagem custa R${}.'.format(distancia, distancia * 0.50))
else:
    print('Você percorreu {}Km. Sua passagem custa R${}.'.format(distancia, distancia * 0.45))'''

'''distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))