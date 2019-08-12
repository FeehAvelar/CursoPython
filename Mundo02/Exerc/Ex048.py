'''
--------------------Exerc 048-------------------
Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no
intervalo de 1~500
------------------------------------------------
'''
soma = 0;
lista = [];
for i in range (1,501,2):
    if (i%3 == 0) and (i%2 != 0):
        lista.append(i);
        soma += i;
print (lista);
print (soma);
