'''
    -------------------Exerc 025-------------------
    Crie um programa que leie o nome de uma pessoa, e diga se ela tem Silva no nome.
    -----------------------------------------------
'''
nome = input('Digite seu nome: \n').lower();
print('Seu nome tem Silva: {}'.format('silva' in nome));
