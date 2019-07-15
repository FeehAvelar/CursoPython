'''
    ---------------- Ex 009----------------
    Faca um programa que leia um num inteiro qualquer e print em sua tela a sua tabuada
    ---------------------------------------
'''
n = int(input('Digite o num inteiro: '));
i = 1
print('-'*20)
while (i <=10):
    print("{}*{} = {}".format(n,i,n*i));
    i += 1;
print('-'*20)