"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
NúmeroLido = 123
NúmeroGerado = 321
"""

num = int(input('Digite um número de três dígitos: '))
n = str(num)

print(n[::-1])
