from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
usuário = 0
maior = n1
while usuário != 5:
    print('-=-' * 20)
    print('OPERAÇÕES: ')
    print('-=-' * 20)
    print('[ 1 ] Somar \n'
          '[ 2 ] Multiplicar \n'
          '[ 3 ] Maior \n'
          '[ 4 ] Novos números \n'
          '[ 5 ] Sair do programa \n')
    usuário = int(input('Qual operação gostaria de executar? '))
    if usuário == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif usuário == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif usuário == 3:
        if n2 > maior:
            maior = n2
        print('O maior valor é {}'.format(maior))
    elif usuário == 4:
        print('Informe os valores novamente:')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif usuário == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    sleep(2)
print('Fim do pragrama! Volte sempre!')
