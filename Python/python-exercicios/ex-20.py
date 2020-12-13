"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A fórmula de conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

k = float(input('Qual é o valor de massa? '))
l = k / 0.45

print(f'O valor de massa em quilogramas: {k}Kg')
print(f'O valor convertido em libras: {l}lb')
