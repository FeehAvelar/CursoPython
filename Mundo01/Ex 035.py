'''
    -------------------Exerc 035-------------------
    Desenvolva um programa que leia o comprimento de 3 retas
    e diga ao user se elas podem ou nao formar um triangulo
    -----------------------------------------------
'''
print('-='*20)
r1 = float(input("Primeira reta: "));
r2 = float(input("Segunda reta: "));
r3 = float(input("Terceira reta: "));
print('-='*20)
if (r1<r2+r3) and (r2 < r1+r3) and (r3 < r1+r2):
    print("O triangulo é formado ^^");
else:
    print("Falha no triangulo")