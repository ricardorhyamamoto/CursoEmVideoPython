# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS
# E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metro = float(input('Digite o valor em metros: '))

print('A convesão de {} metro(s) em centímetros é {} cm e de milimetros é {} mm'
      .format(metro, metro * 100, metro * 1000))
