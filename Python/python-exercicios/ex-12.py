"""
Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros e M em milhas.
"""

m = int(input('Qual é a distância atual? '))
k = 1.61 * m

print(f'A distância em milhas: {m} mi')
print(f'A distância convertida em quilômetros: {k:.0f} Km')
