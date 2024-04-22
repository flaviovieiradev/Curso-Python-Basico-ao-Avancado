"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String.

Em python, tudo o que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Flavio'
- Aspas duplas -> "Flavio"
- Aspas simples triplas -> ''' Flavio '''
"""
# - Aspas duplas triplas -> """Flavio"""

# Entrada de dados
# print("Qual é o seu nome?")
# nome = input()  # Input -> Entrada

nome = input('Qual é o seu nome?\n')

# Exemplo de print 'antigo' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a0 {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7 em diante
print(f'Seja bem-vindo(a) {nome}!')

#print('Qual é a sua idade')
#idade = input()

idade = int(input('Qual é a sua idade?\n'))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('A pessoa %s tem %s anos.' % (nome, idade))
# print('A pessoa {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7 em diante
print(f'A pessoa {nome} tem {idade} anos.')

"""
# int(idade)

Cast é a conversão de um tipo de dado para outro.
"""

print(f'A pessoa {nome} nasceu em {2024 - idade}.')
