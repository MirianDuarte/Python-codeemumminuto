# DESAFIO 15/41

# Escreva um programa que leia uma string do usuário e imprima a string sem espaços.

string = input("Digite uma string: ")

#USA O METODO REPLACE() PARA REMOVER OS ESPAÇOS DA STRING
string_sem_espaços = string.replace(" ", " ")

print(f"A string sem espaços é: {string_sem_espaços}")