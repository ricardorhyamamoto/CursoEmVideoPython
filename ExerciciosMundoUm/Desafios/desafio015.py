# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDO POR UM CARRO ALUGADO
# E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO
# CALCULE O PREÇO A PAGAR SABENDO QUE O CARRO CUSTA 60 REAIS POR DIA E 0,15 CENTAVOS POR KM RODADO

qtde_dias_alugado = float(input('Informe a quantidade de dias em que o carro foi alugado: '))

qtde_km_percorridos = float(input('Informe a quantidade de quilômetros (KM) que foi percorrido com o carro: '))

preco_total_pagar = (qtde_dias_alugado * 60) + (qtde_km_percorridos * 0.15)

print('O preço a pagar pelo carro por {} dias alugados e {} Km rodados é de R${:.2f}'
      .format(qtde_dias_alugado, qtde_km_percorridos, preco_total_pagar))
