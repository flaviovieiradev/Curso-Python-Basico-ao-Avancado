"""
Loop for

Loop > Estrutura de Repetição
For > É uma dessas estruturas

C ou Java

for(i = 0; i < limitador; i++){
    //execução do código
}

# Em Python

for item in iterável:
    //Execução do código


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de Iteráveis:
    - String
    Nome = 'Flavio'
    - Lista
    Lista = [1, 2, 3, 4, 5, 6]
    - Range
    Números = range(1, 10)

nome = 'Flavio'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1, 10)      # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor inicial, valor final)
Observação: O valor final não é inclusive. 
1
2
3 ( O três não será impresso).

for numero in range(1, 3):
    print(numero)


Enumerate 
    O que o Enumerate gera é um índice para cada item iterável.
    Exemplo:
    ((0, 'F'), (1, 'l'), (2, 'a'), (3, 'v'), (4, 'i'), (5, 'o')) 


for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(indice, letra)

# No exemplo abaixo (com o underline) quando não precisamos de um valor (o índice nesse exemplo) podemos
# descartá-lo com o underline.
for _, letra in enumerate(nome):
    print(letra)

nome = 'Flavio'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1, 10)      # Temos que transformar em uma lista


for valor in enumerate(nome):
    print(valor)

qtd = int(input("Quantas vezes esse loop deve funcionar?"))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')

qtd = int(input("Quantas vezes esse loop deve funcionar?"))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Digite o {n} / {qtd}: '))
    soma = soma + num
print(f'A soma é {soma}')


nome = 'Flavio'

for letra in nome:
    print(letra, end='')


# Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original:   U+1F603
# Modificado: U0001F603

emoji = '\U0001F603'

for x in range(3):
    for num in range(1, 10):
        print(f'{emoji * num}')
