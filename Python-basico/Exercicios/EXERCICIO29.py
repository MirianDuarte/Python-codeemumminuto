# DESAFIO 17/41

# Escreva um programa que leia uma string do usuário e verifique se é um palíndromo 
#(ou seja, que pode ser lida da mesma forma de trás para frente).

string = input("Digite uma string: ")

#INVERTE A ORDEM DOS CARACTERES DA STRING USANDO UM LOOP FOR
string_invertida = " "
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

#COMPARA A STRING ORIGINAL COM A STRING INVERTIDA
if string == string_invertida:
    print("A string é um palídromo.")
else:
    print("A string não é um palídromo.")