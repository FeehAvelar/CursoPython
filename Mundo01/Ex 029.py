'''
    -------------------Exerc 029-------------------
                    Radar Eletronico
    Escreva um programa que leia a velocidade de um veiculo. Se ele
    ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.
    A multa vai custar R$7.00 por cade KM acima do limite.
    -----------------------------------------------
'''
vel = int(input("Digite a velocidade: "));

if vel > 80:
    valor = (vel - 80) * 7;
    print('O valor da multa: {}'.format(valor));
else:
    print('Você está permitida!');
