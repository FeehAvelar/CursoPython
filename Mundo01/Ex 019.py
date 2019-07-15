'''
    -------------------Exerc 019-------------------
    Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que
    ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
    ------------------------------------------------
'''
import random;
    
i = 0;
lista = [];
while (i < 4):
    lista.append(input("Digite o nome do {0}º aluno: \n".format(i+1)))
    i += 1;
escolhido = random.choice(lista);
print(lista)
print("O alunos escolhido foi",escolhido);