# FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

valor_produto = float(input('Digite o valor atual do produto: '))

valor_desconto = valor_produto - (valor_produto * 0.05)

print('O valor do produto com 5% de desconto é R${}'.format(valor_desconto))
