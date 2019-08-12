'''
--------------------Exerc 051-------------------
Faca um programa que leia um numero inteiro e diga se ele e primo ou nao
------------------------------------------------
'''

n = int(input("Digite um numero: "));
divisao = 0;
for i in range (1,n+1):
    if (n%i==0):
        divisao += 1;
        print( ' \33[33m {} '.format(i), end='');
    else:
        print( ' \33[31m {} '.format(i), end='');
print();
if (divisao == 2):
    print("\33[32m {} e um num primo!".format(n));
else:
    print("\33[32m {} nao e primo".format(n));