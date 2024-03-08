# DESAFIO 10/41

# Escreva um programa que leia um número inteiro do usuário e imprima sua tabuada.

numero = int(input("Digite um número inteiro: "))

#ITERA DE 1 A 10 E IMPRIME A TABUADA DO NÚMERO LIDO
for i in range(1, 11):
    print(f"{numero} X {i} = {numero*i}")