# DESAFIO 32/41

# Escreva um programa que leia um número inteiro do usuário e imprima quantos dígitos ele possui.

num = int(input("Digite um número inteiro: "))
num_digitos = len(str(num)) #CONVERTE NUM PARA STRING E CONTA SEUS CARACTERES

print(f"O número {num} possui {num_digitos} digito(s)")
