'''
--------------------Exerc 043-------------------
Desenvolva uma logica que leia o peso e a altura de uma pessoa,
calcule o IMG e mostre seu status, de acordo com  a tabela abaixo:
-Abaixo 18.5: Abaixo do peso
-Entre 18,5~25: Peso ideal
-Entre 25~30: Acima do peso
-Entre 30~40: Obeso
-Acima de 40: Obesidade Morbida
------------------------------------------------
'''
altura = float(input("Digite sua altura: "));
peso = float(input("Digite seu peso: "));
imc = peso/(altura**2);

if (imc < 18.5):
    print("Abaixo do peso");
elif (imc < 25):
    print("Peso ideal");
elif (imc < 30):
    print("Acima do peso");
elif (imc < 40):
    print("Obeso");
else:
    print("Mobido");
