'''
    ---------------- Ex 013----------------
    Faca um algoritmo que leia o salario do funcionario e mostre seu novo salario, com
    15% de aumento
    ---------------------------------------
'''
salario = float(input("Digite o salario atual: R$"));

print("O salario inicial: R${:0.2f} \nO novo salario: R${:0.2f}".format(salario,salario*1.15))