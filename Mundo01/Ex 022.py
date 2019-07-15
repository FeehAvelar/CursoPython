'''
    -------------------Exerc 020-------------------
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas a letras minusculas e maiusculas
    - Quantas letras tem (sem considerar espacos)
    - Quantas letras tem o primeiro nome.
    -----------------------------------------------
'''
#Strip() corta os espaços no inicio e no fim, caso possua algum!
nome = input('Digite seu nome completo: \n').strip();

print('Upper: \n{}'.format(nome.upper()));
print('Lower: \n{}'.format(nome.lower()));

espacos = nome.count(' ');
print('Size All: {}'.format(len(nome) - espacos));

nome = nome.split();
print('Size One: {}'.format(len(nome[0])));