# DESAFIO 20/41

# Escreva um programa que leia uma string do usuário e imprima apenas os dígitos da string.

string = input("Digite uma string: ")

#PERCORRE OS CARACTERES DA STRING E VERIFICA SE CADA CARACTERE É UM DIGITO
for caractere in string:
    if caractere.isdigit():
        print(caractere, end="")
