"""
Leia uma velocidade em m/s e apresente-a convertida em km/h.
A fórmula de conversão é: K = m * 3.6, sendo K a velocidade em km/h e M em m/s.
"""

m = float(input('Qual é a velocidade atual? '))
k = m * 3.6

print(f'A velocidade em m/s: {m:.2f} m/s')
print(f'A velocidade convertida em Km/h: {k:.0f} Km/h')
