'''
    -------------------Exerc 017-------------------
    Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de
    um triangulo retangulo, calcule mostre o cumprimento da hipotenusa.
    ------------------------------------------------
'''

from math import sqrt;

catOp = float(input("Digite o cateto Oposto: "));
catAd = float(input("Digite o cateto Adjacente: "));

hipo = sqrt(catOp ** 2 + catAd ** 2);

print("A hipotenusa vale: {:.4f}".format(hipo));