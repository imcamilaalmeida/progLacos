'''
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo
'''

a = 0
while (a <= 20):
    b = a % 2
    if (b == 1):
        print(f"{a} é ímpar")

    a = a + 1