# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

from math import trunc

num_real = float(input('Digite um número real: '))

print('A porção inteira do número real {} é {}'.format(num_real, trunc(num_real)))
