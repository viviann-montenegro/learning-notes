"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados
pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para o
imposto de renda.
"""

s = int(input('Foram quantos dias que o encanador trabalhou? '))
d = 30 * s
des_imposto = (d * 8) // 100
l = d - des_imposto

print(f'O encanador vai receber o valor, com 8% descontados de IR, de: R${l:.2f}')
