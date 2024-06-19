# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO
# FAÇA UM PROGRAMA QUE AJUDE ELE LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

import random

aluno1 = input('Digite o nome do primeiro aluno: ')

aluno2 = input('Digite o nome do segundo aluno: ')

aluno3 = input('Digite o nome do terceiro aluno: ')

aluno4 = input('Digite o nome do quarto aluno: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

print('O aluno escolhido foi',random.choice(lista_alunos))
