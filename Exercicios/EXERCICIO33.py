# DESAFIO 21/41

# Escreva um programa que leia uma string do usuário e verifique se ela contém apenas dígitos.

string = input("Digite uma string: ")

#DEFINE UMA VARIAVEL BOOLEANA PARA ARMAZENAR SE A STRING CONTÉM APENAS DIGITOS
so_digitos = True

#PERCORRE OS CARACTERES DA STRING E VERIFICA SE CADA CARACTERE É UM DIGITO
for caractere in string:
    if not caractere.isdigit():
        so_digitos = False
        break 

#EXIBE O RESULTADO DA VERIFICAÇÃO
if so_digitos == True:
    print("A string contém apenas dígitos.")
else:
    print("A string não contém apenas dígitos.")