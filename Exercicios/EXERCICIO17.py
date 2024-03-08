# DESAFIO 5/41

#Escreva um programa que leia um número inteiro do usuário e imprima se ele é positivo, negativo ou zero.

numero = int(input("Digite um numero inteiro: "))

if(numero > 0):
    print(f"O número {numero} é positivo.")
elif(numero < 0):
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")