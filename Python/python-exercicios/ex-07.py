"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula
de conversão é: C = 5 * (F - 32) / 9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

f = float(input('Qual é a temperatura de hoje em Fahrenheit ºF? '))
c = 5 * (f - 32) / 9

print(f'A temperatura de hoje em Celsius é de {c}ºC')
