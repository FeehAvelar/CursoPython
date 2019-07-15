'''
    -------------------Exerc 023-------------------
    Faça um programa que leia um numero entre 0 e 9999 e mostre
    na tela cada um dos digitos seperados
    Exemplo: 1834
    4 unidade, 3 dezenas, 8 centenas, 1 milhar
    -----------------------------------------------
'''
n = int(input('Digite um numero entre 0 e 9999: \n'));

if (n < 0) or (n > 9999):
    print('Digite um valor valido');
    exit();

u = n // 1 % 10;
d = n // 10 % 10;
c = n // 100 % 10;
m = n // 1000 % 10;

print('{} Unidade - {} Dezena - {} Centena - {} Milhar'.format(u,d,c,m));