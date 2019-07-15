'''
    -------------------Exerc 026-------------------
    Faca um programa que leia uma frase pelo teclado e mostre:
    -   Quantas vezes aparece o 'A';
    -   Em que posição ela aparece a primeira vez
    -   Em que posicao ela aparece a ultima vez
    -----------------------------------------------
'''
frase = input("Digite a frase: \n").lower();
print("""  
Quantidade: {}
Primeiro: {}
Ultimo:{}
""".format(frase.count('a'),frase.find('a')+1,frase.rfind('a')+1));
