'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de b^e
. (Sem usar Math.pow();)
'''

a = int(input("Informe um valor para ser a base da potência: "))
b = int(input("Informe um valor para ser o expoente: "))

c = a ** b
d = 0

print(f"{a} elevado à {b} = {c}")

