# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

numero = int(input('Digite um número: '))

print('O número digitado é {}, o seu dobro é {}, o seu triplo é {} e a raiz quadrada é {:.2f}.'
      .format(numero, numero * 2, numero * 3, numero ** 0.5))
