# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA, SABENDO QUE CADA
# LITRO DE TINTA PINTA UMA ÁREA DE 2 METROS QUADRADOS.

largura = float(input('Informe em metros a largura da parede: '))

altura = float(input('Informa em metros a altura da parede: '))

area = largura * altura

qtde_tinta = area / 2.0

print('A área da parede é de {} metros quadrados. E precisamos de {} litros de tinta para pinta-la'
      .format(area, qtde_tinta))
