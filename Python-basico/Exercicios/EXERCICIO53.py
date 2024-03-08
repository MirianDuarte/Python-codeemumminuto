# DESAFIO 41/41

# Escreva um programa que leia um número inteiro do usuário e imprima a sequência de Fibonacci até o número informado.


#solicita que o usuario digite um nuermo inteiro
num = int(input("Digite um número inteiro: "))

#define os primeiros termos da sequencia Fibonacci
fib1, fib2 = 0, 1

#imprime os dois primeiro termos da sequencia Fibonacci
print(fib1, end=" ")
print(fib2, end=" ")


#enquanto o proximo termo da sequencia Fibonacci dor menor ou igual ao numero informado pelo usuario
while fib1 <= num:
    #calcula o proximo termo da sequencia Fibonacci
    fib3 = fib1 + fib2

    #imprime o proximo termo da sequencia de Fibonacci
    print(fib3, end=" ")

    #atualiza as variaveis da sequencia para que o proximo termo seja a soma dos dois termos anteriores

    fib1 = fib2
    fib2 = fib3