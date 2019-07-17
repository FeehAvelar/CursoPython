'''
--------------------Exerc 036-------------------
Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar
o valor da casa, o salario do comprador e em quantos anos ele vai pagar
Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario, ou entao o emprestimo sera
negado
------------------------------------------------
'''
valor = float(input("Digite o valor da casa: R$"));
sal = float(input("Digite o salario: R$"));
tempo = int(input("Pretende pagar em quantos anos: "));
mensal = valor / (tempo*12);
print("O valor da prestacao é de: R${:.2f}".format(mensal));
if (mensal <= (sal * 0.3)):
    print("Aprovado!");
else:
    print("Reprovado");



'''
--------------------Exerc 040-------------------
Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem
no final, de acordo com a media atingido
-Media abaixo de 5.0 Reprovado
-Media entre 5 e 6.9 Recuperacao
-Media 7.0 ou superior Aprovado
------------------------------------------------
'''
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
'''
--------------------Exerc 042-------------------
Refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo sera formado 
-Equilatero: todos os lados iguais
-Isoceles: Dois lados iguais
-Escaleno: Todos os lados diferentes
------------------------------------------------
'''