"""
Tipo Float
Tipo Real, decimal

Cadas Decimais

OBS: O separador de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado do ponto de vista do float, mas gera uma tupla.

valor = 1, 44

print(valor)
print(type(valor))

# Certo do ponto de vista do float.

valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição

valor, valor2 = 1, 44
print(valor)
print(valor2)

print(type(valor))
print(type(valor2))

# Podemos converter um float para um int. OBS: Ao fazer isso, perdemos a precisão do ponto flutuante.

res = (int(valor))
print(res)
print(type(res))

# Podemos trabalhar com números complexos.
variavel = 5j
