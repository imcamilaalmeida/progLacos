'''
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200
'''
import math

a = 15

while (a <= 200):
    print(f"{a} elevado à 2 = {math.pow(a, 2):.0f}")
    a = a + 1

print("Depois do bloco do while")


'''
import math

a = math.pow(15, 2)

while (a <= 40000):
    print(a)
    a = math.pow(a + 1), 2))


'''