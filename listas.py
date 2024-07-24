"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICOS
e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays

    - Possuem tamanho de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo
    inteiro e poderá ter SEMPRE 5 valores.


Na Linguagem Python:

    - Dinâmico: Não possui tamanho fixo. Ou seja, podemos criar a lista e simplesmente ir adicionando elementos.
    - Qualquer tipo de dados: Não possuem tipo de dado fixo. Ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes [].

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['F', 'l', 'a', 'v', 'i', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list("Flavio")

# Podemos facilmente chegar se determinado valor está contido na lista.

num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista.

# Ordenar a visualização de uma lista (sem alterar o seu conteúdo), através da função sorted.
print(sorted(lista1))
print(lista1)

# Ordenar uma lista alterando o seu conteúdo:
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista.
print(lista1.count(1))
print(lista5.count('a'))

# Adicionar elementos em  listas


# Para adicionar elementos em listas, utilizamos a função append.


print(lista1)
lista1.append(42)
print(lista1)

# Observação: Com o append é possível adicionar apenas um elemento por vez.
# lista1.append(44, 45, 45) # Erro

lista1.append([8, 3, 7]) # Coloca a lista como elemento único (sublista).
print(lista1)

if [8, 3, 7] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional à lista.
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice.
# Observação: Isso não substitui o valor inicial (anterior). O mesmo será deslocado para direita da lista.

lista1.insert(2, 'Hello Word')
print(lista1)

# Podemos facilmente juntar duas listas.

lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista.

# Forma 1 (utilizando o reverse).
lista1.reverse()
lista2.reverse()

# Forma 2 (Utilizando o slice de string).
print(lista1[::-1])
print(lista2[::-1])

# Podemos facilmente copiar uma lista.

lista6 = lista2.copy()
print(lista6)

# Para saber o tamanho de uma lista (contar os elementos), utilizamos o length.
print(len(lista1))


# Podemos remover o último elemento de uma lista utilizando o pop.
# Observação: O Pop não só remove o último elemento, mas também o retorna.
print(lista5)
ultimo_elemento = lista5.pop()
print(lista5)
print(ultimo_elemento)


# Podemos também remover um elemento de uma lista informando o índice do elemento a ser retirado.
# Observação: Os elementos à direita deste índice serão deslocados para à esquerda.
# Observação: Se não existir elemento no índice informado, será gerado o erro IndexError.

print(lista5)
segundo_elemento = lista5.pop(2)
print(lista5)
print(segundo_elemento)

# Podemos remover todos os elementos (zerar a lista).

print(lista5)

lista5.clear()

print(lista5)

# Podemos facilmente repetir elementos em uma lista.


nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string em uma lista.

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Observação: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# No exemplo acima, o separador é a vírgula.

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# No exemplo abaixo estamos falando o seguinte: Pega a lista6, coloque espaço em cada elemento e a transforme
# em uma string.
curso = ' '.join(lista6)
print(curso)

# No exemplo abaixo estamos falando o seguinte: Pega a lista6, coloque um cifrão em cada elemento e a transforme
# em uma string.
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados.
lista6 = [1, 2.34, True, 'Flavio', 'd', [1, 2, 3], 4561212]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando o for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando o while

carrinho = []

produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Em listas, fazemos o acesso aos elementos de forma indexada.

#            0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco


# Em listas, podemos também fazer o acesso aos elementos de forma indexada inversa.
# Para entender melhor o índice negativo, pense na lista como um círculo, onde o final
# de um elemento está ligado ao início da lista.

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
# print(cores[-5]) # Erro, pois não existe índice -5.

for cor in cores:
    print(cor)

indice: int = 0

while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar índice em um for:

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []

lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes, porém úteis.

# Encontrar o índice de um elemento na lista:

numeros = [5, 6, 7, 8, 5, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# Observação: Caso não tenha este elemento na lista, será apresentado o value error.

# print(numeros.index(11))

# Em casos onde há mais de um valor encontrado, o index irá retornar o valor do primeiro item encontrado.
print(numeros.index(5))

# Podemos fazer uma busca em um range, ou seja, qual índice começar a buscar.
print(numeros.index(5, 1)) # Buscando o valor 5 a partir do índice 1.
print(numeros.index(5, 2)) # Buscando o valor 5 a partir do índice 2.
# print(numeros.index(5, 5)) # Buscando o valor 5 a partir do índice 5. # Vai dar ValueError: 5 is not in list

# Podemos fazer uma busca em um range com início e fim.

print(numeros.index(5, 2, 5)) # Buscando o valor 5 a partir do índice 2 e parando no 5.

# Revisão do slicing

# lista(inicio:fim:passo)
# range(inicio:fim:passo)

# Trabalhando com slicing de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes.

# Trabalhando com slicing de lista com o parâmetro 'fim'

print(lista[:2])  # Começa no índice zero e vai até o índice 2, sem incluir o índice 2 (que é o número 3).

print(lista[:4])  # Começa no índice zero e vai até o índice 3.

print(lista[1:3])  # Começa no índice um e vai até o índice 3, sem incluir o índice 3 (que é o número 4).

# Trabalhando com slicing de lista com o parâmetro 'passo'

print(lista[::2])  # Começa no índice zero e vai até o final, a cada dois.

print(lista[1::2])  # Começa no índice um e vai até o final, a cada dois.

# Invertendo valores em uma lista:

nomes = ['Mestre', 'Yoda']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho.
# * Se todos os valores forem numéricos.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # Máximo valor
print(min(lista))  # Mínimo valor
print(len(lista))  # Tamanho da lista

# Transformar uma lista em uma tupla

lista = [1, 2, 3, 4, 5, 6]

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3, 4]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Se tivermos divergências entre as variáveis para receber e as variáveis para receber os dados
# será apresentado o ValueError.

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para a nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra.
# Isso em python é chamado de cópia profunda (Deep Copy).

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista

print(nova)
print(lista)

nova.append(4)

print(nova)
print(lista)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista. Após a adição do valor
# 4 uma lista, a outra também foi alterada. Em Python chamado este processo de Shallow Copy.

"""


