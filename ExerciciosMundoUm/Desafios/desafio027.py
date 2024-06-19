# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE NA TELA O PRIMEIRO E O SEGUNDO NOME SEPARADAMENTE

nome_completo = str(input('Digite o seu nome completo: ')).strip()

nome_separado = nome_completo.split()

print('Seu nome completo é: {}'.format(nome_completo))

print('Seu primeiro nome é: {}'.format(nome_separado[0]))

print('Seu último nome é: {}'.format(nome_separado[len(nome_separado)-1]))
