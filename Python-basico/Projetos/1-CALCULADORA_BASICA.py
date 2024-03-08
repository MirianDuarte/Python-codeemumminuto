#INICIA O LOOP PRINCIPAL DO PROGRAMA
while True:
    #SOLICITA AO USUARIO QUE ESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR
    operacao = input("Escolha a operacao que deseja realizar (+, -, *, /): ")
    
    #SOLICITA AO USUARIO QUE INSIRA O PRIMEIRO NUMERO
    num1 = float(input("Insira o primeiro numero: "))
    #SOLICITA AO USUARIO QUE INSIRA O SEGUNDO NUMERO
    num2 = float(input("Insira o segundo numero:  "))

    #VERIFICA QUAL OPERACAO O USUARIO ESCOLHEU E REALIZA A OPERACAO CORRESPONDENTE
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado  = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        #SE A OPERACAO NAO FOR VALIDA, INFORMA O USUARIO E CONTINUA O LOOP
        print("Operacao invalida.")
        continue
    #EXIBE O RESULTADO DA OPERACAO
    print(f"O resultado é: {resultado}")
    #PERGUNTA AO USUARIO SE ELE DESEJA REALIZAR OUTRA OPERACAO
    continuar = input("Deseja realizar outra operacao? (s/n): ")

    if continuar.lower() == "n":
        break
#EXIBE UMA MENSAGEM DE DESPEDIDA
print("Obrigado por usar a calculadora!")