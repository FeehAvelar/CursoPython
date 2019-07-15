'''
    -------------------Exerc 031-------------------
    Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem,
    cobrando R$0.50/KM para viagens de até 200KM, e R$0.45 para viagens mais longas.
    -----------------------------------------------
'''
dist = int(input("Digite a distancia: "));
valor = 0;
if (dist <= 200):
    valor = dist * 0.5;
else:
    valor = dist *0.45;
print("O Valor da viagem é: R${:.2f}".format(valor));
