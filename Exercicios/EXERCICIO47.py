# DESAFIO 35/41

# Escreva um programa que leia um número inteiro do usuário e imprima todos os seus números primos anteriores.

#solicita que o usuario digite um número inteiro
num = int(input("Digite um número inteiro: "))

#verifica os numeros anteriores ao numero dado
for i in range(num-1, 1, -1):
    qnt_divisores = 0 #inicializa a contagem de divisores
    for j in range(2, i): #verifica se exitem divisores para cada número anterior ao dado
        if i % j == 0: # se houver um divisor, incrementa a contagem e interrompe a verificacao
            qnt_divisores += 1 
            break
        if qnt_divisores == 0: # se não houverem divisores, o número é primo e é exibido na tela
            print(i)