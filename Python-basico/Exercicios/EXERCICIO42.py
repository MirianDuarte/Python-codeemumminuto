# DESAFIO 30/41

# Escreva um programa que leia uma string no formato DD/MM/AAAA e imprima a data no formato AAAA-MM-DD.

data = input("Digite uma data no formato DD/MM/AAAA")

dia = data[0:2]
mes = data[3:5]
ano = data[6:]

data_formatada = ano + "-" + mes + "-" + dia

print(data_formatada)
