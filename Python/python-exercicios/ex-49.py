"""
Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração em segundos, de uma experiência
biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do término da experiência Bio.
"""

s = int(input('Quantos segundos desde o início? '))
d = int(input('Quantas horas de duração de experiência biológica? '))
h = s / 3600 * 100
m = s / 60

print(f'Hora de início: {h:.0f}h')
print(f'Min. de início: {m:.0f}min')
print(f'Seg. de início: {s}s')
print(f'{d - h:.0f}h para o término')
print(f'{(d - h) * 60:.0f}min para o término')
print(f'{(d - h) * 3600:.0f}s para o término')
