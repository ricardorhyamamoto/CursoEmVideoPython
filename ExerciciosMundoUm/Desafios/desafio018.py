# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE AMGULO

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))

cosseno = cos(radians(angulo))

tangente = tan(radians(angulo))

print('O ângulo de {} graus tem o seno de {:.2f}'.format(angulo, seno))

print('O ângulo de {} graus tem o cosseno de {:.2f}'.format(angulo, cosseno))

print('O ângulo de {} graus tem a tangente de {:.2f}'.format(angulo, tangente))
