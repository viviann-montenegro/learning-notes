"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

l = int(input('Qual é o valor de massa em libras? '))
k = l * 0.45

print(f'O valor da massa em libras: {l}lbs')
print(f'O valor convertido em quilogramas: {k}Kg')
