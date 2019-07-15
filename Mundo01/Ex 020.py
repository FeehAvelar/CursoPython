'''
    -------------------Exerc 020-------------------
    O mesmo professor do desafio 19, quer sortear a ordem de apresentacao de trabalhos dos alunos.
    Faca um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
    ------------------------------------------------
'''
import random;

i = 0;
lista = [];
for i in range(0,4):
    lista.append(input("Digite o nome {}º do aluno: \n".format(i+1)));
random.shuffle(lista)
print(lista);