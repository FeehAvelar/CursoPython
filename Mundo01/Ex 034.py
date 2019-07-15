'''
    -------------------Exerc 034-------------------
    Escreva um programa que pergunte o salario de um funcionario e calcule
    o valor do seu aumento. Para o salarios superiores a R$1200.00, calcule
    um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
    -----------------------------------------------
'''
salario = float(input("Digite o seu salario: "));
if (salario > 1200.00):
    salario *= 1.1;
else:
    salario *= 1.15;
print("O novo salario com o aulmento é: R$ {:.2f}".format(salario));