# importa a biblioteca time para usar a função sleep
from time import sleep

# loop que decrementa o tempo até chegar a zero e imprime cada segundo
tempo = int(input('Tempo em segundos: '))
while tempo >= 0:
    print(tempo)
    sleep(1)
    tempo -= 1

   # quando o tempo acabar, imprime uma mensagem
    print('O tempo acabou!') 