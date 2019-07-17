'''
--------------------Exerc 037-------------------
Escreva um programa que leia um numero inteiro qualquer e peca para o usuario qual sera a base:
1-para binario
2-para octal
3-para hexadecimal
------------------------------------------------
'''
n = int(input("Digite um numero inteiro: "));
base = int(input("Escolha uma base: \n1 - Binario \n2 - Octal \n3 - Hexadecimal\n"));

if (base == 1):
    print("{} convertido para binario {}".format(n, bin(n)[2:] ));
elif (base == 2):
    print("{} convertido para binario {}".format(n, oct(n)[2:] ));
else:
    print("{} convertido para binario {}".format(n, hex(n)[2:] ));