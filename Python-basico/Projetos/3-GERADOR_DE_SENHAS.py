#IMPORTA O MODULO "RANDOM" PARA GERAR NUMEROS ALEATORIOS
import random

#DEFINE AS LETRAS, NUMEROS E CARACTERES ESPECIAIS QUE PODEM SER USADOS NA SENHA
letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteres = "!@#$%&*()_+-=[]{}|;:,.<>?"

tamanho = 8

#INICIA A STRING VAZIA QUE IRÁ ARMAZENAR A SENHA
senha = ""

#GERA A SENHA
for i in range(tamanho):
    #ESCOLHE ALEATORIAMENTE UMA CATEGORIA DE CARACTERES (LETRAS, NUMEROS OU CARACTERES ESPECIAIS)
    categoria = random.randint(1, 3)

    if categoria == 1:
        #SE A CATEGORIA ESCOLHIDA FOR LETRAS, ESCOLHE ALEATORIAMENTE UMA LETRA E ADICIONA A SENHA
        letra_aleatoria = random.choice(letras)
        senha += letra_aleatoria
    elif categoria == 2:
        #SE A CATEGORIA ESCOLHIDA FOR NUMEROS, ESCOLHE ALEATORIAMENTE UM NUMERO E ADICIONA A SENHA
        numero_aleatorio = random.choice(numeros)
        senha += numero_aleatorio
    else:
        #SE A CATEGORIA ESCOLHIDA FOR CARACTERES ESPECIAIS, ESCOLHE ALETORIAMENTE UM CARACTERE ESPECIAL E ADICIONA A SENHA
        caractere_aleatorio = random.choice(caracteres)
        senha += caractere_aleatorio

#EXIBE A SENHA GERADA
print(f"A senha gerada é: {senha}")

#EXIBE UMA MENSAGEM DE DESPEDIDA
print("Obrigado por usar o gerador de senhas!")
