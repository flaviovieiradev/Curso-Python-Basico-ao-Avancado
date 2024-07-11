"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""

num: int = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número digitado é: {num}. Este número é par.")
else:
    print(f"O número digitado é: {num}. Este número é ímpar.")
