'''
--------------------Exerc 051-------------------
Crie um programa que leia um frase qualquer e diga se ela e um palindromo, desconsiderando espacos
------------------------------------------------
'''

frase = input("Digite sua frase: \n");
Inverso = '';

lista = frase.split();
fraseJunto = ''.join(lista);

for letra in range(len(fraseJunto) - 1, -1, -1):
    Inverso += fraseJunto[letra];

print(Inverso);
if Inverso.lower() == fraseJunto.lower():
    print('Palindromo');
else:
    print('Nao Palindromo');
