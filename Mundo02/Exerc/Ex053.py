'''
--------------------Exerc 051-------------------
Crie um programa que leia um frase qualquer e diga se ela e um palindromo, desconsiderando espacos
------------------------------------------------
'''
frase = input('Digite a sua Frase: \n');
frase = frase.replace(' ', '');

fraseInvertida = frase [::-1];

print(fraseInvertida.lower());
#print(frase.lower());
if (fraseInvertida.lower() == frase.lower()):
    print("É um palindromo");
else:
    print("Não é um palindromo");