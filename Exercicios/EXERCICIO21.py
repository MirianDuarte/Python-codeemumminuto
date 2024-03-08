# DESAFIO 9/41

# Escreva um programa que leia um número inteiro do usuário e imprima todos os seus divisores.

numero = int(input("Digite um número inteiro: "))

#PERCORRE UM LAÇO DE 1 ATÉ O NUMERO DIGITADO PELO USUARIO
for i in range(1, numero):
    #SE FOR DIVISOR
    if numero % i == 0:
        print(f"{i} é um divisor de {numero}")
