# MANIPULANDO TEXTO

frase: str = 'Curso em Vídeo Python'

print(frase)

# FATIAMENTO
print('\nFATIAMENTO')

print(frase[9])

# FATIAMENTO DE RANGE, COMEÇA PELO 9 MAS PEGA ATÉ O 12 PARANDO EM 13
print(frase[9:13])

# FATIAMENTO DE RANGE, COMEÇA PELO 9 MAS PEGA ATÉ O 20 E PULANDO DE 2 EM 2
print(frase[9:21:2])

# FATIAMENTO DO INICIO PARANDO EM 5
print(frase[:5])

# FATIAMENTO A PARTIR DE 15 E INDO ATÉ O FINAL
print(frase[15:])

# FATIAMENTO A PARTIR DE 9, VAI ATÉ O FINAL E PULA DE 3 EM 3
print(frase[9::3])

# CONTA O NÚMERO DE RANGE
print(len(frase))

# CONTA O NÚMERO DE VEZES QUE A LETRA 'O' APARECE
print(frase.count('o'))

# CONTA O NÚMERO DE VEZES QUE A LETRA 'O' APARECE INICIANDO EM 0 E PARANDO EM 13
print((frase.count('o',0,13)))

# CONTA O NÚMERO DE VEZES QUE 'DEO' APARECE
print(frase.count('deo'))

# PROCURA ONDE COMEÇA 'DEO'
print(frase.find('deo'))

# PROCURA A STRING 'ANDROID', SE NÃO ENCONTRAR RETORNA -1
print(frase.find('android'))

# ANALISE SE EXISTE A STRING 'CURSO' NA VARIÁVEL FRASE
print('Curso' in frase)


# TRANSFORMAÇÃO
print('\nTRANSFORMAÇÃO')

# SUBSTITUI A STRING PYTHON POR ANDROID
print(frase.replace('Python', 'Android'))

# PRINTA TODA A STRING EM MAIÚSCULA
print(frase.upper())

# PRINTA TODA A STRING EM MINÚSCULA
print(frase.lower())

# SOMENTE A PRIMEIRA EM MAIÚSCULA
print(frase.capitalize())

# INICIA TODAS AS PALAVRAS EM MAIÚSCULAS USANDO O ESPAÇO COMO QUEBRA DE PALAVRAS
print(frase.title())

frase_espaco = '   Aprenda Python   '

print(frase_espaco)
# REMOVE OS ESPAÇOS INÚTEIS NO COMEÇO E FIM DA STRING
print(frase_espaco.strip())

# REMOVE APENAS OS ESPAÇOS A DIREITA
print(frase_espaco.rstrip())

# REMOVE APENAS OS ESPAÇOS A ESQUERDA
print(frase_espaco.lstrip())


# DIVISÃO
print('\nDIVISÃO')

# DIVIDI A VARIAVEL FRASE EM UMA LISTA DE PALAVRAS TENDO O ESPACO COMO DELIMITADOR
print(frase.split())
divisao = frase.split()

# JUNÇÃO
print('\nJUNÇÃO')

print('-'.join(divisao))


# IMPRIMINDO TEXTO LONGO
print('\nIMPRIMINDO TEXTO LONGO')

print('''Se eu quiser imprimir um texto longo no Python.
Eu posso utilizar 3 aspas no início e no fim e
eu vou conseguir imprimir esse texto longo
na tela.''')



