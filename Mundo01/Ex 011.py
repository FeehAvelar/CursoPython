'''
    ---------------- Ex 011----------------
    Faca um programa que leia a altura e largura de uma parede em M, calcule a sua area
    e a quantidade de tintas necessaria para pinta-la, sabendo que cada litro de tinta
    pinta uma área de 2M².
    ---------------------------------------
'''
h = float(input("Digite a altura: "));
b = float(input("Digite a largura: "));
m = h*b;
tinta = m/2;
print("Em uma parede de {}M² precisa de {}L de tinta".format(m,tinta));