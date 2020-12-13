"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuário deverá subir para atingir o seu objetivo.
"""

a = float(input('Qual é a altura do degrau da escada (cm)? '))
ab = float(input('Qual é a altura que você deseja alcançar subindo a escada (metros)? '))
x = (ab * 100) / a

print(f'O usuário deverá subir {x:.0f} degraus para alcançar o objetivo.')
