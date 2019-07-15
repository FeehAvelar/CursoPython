'''
    -------------------Exerc 027-------------------
    Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
    e o ultimo nome separadamente.
    Ex: Ana Maria de Souza
    Ana / Souza
    -----------------------------------------------
'''

nome = input('Digite o seu nome: \n');
nomeL = nome.split();
print('Primeiro: {} \nSegundo: {}'.format(nomeL[0], nomeL[len(nomeL) - 1]));