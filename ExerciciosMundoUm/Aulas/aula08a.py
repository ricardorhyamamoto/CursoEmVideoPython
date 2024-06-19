import math

from math import factorial

import random

import emoji

num = int(input('Digite um número: '))

raiz_quadrada = math.sqrt(num)

fatorial = factorial(num)

numero_randomico = random.random()

numero_randomico_int = random.randint(1, 100)

print('A raiz quadrada de {} é igual a {:.0f}'.format(num, raiz_quadrada))

print('O fatorial de {} é {}'.format(num, fatorial))

print(numero_randomico)

print(numero_randomico_int)

print(emoji.emojize('Vamos São Paulo :trophy:', language='alias'))
