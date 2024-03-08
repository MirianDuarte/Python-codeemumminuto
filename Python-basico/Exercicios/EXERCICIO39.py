# DESAFIO 27/41

#  Escreva um programa que leia uma string do usuário e verifique se ela termina com uma determinada letra.

string = input("Digite uma string: ")
string_ultimo_indice = len(string)-1

letra = input("Digite uma letra: ")
letra_ultimo_indice = len(letra)-1

if string[string_ultimo_indice] == letra[letra_ultimo_indice]:
    print(f"A string '{string}' termina com a letra '{letra}'.")
else:
    print(f"A string '{string}' não termina com a letra '{letra}'.")