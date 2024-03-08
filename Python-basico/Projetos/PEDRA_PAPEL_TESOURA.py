import random

# define as jogadas possiveis
PEDRA = 'pedra'
PAPEL = 'papel'
TESOURA = 'tesoura'

# define as chaves das jogadas possiveis
CHAVE_PEDRA = 0
CHAVE_PAPEL = 1
CHAVE_TESOURA = 2

# define as mensagens para o jogador ganhar, perder ou empatar
MENSAGEM_GANHOU = 'Você ganhou!'
MENSAGEM_PERDEU = 'Você perdeu!'
MENSAGEM_EMPATOU = 'Você empatou!'

# pede ao jogador para digitar sua jogada
jogada_jogador = input('Escolha sua jogada: (pedra, papel ou tesoura): ')

# verifica se a jogada do jogador é valida
while jogada_jogador != PEDRA and jogada_jogador != PAPEL and jogada_jogador != TESOURA:
    jogada_jogador = input('Escolha sua jogada: (pedra, papel ou tesoura): ')

# gera uma jogada aleatoria para o computador
jogada_computador = random.randint(0, 2)

# verifica qual jogada o computador escolheu e imprime a mensagem correspondente
if jogada_computador == CHAVE_PEDRA:
    print('O computador escolheu pedra.')
elif jogada_computador == CHAVE_PAPEL:
    print('O computador escolheu papel')
else:
    print('O computador escolheu tesoura.')

# verifica quem ganhou e imprime a mensagem correspondente
if (jogada_jogador == PEDRA and jogada_computador == CHAVE_TESOURA) or (jogada_jogador == PAPEL and jogada_computador == CHAVE_PEDRA) or (jogada_jogador == TESOURA and jogada_computador == CHAVE_PAPEL):
    print(MENSAGEM_GANHOU)
elif (jogada_jogador == PEDRA and jogada_computador == CHAVE_PAPEL) or (jogada_jogador == PAPEL and jogada_computador == CHAVE_TESOURA) or (jogada_jogador == TESOURA and jogada_computador == CHAVE_PEDRA):
    print(MENSAGEM_PERDEU)
else:
    print(MENSAGEM_EMPATOU)