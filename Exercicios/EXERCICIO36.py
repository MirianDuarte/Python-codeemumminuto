# DESAFIO 24/41

# Escreva um programa que leia uma string do usuário e verifique se ela contém apenas letras minúsculas.

string = input("Digite uma string: ")

letras_minusculas = True

for caractere in string:
    if not caractere.islower():
        letras_minusculas = False
        break

if(letras_minusculas == True):
    print("A string contém só letras minúsculas!")
else:
    print("A string não contém só letras minúsculas!")