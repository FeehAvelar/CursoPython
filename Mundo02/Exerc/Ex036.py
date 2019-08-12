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



