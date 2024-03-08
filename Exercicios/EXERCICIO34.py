# DESAFIO 22/41

# Escreva um programa que leia uma string do usuário e verifique se ela contém apenas letras.

string = input("Digite uma string: ")

#DEFINE UMA VARIAVEL BOOLEANA PARA ARMAZENAR SE A STRING CONTÉM APENAS LETRAS
so_letras = True

#PERCORRE OS CARACTERES DA STRING E VERIFICA SE CADA CARACTERE É UMA LETRA
for caractere in string:
    if not caractere.isalpha():
        so_letras = False
        break 

#EXIBE O RESULTADO DA VERIFICAÇÃO
if so_letras == True:
    print("A string contém apenas letras")
else:
    print("A string não contém apenas letras.")