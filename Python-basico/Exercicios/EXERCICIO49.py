# DESAFIO 37/41

# Escreva um programa que leia um número inteiro do usuário e imprima todos os seus números perfeitos anteriores.

#solicita que o usuario digite um número inteiro
num = int(input("Digite um número inteiro: "))

#verifica os números anteriores ao número dado
for i in range(num-1, 0, -1):
    soma_divisores = 0 #inicializa a soma dos divisores
    for j in range(1, i): #verifica se existem divisores para cada número anterior ao dado
        if i % j == 0: #se houver um divisor, adiciona a soma
            soma_divisores += j
        if soma_divisores == i: # se a soma dos divisores for igual ao número, é um número perfeito e é exibido na tela
            print(i)