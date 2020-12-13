"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula
de conversão é: K = C + 273.15, sendo K a temperatura em Kelvin e C a temperatura em Celsius.
"""

c = float(input('Qual é a temperatura de hoje em graus Celsius ºC? '))
k = c + 273.15

print(f'A temperatura de hoje em Kelvin é de {k}K')
