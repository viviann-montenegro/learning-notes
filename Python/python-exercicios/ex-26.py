"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H a área em hectares.
"""

m = float(input('Digite o valor da área em metros quadrados: '))
h = m * 0.0001

print(f'O valor da área em metros quadrados: {m} m²')
print(f'O valor convertido em hectares: {h} ha')
