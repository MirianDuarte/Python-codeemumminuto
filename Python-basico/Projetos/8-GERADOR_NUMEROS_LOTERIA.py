import random

# função para gerar uma lista de 'num' numeros aleatorios entre 1 e 60
def gerar_numeros_loteria(num):
    return random.sample(range(1,61), num)

# loop para jogar a loteria 'num_de_jogos' vezes com 'num_de_numeros' numeros em cada jogo
num_de_jogos = 5
num_de_numeros = 6
for i in range(num_de_jogos):
    # gera uma lista de numeros aleatorios para cada jogo
    numeros = gerar_numeros_loteria(num_de_numeros)
    # imprime os numeros gerados para cada jogo
    print(f'O jogo {i+1}: {numeros}')
