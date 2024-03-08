# DESAFIO 38/41

# Escreva um programa que leia um número inteiro do usuário e imprima todos os seus números perfeitos posteriores.

#solicita que o usuario digite um numero inteiro
num = int(input("Digite um número inteiro: "))

#verifica os numeros posteriores ao numero dado
for i in range(num + 1, num + 100): #verifica os proximos 100 numeros
    soma_divisores = 0 #inicializa a soma dos divisores
    for j in range(1, i): #verifica se existem divisores para cada numero posterior ao dado
        if i % j == 0: #se houver divisor, adiciona a soma
            soma_divisores += j
    if soma_divisores == i: #se a soma dos divisores for igual ao numero, é um numero perfeito e é exibido na tela
        print(i)