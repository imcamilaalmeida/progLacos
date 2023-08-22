'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''

a = float(input("Digite um número (-1 encerra o programa): "))
b = a
c = a
d = 0
soma = 0

while (a != -1):
    d = d + 1
    soma = soma + a
    if (b < a):
        b = a

    if (c > a):
        c = a

    a = float(input("Digite outro número (-1 encerra o programa): "))
if (b == -1):
    print("Você inseriu -1 na primeira resposta. \n PROGRAMA ENCERRADO!")

else:
    print(f"Maior valor inserido: {b:.0f}")
    print(f"Menor valor inserido: {c:.0f}")
    print(f"Média dos valores inseridos: {soma/d}")
    print(f"Total de respostas: {d}")