#IMPORTA O MÓDULO "RANDOM" PARA GERAR NUMEROS ALEATORIOS
import random

#DEFINE O INTERVALO EM QUE O NUMERO ALEATORIO SERA GERADO
num_minimo = 1
num_maximo = 100

#GERA UM NUMERO ALEATORIO DENTRO DO INTERVALO DEFINIDO
numero_aleatorio = random.randint(num_minimo, num_maximo)

#INICIA O LOOP PRINCIPAL DO JOGO
while True:
    #SOLICITA AO JOGADOR QUE INSIRA UM PALPITE
    palpite = int(input(f"Digite um número entre {num_minimo} e {num_maximo}: "))

    #VERIFICA SE O PALPITE É IGUAL AO NUMERO ALEATORIO
    if palpite == numero_aleatorio:
        print("Parabéns, você acertou!")
        break
    elif palpite < numero_aleatorio:
        print("O número é maior.")
    else:
        print("O número é menor.")

#EXIBE UMA MENSAGEM DE DESPEDIDA
print('Obrigado por jogar!')