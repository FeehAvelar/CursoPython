'''
    -------------------Exerc 023-------------------
    Faça um programa que leia um numero entre 0 e 9999 e mostre
    na tela cada um dos digitos seperados
    Exemplo: 1834
    4 unidade, 3 dezenas, 8 centenas, 1 milhar
    -----------------------------------------------
'''
n = float(input('Digite um numero entre 0 e 9999: \n'));

if (n < 0) or (n > 9999):
    print('Digite um valor valido');
    exit();

#milhar
m = n // 1000;
n -= m*1000;
#centena
c = n // 100;
n -= c *100;
#Dezena
d = n // 10;
n -= d * 10;

print('{} Unidade - {} Dezena - {} Centena - {} Milhar'.format(n,d,c,m));