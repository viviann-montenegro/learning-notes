"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e A a área em acres.
"""

m = int(input('Qual é o valor da área em metros quadrados? '))
a = m * 0.000247

print(f'O valor da área em metros quadrados: {m}m²')
print(f'O valor convertido em acres: {a}ac')
