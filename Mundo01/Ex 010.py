'''
    ---------------- Ex 010----------------
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos
    Dolares ele pode comprar. US$ = R$3,27
    ---------------------------------------
'''
atual = float(input("Quanto de dinheiro vc possui: "));
dollar = atual/3.27;
print("Com R${} voce pode comprar US${:.3f}".format(atual,dollar));