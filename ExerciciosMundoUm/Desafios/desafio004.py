# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO
# E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELA

variavel = input('Digite algo: ')

print('O TIPO PRIMITIVO dessa variável é:', type(variavel))

print('Só tem espaços?', variavel.isspace())

print('É um número?', variavel.isnumeric())

print('É alfabético?', variavel.isalpha())

print('É alfanumérico?', variavel.isalnum())

print('Está somente em maiúsculas?', variavel.isupper())

print('Está somente em minúsculas?', variavel.islower())

print('Está capitalizada?', variavel.istitle())