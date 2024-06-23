# FAÇA UM PROGRAMA QUE LEIA UM  NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS EM UNIDADE, DEZENA, CENTENA E MILHAR

numero = int(input('Digite um número entre 0 e 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('Analisando o número: {}'.format(numero))

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
