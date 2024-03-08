#FAÇA UM PROGRAMA QUE CALCULE O DESCONTO DE UM PRODUTO DE ACORDO COM A FORMA DE PAGAMENTO ESCOLHIDO PELO CLIENTE
#A VISTA 10%
#CARTÃO 5% 
#PARCELADO NORMAL

preco = float(input("Digite o valor da compra: "))

print("1. À vista\n2. À vista cartão\n3. Parcelado")
opcao = int(input("Escolha sua forma de pagamento: "))

if(opcao == 1):
    calculo = preco * 0.90
    print(f"Preço final: {calculo}")
elif (opcao == 2):
    calculo = preco * 0.95
    print(f"Preço final: {calculo}")
elif (opcao == 3 ):
    print(f"Preço final: {preco}")
else: 
    print ("Opção inválida!")