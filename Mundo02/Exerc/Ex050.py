'''
--------------------Exerc 050-------------------
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar desconsidere-o
------------------------------------------------
'''
soma = 0;
for n in range (1,7):
    num = int(input('Digite o {}º numero: '.format(n)));
    if (num % 2 == 0):
        soma += num;
print(soma);