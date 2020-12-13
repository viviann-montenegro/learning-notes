"""
Faça um programa que leia o valor da hora de trabalho (em reais) e o número de horas trabalhadas no mês. Imprima
o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

h = int(input('Qual é o valor da hora de trabalho em reais? '))
m = int(input('Quantas horas o funcionário trabalhou no mês? '))
vsalario = h * m
vsalario2 = (vsalario * 10) / 100

print(f'O funcionário vai receber o valor de R${vsalario+vsalario2:.2f} com 10% de aumento.')
