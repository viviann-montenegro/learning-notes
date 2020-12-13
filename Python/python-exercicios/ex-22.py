"""
Leia um valor de comprimento em Jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em Jardas e M o comprimento em metros.
"""

j = int(input('Qual é o valor de comprimento em jardas? '))
m = 0.91 * j

print(f'O valor em jardas: {j}yd')
print(f'O valor convertido em metros: {m}m')
