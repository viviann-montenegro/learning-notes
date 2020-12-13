"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista
que o desconto foi de 12%.
"""

x = float(input('Qual é o valor do produto? '))
d = (x * 12) / 100

print(f'O valor do produto custa: R${x:.2f}')
print(f'O valor do produto com desconto de 12%: R${d:.2f}')
