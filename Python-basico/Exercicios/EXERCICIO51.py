# DESAFIO 39/41

# Escreva um programa que leia uma string do usuário e substitua todas as suas vogais por um caractere "*".

#solicita que o usuario digite uma string
texto = input("Digite uma string: ")

#define vogais
vogais = "aeiouAEIOU"

#itera sobre cada caractere da string
for caractere in texto:
    #verifica se o caractere é uma vogal
    if caractere in vogais:
        #substitui o caractere por um "*"
        texto = texto.replace(caractere, "*")

#exibe o resultado
print(texto)