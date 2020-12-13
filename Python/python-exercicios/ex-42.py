"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse
funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de
imposto sobre o salário-base.
"""

base = float(input('Qual é o salário base do funcionário? '))
gr = (base * 5) / 100
IR = (base * 7) / 100
salariofinal = (base - IR) + gr

print(f'O funcionário vai receber R${salariofinal:.2f} com gratificação de 5% e desconto de IR em 7%.')
