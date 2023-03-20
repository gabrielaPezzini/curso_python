'''n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior número é {}.'.format(maior))
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor número é {}.'.format(menor))'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado é {}.'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é {}.'.format(maior))
