# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#
# O NOME COM TODAS AS LETRAS MAIÚSCULAS
#
# O NOME COM TODAS AS LETRAS MINÚSCULAS
#
# QUANTAS LETRAS AO TODO (SEM CONSIDERAR OS ESPAÇOS)
#
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite o seu nome completo: ')).strip() # O STRIP VAI ELIMINAR POSSÍVEIS CARACTERES DE ESPAÇO QUE NO ÍNICIO OU NO FINAL DO NOME

print('Nome completo: {}'.format(nome))

print('Nome completo em maiúsculo: {}'.format(nome.upper()))

print('Nome completo em minúsculo: {}'.format(nome.lower()))

print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
