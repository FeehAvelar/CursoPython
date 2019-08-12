'''
--------------------Exerc 040-------------------
Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
no final, de acordo com a media atingido
-Media abaixo de 5.0 Reprovado
-Media entre 5 e 6.9 Recuperacao
-Media 7.0 ou superior Aprovado
------------------------------------------------
'''
n1 = float(input("Digite 1º nota: "));
n2 = float(input("Digite 2º nota: "));
media = (n1 + n2)/2;
if (media < 5.0):
    print("Reprovado");
elif (media >= 7.0):
    print("Aprovado");
else:
    print("Recuperação");