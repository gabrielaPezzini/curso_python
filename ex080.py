lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: # or 'lista[len(lista)-1]' / se meu número for maior do que o ultimo numero da minha lista.
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): # ele vai do 0 até a ultima posição
           if n <= lista[pos]:
               lista.insert(pos, n)
               print(f'Adicionado na posição {pos} da lista...')
               break
           pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')