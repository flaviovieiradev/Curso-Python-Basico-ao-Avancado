"""
Escopo de variáveis

Dois casos de escopo:

1- Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no blcco onde foram declaradas.
    Ou seja, o seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python, fazemos:

nome_da_variável = valor da variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declarmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Flavio'
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 42
# novo = 0


if numero > 10:
    novo = numero + 10 # A variável novo está declarada
    print(novo)        # localmente dentro do bloco do if.
                       # Portanto é uma variável global.

print(novo)