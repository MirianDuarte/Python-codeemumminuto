# DESAFIO 6/41

#  Escreva um programa que leia uma temperatura em graus Celsius e a converta em graus Fahrenheit.
# A fórmula de conversão é F = (C * 1.8) + 32

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheint = (celsius * 1.8) + 32

print(f"A temperatura em Fahrenheint é {fahrenheint:.2f}.")