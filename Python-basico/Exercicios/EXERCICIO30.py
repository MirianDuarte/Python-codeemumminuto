# DESAFIO 18/41

# Escreva um programa que leia uma string do usuário e imprima apenas as vogais da string.

string = input("Digite uma string: ")

#PERCORRE OS CARACTERES DA STRING E IMPRIME APENAS AS VOGAIS
for caractere in string:
    if caractere in "aeiouAEIOU":
        print(caractere, end="")