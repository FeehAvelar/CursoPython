'''
--------------------Exerc 038-------------------
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela:
-O primeiro e maior
-O segundo e maior
-Nao existe valor maior,Sao iguais
------------------------------------------------
'''
n1 = int(input("Digite um numero: "));
n2 = int(input("Digite um numero: "));

if (n1 > n2):
    print("O primeiro é maior");
elif (n1 == n2):
    print("São iguais");
else:
    print("O segundo é maior");