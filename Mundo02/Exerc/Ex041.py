'''
--------------------Exerc 041-------------------
A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento do atleta
e mostre sua categoria, de acordo com a idade:
-Ate 9 anos: Mirim
-Até 14 anos: Infantil
-Ate 19 anos: Junior
-Até 20 anos: Senior
-Acima: Master
------------------------------------------------
'''
idade = int(input("Digite a sua idade:"));
if (idade < 9):
    print("Mirim");
elif (idade < 14):
    print("Infantil");
elif (idade < 19):
    print("Junior");
elif (idade < 20):
    print("Senior");
else:
    print("Master");