'''
    -------------------Exerc 032-------------------
    Faca um programa que leia um ano qualquer e mostre se é bissexto
    -----------------------------------------------
'''
ano = int(input("Digite o ano: "));
if ((ano%4 == 0 and (ano%100 != 0)) or (ano%400 == 0)):
    print("O ano {} é Bissexto".format(ano));
else:
    print("O ano {} é normal!".format(ano))
