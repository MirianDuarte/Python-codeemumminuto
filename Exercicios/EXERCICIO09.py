#FAÇA UM PROGRAMA QUE RECEBA AS MEDIDAS DOS TRES LADOS DE UM TRIANGULO E DIGA SE ELE É EQUILATERO, ISOSCELES OU ESCALENO

#EQUILÁTERO - TODOS OS LADOS IGUAIS
#ISOSCELES - POSSUI 2 LADOS IGUAIS
#ESCALENO - NENHUM LADO IGUAL 

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 == lado2 and lado2 == lado3):
    print("O triângulo é o equilátero")
elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("O triângulo é o isosceles!")
else:
    print("O triângulo é o escaleno")