#DESAFIO 4/41
# Escreva um programa que leia um número inteiro do usuário e imprima se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

#verifica se o número é par ou ímpar utilizando
#o operador de módulo(%), se o resto da divisão por 2 for igual a 0, o número é par
#caso contrário, é ímpar
if(numero % 2 == 0):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")