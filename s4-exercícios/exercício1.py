"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor:'))

if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo número ({num2}).")
elif num1 == num2:
    print(f"Os números {num1} e {num2} são iguais.")
else:
    print(f"O segundo número ({num2}) é maior que o primeiro número ({num1}).")
