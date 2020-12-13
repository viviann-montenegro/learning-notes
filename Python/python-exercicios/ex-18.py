"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos.
"""

m = int(input('Qual é o valor do volume? '))
l = 1000 * m

print(f'O valor em metros cúbicos: {m}m³')
print(f'O valor convertido em litros: {l}L')
