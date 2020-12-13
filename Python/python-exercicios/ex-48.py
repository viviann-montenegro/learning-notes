"""
Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos.
"""

s = int(input('Quantos segundos? '))
h = s / 3600 * 100
m = s / 60

print(f'O primeiro valor: {h:.0f}h')
print(f'O segundo valor: {m:.0f}min')
print(f'O terceiro valor: {s:.0f}s')
