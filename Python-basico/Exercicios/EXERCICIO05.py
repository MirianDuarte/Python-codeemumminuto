#PROGRAMA QUE CALCULA O IMC

# IMC = PESO / (ALTURA*ALTURA)

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

print(f"O cálculo do seu IMC é: ", imc)
