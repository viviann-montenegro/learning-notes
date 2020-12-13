"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
"""

h = float(input('Digite o valor da área em hectares: '))
m = h * 10000

print(f'O valor da área em hectares: {h} ha')
print(f'O valor convertido em metros quadrados: {m} m²')
