# DESAFIO 19/41

# Escreva um programa que leia uma string do usuário e imprima apenas as consoantes da string.

string = input("Digite uma string: ")

#PERCORRE OS CARACTERES DA STRING E VERIFICA SE CADA CARACTERE É UMA CONSOANTE
for caractere in string:
    if caractere.isalpha() and caractere not in "aeiouAEIOU":
        print(caractere, end="")