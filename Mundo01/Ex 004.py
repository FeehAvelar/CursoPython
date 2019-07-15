'''
    -----------Exerc 004 --------------
    Faça um programa que receba algum dado, e mostre seu tipo, e todas suas informações.
    -----------------------------------
'''
valor = input('Digite qualquer coisa: \n');
print(" Type: {0} \n Is Number: {1} \n Is AlphaNumber: {2} ".format(type(valor), valor.isnumeric(), valor.isalnum()));
print(" Is Alphabetic: {} \n UpperCase: {} \n LowerCase: {} ".format(valor.isalpha(), valor.isupper(), valor.islower()));
print(" Is Title: {} \n BarSpace: {}".format(valor.istitle(), valor.isspace()))