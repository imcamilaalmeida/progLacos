'''
Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente
'''

a = 0
b = 1


while (a <= 610):
    c = a + b
    print(f"O número da sequência Fibonacci é {c}")
    