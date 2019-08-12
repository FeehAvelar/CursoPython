'''
--------------------Exerc 045-------------------
Crie um programa que faca o computador jogar Jokenpo com voce
------------------------------------------------
'''
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura');
pc = randint(0,2);
pessoa = int(input("[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n"));
pessoa -= 1;
if (pessoa > 3):
    print("Aprende ler, burro!")
    exit();

print("-="*10);
print("\33[34m Jogador jogou: {}\n \33[35mComputador jogou: {} \33[m".format(itens[pessoa], itens[pc]));
print("-="*10);
if (pc == 0): #pedra
    if (pessoa == 0):
        print("Empatou.")
    elif (pessoa == 1):
        print("Jogador venceu")
    else:
        print("Pc venceu")
elif(pc == 1): #papel
    if (pessoa == 0):
        print("PC venceu");
    elif (pessoa == 1):
        print("Empate");
    else:
        print("Pessoa Venceu")
else: #Tesoura
    if (pessoa == 0):
        print("Pessoa venceu");
    elif (pessoa == 1):
        print("PC venceu");
    else:
        print("Empate");


print("-="*10);
