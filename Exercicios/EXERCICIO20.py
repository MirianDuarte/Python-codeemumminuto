# DESAFIO 8/41

# Escreva um programa que leia um número inteiro do usuário e imprima se ele é primo.

numero = int(input("Digite um número inteiro: "))

#INICIALIZA A VARIAVEL COM O VALOR 0
vdivisores = 0

#VERIFICA SE O NÚMERO É MENOR OU IGUAL A 1 (NUMEROS MENORES OU IGUAIS A 1 NÃO TEM DIVISORES ALÉM DE 1 E ELES MESMOS)
if(numero <= 1):
    vdivisores = 1
else: 
    #VERIFICA QUANTOS DIVISORES O NÚMERO TEM, CONTANDO DE 2 ATÉ O PRÓPRIO NÚMERO - 1
    for i in range(2, numero):
        if numero % i == 0:
            vdivisores += 1

if(vdivisores == 2): # == IGUAL A 
    print("O número {numero} é primo")
else:
    print("O número {numero} não é primo")