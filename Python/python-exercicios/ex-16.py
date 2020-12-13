"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""

p = float(input('Qual é o valor de comprimento em polegadas? '))
c = p * 2.54

print(f'O valor de comprimento em polegadas: {p}in')
print(f'O valor convertido em centímetros: {c}cm')
