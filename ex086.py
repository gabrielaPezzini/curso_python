matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# primeiro grupo de for para colocar os valores na matriz
for l in range(0, 3): #linha
    for c in range(0, 3): #coluna
        matriz [l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
#segundo grupo de for para mostrar os valores na matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() #toda a vez quer fizer uma coluna, ele irpa quebrar para fazer uma nova linha