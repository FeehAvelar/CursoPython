'''
    Math: ceil, floor, trunc, pow, sqrt, factorial...;
'''
import math;
from math import sqrt,ceil;

num = int(input("Digite um num interio: "));
quadrada = math.pow(num,2);
raiz = sqrt(num);
print("Num: {} \nN²:{} \nSqr:{:.4f}".format(num,quadrada,raiz))