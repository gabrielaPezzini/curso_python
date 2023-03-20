n1 = float(input('Digite o valor do seu sálario atual em reais: '))
s = n1 * 0.15
ns = s + n1
print('Parabéns! Você recebeu um aumento de 15% e seu novo salário será R${:.2f}.'.format(ns))
