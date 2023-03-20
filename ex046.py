'''from time import sleep
festa = str(input('Qual é a comemoração? ')).upper()
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FELIZ {}!!'.format(festa))'''

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POOOW!')