"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.
"""

a = float(input('Qual é o valor de área em acres? '))
m = a * 4048.58

print(f'O valor da área em acres: {a} ac')
print(f'O valor convertido em metros quadrados: {m} m²')
