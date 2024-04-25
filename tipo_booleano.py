"""
Tipo Booleano

Álgebra Booleana, criada por George Boolean

Duas contantes, verdadeiro ou falso.

Errado: true, false

Certo: True, False
"""

ativo = True

print(ativo)

"""
Operações básicas
"""

# Negação (not)
"""
Fazendo a negação, se o valor boolean for verdadeiro o resultado será false. 
Se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)

# Ou (or)

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> False or True
True
>>>

"""

logado = True

print(ativo or logado)

# E (and)

"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.

>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> 

>>> 5 > 6
False
>>> 5 < 6 
True
>>> 6 == 6 
True
>>> 4 <= 5  
True
>>> num1 =7 
>>> num2 = 8
>>> num1 >= num2
False
>>> num1 == num2
False
>>> num1 < num2 or num1 >3
True
>>> num1 < num2 or num1 > 3
True
>>> num1 < num2 and num1 > 3
True
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> ativo = True
>>> type(ativo)
<class 'bool'>




"""


