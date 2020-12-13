"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = c / 2.54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""

c = float(input('Qual é o valor de comprimento em centímetros? '))
p = c / 2.54

print(f'O valor em centímetros: {c:.1f}cm')
print(f'O valor convertido em polegadas: {p}in')
