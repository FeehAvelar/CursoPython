'''
    Digite um programa que leia a quantidade de KM percorridos por um carro alugado,
    e a quantidade de dias que ele ficou alugado. Calcule o preco a pagar, sabendo
    que custa R$60.00 dia, e R$0.15 o KM.
'''

km = float(input("Quanto KM vc rodou com carro: "));
dia = int(input("Quantos dias vc ficou com o carro: "));

preco = (km * 0.15) + (dia *60);
print("O preço do carro ficou em R${:0.2f}".format(preco));