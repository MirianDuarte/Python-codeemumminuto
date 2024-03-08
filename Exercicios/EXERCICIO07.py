#RECEBE 2 NOTAS DE UM ALUNO, CALCULA MEDIA E MOSTRA SE ELE FOI APROVADO OU REPROVADO.
#MEDIA ACIMA DE 7 = APROVADO / MEDIA ABAIXO DE 7 = REPROVADO

nota1 = int(input("Digite o valor da primeira nota: "))
nota2 = int(input("Digite o valor da segunda nota: "))
media = (nota1 + nota2) / 2

if (media >= 7):
    print("Você está aprovado! Parabéns")
else: ("Você está reprovado! Sinto muito")