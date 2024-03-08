# importa a biblioteca random
import random

# define as listas de vogais e consoantes
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

#loop para gerar nomes enquanto o usuario quiser
continua = 'S'
while continua == 'S':
    # inicializa a string do nome
    nome = ''
    # gera um tamanho aleatorio para o nome entre 4 a 10 caracteres
    tamanho = random.randint(4,10)
    # loop para construir o nome
    for i in range(tamanho):
        # adiciona uma consoante se a posição for par, uma vogal se for impar
        if i % 2 == 0:
            nome += random.choice(consoantes)
        else:
            nome += random.choice(vogais)
    #capitaliza o nome e o imprime
    print(nome.capitalize())
    #pergunta ao usuario se ele quer gerar outro nome
    continua = input('Deseja gerar outro nome? S/N ').upper()


