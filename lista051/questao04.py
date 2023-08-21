'''
Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100
'''

a = 1
b = 1
while (a <= 100):
    b = b + a
    a = a + 1

print(f"A soma dos valores de 1 a 100 é {b}")