# DESAFIO 23/41

# Escreva um programa que leia uma string do usuário e verifique se ela contém apenas letras maiúsculas.

string = input("Digite uma string: ")

letras_maiusculas = True

for caractere in string:
    if not caractere.isupper():
        letras_maiusculas = False
        break

if(letras_maiusculas == True):
    print("A string contém apenas letras maiúsculas!")
else:
    print("A string não contém só letras maiúsculas!")
