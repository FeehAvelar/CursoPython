'''
--------------------Exerc 047-------------------
Crie um programa que mostre na tela todos os numeros pare que estao entre 1~50
------------------------------------------------
'''
lista = [];
for i in range(0,51):
    if (i%2 == 0):
        lista.append(i);
print(lista)