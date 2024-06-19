# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA
# E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR
# CONSIDERE U$$1,00 = R$3,27

reais = float(input('Informe quantos Reais R$ você possui: '))
cotacao_dolar = float(input('Informe a cotação atual do Dólar U$$: '))

dolares = reais / cotacao_dolar

print('Com R${} você consegue comprar U$${:.2f}'.format(reais, dolares))
