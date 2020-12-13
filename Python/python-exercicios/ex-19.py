"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume em metros cúbicos.
"""

l = int(input('Qual é o valor do volume? '))
m = l / 1000

print(f'O valor do volume em litros: {l}L')
print(f'O valor convertido em metros cúbicos: {m}m³')
