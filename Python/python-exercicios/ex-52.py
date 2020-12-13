"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor
que cada um deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor
do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

num1 = int(input('Valor do amigo X: '))
num2 = int(input('Valor do amigo Y: '))
num3 = int(input('Valor do amigo Z: '))
total = int(input('Qual é o valor do prêmio? '))

print(f'O apostador X investiu R${num1:.2f} e ganhou R${(num1 + total) / 3:.2f}')
print(f'O apostador Y investiu R${num2:.2f} e ganhou R${(num2 + total) / 3:.2f}')
print(f'O apostador Z investiu R${num3:.2f} e ganhou R${(num3 + total) / 3:.2f}')
print(f'O valor do prêmio é: R${total:.2f}')
