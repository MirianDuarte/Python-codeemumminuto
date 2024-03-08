# importa randiant da biblioteca random
from random import randint

# loop infinito
while True:
    # espera o usuario pressionar enter para jogar o dado
    input('Pressione o Enter para jogar o dado...')
    # gera um numero aleatorio entre 1 e 6
    resultado = randint(1,6)
    # imprime o resultado
    print(f'O dado caiu em {resultado}')
    # pergunta ao usuario se ele quer jogar novamente
    continua = input('Deseja jogar novamente? (s/n): ')
    # se a resposta não for 's', sai do loop
    if continua.lower() != 's':
        break