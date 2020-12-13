"""
Leia uma distância em quilômetros e apresente-a convertida em milhas.
A fórmula de conversão é: m = k / 1.61, sendo K a distância em quilômetros e M em milhas.
"""

k = int(input('Qual é a distância atual? '))
m = k / 1.61

print(f'A distância atual em quilômetros: {k} Km')
print(f'A distância convertida em milhas: {m:.1f} mi')
