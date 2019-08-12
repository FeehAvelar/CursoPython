'''
--------------------Exerc 056-------------------
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
-A media de idade do grupo;
-Qual e o nome dp homem mais velho;
-Quantas mulheres tem menos de 20 anos
------------------------------------------------
'''

soma = 0;
idadeVelho = 0;
Homem = '';
Mulheres = 0;

for i in range (0,4):
    print('---{}º PESSOA---'.format(i+1));
    nome = input("Qual o seu nome: ");
    idade = int(input("Digite a sua idade: "));
    Sexo = input("M - Masculino / F - Feminino: ");
    soma += idade;
    if (Sexo == 'M') and (idadeVelho < idade):
        Homem = nome;
    if (Sexo == 'F') and (idade < 20):
        Mulheres += 1;

print ("A média de idade é {}\nO homem mais velho é o: {}\nTem {} mulheres abaixo de 20 anos".format(soma/4,Homem,Mulheres))


