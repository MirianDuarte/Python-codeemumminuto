# DESAFIO 40/41

# Escreva um programa que leia uma string do usuário e substitua todas as suas letras por um caractere "*".

#soliita que o usuario digite uma string
texto = input("Digite uma string: ")

#itera sobre cada caractere da string
for caractere in texto:
    #verifica se o caractere é uma letra
    if caractere.isalpha():
        #substitui o caractere por um "*"
        texto = texto.replace(caractere, "*")

#exibe o resultado
print(texto)