"""
Ranges

 - Precisamos conhecer o loop for para entender o ranges.
 - Precisamos conhecer o ranges para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais

# Forma 1

range(valor_de_parada)

Observação: valor_de_parada não inclusive (início padrão 0, e passo a cada um).

# Exemplo Forma 1
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)

Observação: valor_de_parada não inclusive (início especificado pelo usuário, e passo a cada um).

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

Observação: valor_de_parada não inclusive (valor_de_inicio, valor de parada e passo especificado pelo usuário).

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4 (É a forma 3 só que inversa).

range(valor_de_inicio, valor_de_parada, -(passo))

Observação: valor_de_parada não inclusive (valor_de_inicio, valor de parada e passo especificado pelo usuário).

# Exemplo Forma 4
for num in range(10, -1, -2):
    print(num)

"""





