"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python

The Zen of Python
import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

A ideia da PEP8 é que possamos escrever código Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes:

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis.


def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para indentação (NÃO USE TAB!)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classes em branco;
- Métodos dentro de uma classe  devem ser separados com uma única linha em branco;

[5] - Imports
 - Imports devem ser sempre feitos em linhas separadas;

#Import Errado:
import sys, os

#Import Certo:
import sys
import os

# Não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depos de quaisquer comentários ou docstrings e antes
# de constantes ou variáveis globais.

[6] - Espaços entre expressões e instruções

# Não faça:

funcao ( algo [ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1]), {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict = ['chave'] = list [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x              = 1
y              = 9
variavel_longa = 5

# Faça:

x = 1
y = 9
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha.

"""
import this