# DESAFIO 7/41

# Escreva um programa que leia um número inteiro do usuário e imprima seu fatorial.

numero = int(input("Digite um número inteiro: "))

fatorial = 1

for i in range(1, numero + 1): #IN - VERIFICA SE UM VALOR ESTÁ PRESENTE NA SEQUENCIA /#RANGE - CONJUNTO DE VALORES
    fatorial *= i # *= MULTIPLICA A VARIAVEL POR UM VALOR

print(f"O fatorial de {numero} é {fatorial}.")
