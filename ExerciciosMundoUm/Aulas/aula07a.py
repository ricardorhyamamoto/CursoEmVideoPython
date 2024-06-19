# OPERADORES ARITMÉTICOS
#
# +   ADIÇÃO
# -   SUBTRAÇÃO
# *   MULTIPLICAÇÃO
# /   DIVISÃO
# //  DIVISÃO INTEIRA
# %   RESTO DA DIVISÃO
# **  POTÊNCIA ou EXPONENCIAÇÃO
# ==  IGUAL
#
# ORDEM DE PRECEDÊNCIA
#
# 1   ()
# 2   **
# 3   *, /, //, %
# 4   +, -


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input(('Digite o segundo valor: ')))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
div_inteira = n1 // n2
resto_div = n1 % n2
potencia = n1 ** n2

print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f}, '
      'a divisão inteira é {}, o resto da divisão é {} e a potência é {}'
      .format(soma, sub, mult, div, div_inteira, resto_div, potencia))
