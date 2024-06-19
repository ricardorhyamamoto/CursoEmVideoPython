# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO
# E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR

numero = int(input('Digite um número: '))

print('O número digitado foi {}, o seu sucessor é {} e seu antecessor é {}.'
      .format(numero, numero + 1, numero -1))
