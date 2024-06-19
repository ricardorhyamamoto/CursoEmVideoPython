# FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU
# NOVO SALÁRIO COM 15% DE AUMENTO.

salario = float(input('Informe o valor do seu salário: '))

novo_salario = salario + (salario * 0.15)

print('Seu novo salário com aumento de 15% será de R${:.2f}'.format(novo_salario))
