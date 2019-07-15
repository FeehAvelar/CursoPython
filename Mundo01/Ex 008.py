'''
    ---------------- Ex 008----------------
    Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm
    ---------------------------------------
'''

m = float(input("Digite a quantidades de metros"));
cm = m * 100;
mm = cm * 100;
print("Metros: {} \nCenti.: {} \nMilim.: {}".format(m,cm,mm));