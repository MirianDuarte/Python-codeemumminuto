#DECLARACAO DE DUAS STRNGS: ALFABETO COM TODAS AS LETRAS DO ALFABETO EM ORDE, E CHAVE COM A PERMUTAÇÃO DESSAS LETRAS
alfabeto = "abcdefghijklmnopqrstuvwyxz"
chave = "qwertyuiopasdfghjklzxcvbnm"

#SOLICITA QUE O USUARIO DIGITE UMA MENSAGEM A SER CRIPTOGRAFADA E CONVERTE TODAS AS LETRAS PARA MINUSCULAS
mensagem = input("Digite uma mensagem a ser criptografada: ").lower()

#INICIALIZAÇAO DA VARIAVEL MENSAGEM_CRIPTOGRAFADA COMO UMA STRING VAZIA
mensagem_criptografada = " "

#LOOP ATRAVES DE CADA LETRA NA MENSAGEM
for letra in mensagem:
    #SE A LETRA ESTIVER NO ALFABETO
    if letra in alfabeto:
        #ENCONTRA O INDICE DA LETRA NO ALFABETO
        indice = alfabeto.index(letra)
        #USA O MESMO INDICE PARA ENCONTRAR A LETRA CORRESPONDENTE NA CHAVE
        nova_letra = chave[indice]
        #ADICIONA A NOVA LETRA A MENSAGEM CRIPTOGRAFADA
        mensagem_criptografada += nova_letra
    #SE A LETRA NAO ESTIVER NO ALFABETO, ADICIONA A MENSAGEM CRIPTOGRAFADA SEM CRIPTOGRAFAR
    else:
        mensagem_criptografada += letra

#IMPRIME UMA MENSAGEM CRIPTOGRAFADA
print("Mensagem criptografada:", mensagem_criptografada)