"""
Faça um programa para ler as dimensões de um terreno (comprimento C e largura L), bem como o preço
do metro de tela P. Imprima o custo para cercar este mesmo terreno com tela.
"""

c = float(input('Qual é o comprimento do terreno? '))
l = float(input('Qual é a largura do terreno? '))
p = float(input('Qual é o preço do metro de tela p? '))
pc = p * c * l

print(f'O custo para cercar este mesmo terreno com tela é de R${pc:.2f}')
