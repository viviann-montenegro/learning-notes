"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula
de conversão é: F = C * (9 / 5) + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

c = float(input('Qual é a temperatura de hoje em graus Celsius ºC? '))
f = c * (9 / 5) + 32

print(f'A temperatura de hoje em Fahrenheit é de {f}ºF')
