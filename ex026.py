frase = str(input('Digite uma frase: ')).upper().strip()
a = frase.count('A')
print('A letra "a" aparece {} vezes na sua frase.'.format(a))
p = frase.find('A') + 1
print('Foi encontrada pela primeira vez na posição {}.'.format(p))
u = frase.rfind('A') + 1
#rfind é para começar a procurar pelo lardo direito
print('E pela última vez na posição {}.'.format(u))
#Dividada seu programa em pequenos pedaços
#O usuário fará coisas para o seu programa parar de funcionar

