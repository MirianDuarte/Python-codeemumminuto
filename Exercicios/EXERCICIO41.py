# DESAFIO 29/41

# Escreva um programa que leia duas strings do usuário e verifique se uma é um anagrama da outra (ou seja, que
# possuem as mesmas letras, mas em ordem diferente).

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# VERIFICA SE AS STRING SÃO ANAGRAMAS
# A FUNÇÃO {SORTED} COLOCA AS STRINGS EM ORDEM ALFABETICA
if sorted(string1) == sorted(string2):
    print("As strings são anagramas.")
else:
    print("As strings não são anagramas.")