"""
Leia um valor de comprimento em metros e apresente-o convertido em Jardas.
A fórmula de conversão é: J = M / 0.91, sendo J o comprimento em Jardas e M o comprimento em metros.
"""

m = float(input('Qual é o valor de comprimento em metros? '))
j = m / 0.91

print(f'O valor em metros: {m}m')
print(f'O valor convertido em jardas: {j:.2f}yd')
