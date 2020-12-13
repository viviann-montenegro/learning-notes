"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.
"""

s = float(input('O salário do Manoel é: '))
a = (s * 25) / 100
n = s + a

print(f'O novo salário do Manoel com o aumento de 25% ficou em: R${n:.2f}')
