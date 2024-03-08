#DESAFIO 12/41

# Escreva um programa que leia uma string do usuário e imprima a string invertida.

string = input("Digite uma string: ")

#VARIAVÉL VAZIA PARA ARMAZENAR A STRING INVERTIDA
string_invertida = " "

#ITERA POR CADA CARACTER NA STRING, COMEÇANDO PELO ÚLTIMO, E INDO ATÉ O PRIMEIRO
for i in range(len(string)-1, -1, -1):
    #ADICIONA CADA CARACTER NA VARIAVÉL STRING_INVERTIDA
    string_invertida += string[i]

print(f"A string invertida é: {string_invertida}")