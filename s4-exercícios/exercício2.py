import math
"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule a 
raiz quadrada do número e apresente-a.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print(f"A raiz quadrada do número", numero, "é", math.isqrt(numero))
else:
    print(f"O número", numero, "é negativo.")
