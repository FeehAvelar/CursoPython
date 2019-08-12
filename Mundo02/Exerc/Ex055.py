'''
--------------------Exerc 055-------------------
Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o mais pesados, e o mais leve.
------------------------------------------------
'''

maior = 0;
menor = 0;

for i in range (0, 5):
    n = float(input("Digite {}º peso: ".format(i+1)));
    if (n > maior):
        maior = n;

    if (n < menor) or (menor == 0):
        menor = n;

print("O maior peso foi: {:.2f} \nO menor peso foi: {:.2f}".format(maior,menor));