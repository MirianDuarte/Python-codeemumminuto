# DESAFIO 31/41

# Escreva um programa que leia um número inteiro do usuário e imprima os seus dígitos em ordem inversa.

numero = int(input("Digite um número inteiro: "))
numero_invertido = str(numero)[::-1] #INVERTE A ORDEM DOS DIGITOS

print(f"O numero {numero} invertido é {numero_invertido}")

