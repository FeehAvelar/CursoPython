'''
    -------------------Exerc 018-------------------
    Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno
    e tangente desse angulo
    ------------------------------------------------
'''
import math;

angulo = float(input("Digite o angulo: "));
sen = math.sin(math.radians(angulo));
cos = math.cos(math.radians(angulo));
tg = math.tan(math.radians(angulo));
print(" A: {} \n S: {:.2f} \n C: {:.2f} \n T: {:.2f}".format(angulo,sen,cos,tg));
