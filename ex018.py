from math import radians, sin, cos, tan
num = float(input('Digite o ângulo: '))
seno = sin(radians(num))
print('O ângulo de {} tem seno de {:.2f}.'. format(num, seno))
cosseno = cos(radians(num))
print('O ângulo de {} tem cosseno de {:.2f}.'. format(num, cosseno))
tangente = tan(radians(num))
print('O ângulo de {} tem tangente de {:.2f}.'. format(num, tangente))
