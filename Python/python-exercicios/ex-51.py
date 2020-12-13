"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule a sua distância da origem (0, 0).
"""

x1 = 0.0
y1 = 0.0

x2 = float(input('Informe a coordenada X: '))
y2 = float(input('Informe a coordenada y: '))

r = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

print(f'A distância é {r}')
