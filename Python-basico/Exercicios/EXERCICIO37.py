# DESAFIO 25/41

# Escreva um programa que leia uma string do usuário e verifique se ela contém apenas espaços em branco.

string = input("Digite uma string: ")

so_espacos = True

for caractere in string:
    if not caractere.isspace():
        so_espacos = False
        break

if so_espacos:
    print("A string só contém espaços em branco.")
else:
    print("A string não contém só espaçoes em  branco.")