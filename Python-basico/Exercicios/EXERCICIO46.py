# DESAFIO 34/41 

# Escreva um programa que leia um número inteiro do usuário e imprima se ele é um número de Armstrong (ou seja,
# se a soma das potências dos seus dígitos é igual ao próprio número).

#lê um numero inteiro do usuario
num = int(input("Digite um número inteiro: "))
#inicializa a variavel para a soma das potencias dos digitos
soma = 0 
# converte o numero para string para poder iterar pelos digitos
num_str = str(num)

#itera pelos digitos do número
for d in num_str:
    #converte o digito para int e eleva a potencia do número de digitos
    soma += int(d) ** len(num_str)

#verifica se a soma das potencias dos digitos é igual ao proprio número
if soma == num:
    print(f"{num} é um número de Armstrong")
else: 
    print(f"{num} não é um número de Armstrong")
