'''
    -------------------Exerc 033-------------------
    Faca um programa que leia tres numeros e mostre qual é o MAIOR e o MENOR
    -----------------------------------------------
'''
n = int(input('Digite um num: '));
n2 = int(input('Digite um num: '));
n3 = int(input('Digite um num: '));

if (n > n2) and (n > n3):
    print("Maior: ",n);
elif (n2 > n3):
    print("Maior: ",n2);
else:
    print("Maior: ",n3);

if (n < n2) and  (n < n3):
    print("Menor: ",n);
elif (n2 < n3):
    print("Menor: ",n2);
else:
    print("Menor: ",n3);
