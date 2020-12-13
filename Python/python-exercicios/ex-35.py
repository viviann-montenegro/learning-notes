"""
Sejam A e B os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raíz a² + b².
Faça um programa que receba os valores de A e B e calcule o valor da hipotenusa através da equação.
Imprima o resultado dessa operação.
"""

import math
a = int(input('Qual é o valor do cateto A? '))
b = int(input('Qual é o valor do cateto B? '))
hipot = math.sqrt(a ** 2 + b ** 2)

print(f'O valor da hipotenusa: {hipot}')
