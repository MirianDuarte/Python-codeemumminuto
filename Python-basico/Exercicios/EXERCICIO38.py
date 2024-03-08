# DESAFIO 26/41

#Escreva um programa que leia uma string do usuário e verifique se ela começa com uma determinada letra.

string = input("Digite uma string: ")
letra = input("Digite uma letra: ")

if string[0] == letra[0]:
    print(f"A string '{string}' começa com a letra '{letra}'.")
else:
    print(f"A string '{string}' não começa com a letra '{letra}'.")