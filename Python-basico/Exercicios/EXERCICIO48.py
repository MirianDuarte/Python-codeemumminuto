# DESAFIO 36/41

# Escreva um programa que leia um número inteiro do usuário e imprima todos os seus números primos posteriores.

#solicita que o usuario digite um número inteiro
num = int(input("Digite um número: "))

#verifica os números posteriores ao número dado 
for i in range(num + 1, num + 100): #verifica o próximos 100 números
    qnt_divisores = 0 #inicializa a contagem de divisores
    for j in range(2, int(i/2) + 1): #verifica se existem divisores para cada número posterior ao dado
        if i % j == 0: #se houver um divisor, incrementa a contagem e interrompe a verificação
            qnt_divisores += 1
            break
    if qnt_divisores == 0: #se não houverem divisores, o número é primo e exibido na tela
        print(i)
