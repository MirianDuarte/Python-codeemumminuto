# DESAFIO 28/41

# Escreva um programa que leia uma string do usuário e conte quantas vezes uma determinada letra aparece na string.

string = input("Digite uma string: ")
letra = input("Digite uma letra: ")

#INICIANDO O CONTADOR DE OCORRENCIAS DA LETRA COMO ZERO
cont = 0

for c in string:
    #SE O CARACTERE FOR IGUAL A LETRA DESEJADA, INCREMENTA O CONTADOS
    if c == letra:
        cont += 1

print(f"A letra '{letra}' aparece {cont} vezes na string.")



