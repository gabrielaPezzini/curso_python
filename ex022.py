'''frase = str(input('Digite seu nome completo: '))
frase = frase.upper()
print(frase)
frase = frase.lower()
print(frase)
e = frase.replace(' ', '')
print(len(e))
p = frase.split()[0]
print(len(p))'''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
