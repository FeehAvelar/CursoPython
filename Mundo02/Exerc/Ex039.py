'''
--------------------Exerc 039-------------------
Faca um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
-Se ainda vai fazer o alistamento militar
-Se e hora de se alistar
-Se ja passou do tempo do alistamento

*Seu programa tambem devera mostar o tempo que falta ou passou do alistamento
------------------------------------------------
'''
from datetime import date;
nasc = int(input("Digite o seu ano de nascimento: "));
ano = date.today().year;
tempo = ano - nasc;
if (tempo < 18):
    print("Voce ainda vai se alistar, falta {} anos".format(18 - tempo));
elif (tempo == 18):
    print("It's time ");
else:
    print("Ja passou do tempo, BURRO! Passou {} anos".format(tempo - 18));