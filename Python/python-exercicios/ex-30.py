"""
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""

r = float(input('Quantos reais você tem na carteira? '))
d = r / 4.88

print(f'O valor em reais: R${r:.2f}')
print(f'O valor convertido em dólar americano na data 08/06/2020: US${d:.2f}')
