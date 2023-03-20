'''frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
inverso = frase[::-1]
if frase == inverso:
    print('A frase {} invertida fica {}. \n'
          'Portanto, ela É UM PALÍNDROMO!'.format(frase, inverso))
else:
    print('A frase {} invertida fica {} \n'
          'Portanto, ela NÃO É UM PALÍNDROMO!'.format(frase, inverso))'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
