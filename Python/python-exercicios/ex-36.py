"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro
circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.14.
"""

a = float(input('Qual é a altura do cilindro cirular? '))
r = float(input('Qual é o raio do cilindro circular? '))
v = 3.14 * (r ** 2) * a

print(f'O volume do cilindro é: {v}')
