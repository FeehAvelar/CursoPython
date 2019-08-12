'''
--------------------Exerc 042-------------------
Refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo sera formado
-Equilatero: todos os lados iguais
-Isoceles: Dois lados iguais
-Escaleno: Todos os lados diferentes
------------------------------------------------
'''

print('-='*20)
r1 = float(input("Primeira reta: "));
r2 = float(input("Segunda reta: "));
r3 = float(input("Terceira reta: "));
print('-='*20)
if (r1<r2+r3) and (r2 < r1+r3) and (r3 < r1+r2):
    if (r1 == r2) and (r2 == r3):
        print("Equilatero");
    elif (r1 != r2) and (r1 != r3) and (r2 != r3):
        print("Escaleno");
    else:
        print("Isoceles");
else:
    print("Falha no triangulo");