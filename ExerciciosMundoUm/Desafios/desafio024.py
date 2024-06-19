# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME SANTO

nome_cidade = str(input('Digite o nome da cidade: ')).strip()

verifica_cidade = nome_cidade.split()

print('O nome digitado da cidade foi: {}'.format(nome_cidade))

# print(nome_cidade[:5].upper() == 'SANTO')

if verifica_cidade[0].upper() == 'SANTO':
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')
