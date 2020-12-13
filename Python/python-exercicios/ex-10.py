"""
Leia uma velocidade em Km/h e apresente-a convertida em m/s.
A fórmula de conversão é: m = k / 3.6, sendo K a velocidade em Km/h e M em m/s.
"""

k = int(input('Qual é a velocidade atual? '))
m = k / 3.6

print(f'A velocidade em Km/h: {k} Km/h')
print(f'A velocidade convertida em m/s: {m:.2f} m/s')
