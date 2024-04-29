"""
Tipo String

Em Python, um dado é considerado do tipo String sempre que:

- Estiver entre aspas simples: 'uma string', '234', 'a', 'True', '42.3'

- Estiver entre aspas duplas: "uma string", "234", "a', "True", "42.3"

- Estiver entre aspas simples trplas: ''' uma string ''', '''234''', '''a''',  '''True''', '''42.3'''

- Estiver entre aspas duplas triplas: """ """

nome = 'Flavio'
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina \"Jolie' # O barra é um caractere de escape.
print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(nome.upper())

nome = 'Angelina Jolie'
print(nome.lower())

nome = 'Angelina Jolie'
print(nome.split())

print(nome[0:4]) # O quarto elemento não está incluído.  Essa operação é chamada de slice de string.

nome = 'Flavio'
print(nome[2:6]) # O quarto elemento não está incluído. Essa operação é chamada de slice de string.

nome = 'Flavio Vieira'
print(nome.split())

print(nome.split()[1])

"""

# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """"True""", """42.3"""
# ['0','1','2','3','4','5']
# ['F','l','a','v','i','o']

nome = 'Flavio Vieira'
"""
[:: -1] -> Começe do primeiro elemento, vá até o último elemento e inverta.
"""
print(nome[::-1]) # Inversão da string.

print(nome.replace('a','P'))

print(type(nome))







