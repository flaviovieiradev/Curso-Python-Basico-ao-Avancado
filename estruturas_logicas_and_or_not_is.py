"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    -not

Operadores binários:
    -and, or, is

Regras de Funcionamento:
Para o 'and', ambos os valores precisam ser True.
Para o 'or', ou um, ou outro precisa ser True
Para o 'not', o valor do booleano é invertido. Se for True vira True. Se for True vira False.
Pata o 'is', o valor é comparado com um segundo.
"""
"""
ativo = True
logado = False

# And
if ativo and logado:
    print('Bem vindo ao sistema.')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque o seu e-mail!')

# Or
if ativo or logado:
    print('Bem vindo ao sistema.')
else:
    print('Você precisa ativar a sua conta. Por favor, cheque o seu e-mail!')


if not ativo:
    print('Você precisa ativar a sua conta. Por favor, cheque o seu e-mail!')
else:
    print('Bem vindo ao sistema.')
"""

ativo = True
logado = False

# A variável ativo é False?
print(ativo is False)


