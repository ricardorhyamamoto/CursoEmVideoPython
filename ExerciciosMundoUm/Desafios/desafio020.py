# O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA

import random

aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome do aluno: '))
aluno3 = str(input('Digite o nome do aluno: '))
aluno4 = str(input('Digite o nome do aluno: '))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista_alunos)

print('A ordem de apresentação será: ')
print(lista_alunos)