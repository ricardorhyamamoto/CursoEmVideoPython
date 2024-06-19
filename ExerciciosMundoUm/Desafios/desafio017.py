# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO
# CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import pow, sqrt, hypot

cateto_oposto = float(input('Digite o valor do cateto oposto: '))

cateto_adjacente = float(input('Digite o valor do cateto adjacenete: '))

# quadrado_hipotenusa = (pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

# hipotenusa = sqrt(quadrado_hipotenusa)

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))
