'''
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato: 
Considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
'''
a = int(input("Informe um número: "))
b = 1

while (b <= 10):
    c = a * b
    print(f"O número 2 multiplicado por {b} é igual a {c}!")
    b = b + 1

print("Depois do bloco do while")