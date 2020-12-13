"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula
de conversão é: C = K - 273.15, sendo K a temperatura em Kelvin e C a temperatura em Celsius.
"""

k = float(input('Qual é a temperatura de hoje em Kelvin K? '))
c = k - 273.15

print(f'A temperatura de hoje em Celsius é de {c}ºC')
