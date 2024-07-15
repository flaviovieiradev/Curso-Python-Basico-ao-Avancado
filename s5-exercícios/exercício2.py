"""
2. Faça um programa que utilize o comando while para mostrar uma contagem regressiva na tela, iniciando em 10
e terminando em 0. Mostre também uma mensagem “FIM!” após a contagem.
"""

contador = 11
while contador >= 0:
    print(f'Contagem regressiva: {contador}')
    contador -= 1
print('Fim da contagem')
