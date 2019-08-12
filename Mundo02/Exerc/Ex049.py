'''
--------------------Exerc 048-------------------
Refaça o Ex 009, mostrando a tabuada de um numero que o usuario escolher , so que agora
ultilando um laco for
------------------------------------------------
'''
n = int(input('Digite um numero para tabuada: '));

for i in range (0,11):
    print('{} x {} = {}'.format(n,i,i*n));
print('=-'*20);