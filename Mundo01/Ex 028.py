'''
    -------------------Exerc 028-------------------
                    Jogo de advinhação
    Escreva um programa que faca o computador "pensar" em um numero inteiro
    entre 0 e 5 e peca para o usuario tentar descobrir qual num foi escolhido
    pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu
    -----------------------------------------------
'''

from random import randint;

num = randint(0,5);
num2 = int(input("Digite o numero: "));

#print(num)

if (num == num2):
    print("Você acertou!");
else:
    print("Você errou");
