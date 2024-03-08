# DESAFIO 33/41

#Escreva um programa que leia um número inteiro do usuário e imprima a soma dos seus dígitos.

num = int(input("Digite um número inteiro: "))
#converte o número para string
num_str = str(num)

soma = 0 
for digito in num_str:
    soma += int(digito)
print(f"A soma dos dígitos de {num} é {soma}.")


