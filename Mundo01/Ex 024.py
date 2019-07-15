'''
    -------------------Exerc 024-------------------
    Crie um programa que leia o nome de uma cidade e diga se ela começa com "Santo".
    -----------------------------------------------
'''

cid = input('Digite o nome da cidade: \n').strip().lower();

print(cid[:5] == "santo");