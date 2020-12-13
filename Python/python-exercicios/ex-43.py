"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
- O total a pagar com desconto de 10%;
- O valor de cada parcela, no parcelamento de 3x sem juros;
- A comissão do vendedor no caso da venda ser a vista (5% sobre o valor com desconto)
- A comissão do vendedor no caso da venda ser parcelada (5% sobre o valor total)
"""

vt = float(input('Hey vendedor, quanto custa o produto? '))
d = (vt * 10) / 100
vt2 = vt - d
p = vt / 3
com = vt2 * 5 / 100
com2 = vt * 5 / 100

print(f'O cliente pode ter 10% de desconto se pagar a vista e o produto fica em R${vt2:.2f}')
print(f'O valor de cada parcela do produto em 3x sem juros fica em R${p:.2f}')
print(f'A comissão do vendedor (5%) no caso da venda sendo a vista: R${com:.2f}')
print(f'A comissão do vendedor (5%) no caso da venda parcelada: R${com2:.2f}')
