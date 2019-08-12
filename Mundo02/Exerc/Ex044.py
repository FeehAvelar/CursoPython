'''
--------------------Exerc 044-------------------
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu valor preco normal e condicao de pagamento:
-A vista dinheiro/cheque: 10% de desconto
-A vista no cartao: 5% de desconto
-Em ate 2x: preco normal
-3x ou mais: 20% juros
------------------------------------------------
'''

print('='*20+'Lojas Alpaca'+'='*20);
valor = float(input("Digite o valor do produto:"));
cond = int(input("[1] para avista\n[2] para cartao \n[3] 2X no cartao\n[4] 3X ou mais \n"));
if (cond == 1):
    valor = valor * 0.9;
    print("Valor no money: R${}".format(valor));
elif (cond == 2):
    valor = valor * 0.95;
    print("Valor no cartao: R${}".format(valor));
elif (cond == 3):
    print("Valor: R${}".format(valor));
elif (cond == 4):
    valor = valor * 1.2;
    print("Valor: R${}".format(valor));
else:
    print("De 1 a 4, Mentecapto!");