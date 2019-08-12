'''
--------------------Exerc 054-------------------
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda nao atingiram a maioridade e quantas atingiram
------------------------------------------------
'''
from datetime import date;

pessoaMaior = 0;
pessoaMenor = 0;
anoAtual = date.today().year;

for i in range (0,7):
    ano = int(input("Digite o ano de nascimento da {}º pessoa: ".format(i+1)));
    idade = anoAtual - ano;

    if idade >= 18:
        pessoaMaior += 1;
    else:
        pessoaMenor += 1;

print('No final foi: \n{} Maioridade\n{} Menoridade'.format(pessoaMaior,pessoaMenor));