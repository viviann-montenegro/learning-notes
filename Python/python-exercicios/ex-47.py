"""
Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""

num = int(input('Digite um número inteiro de 4 dígitos: '))
n = str(num)

print(f'Primeiro dígito: {n[0]}')
print(f'Segundo dígito: {n[1]}')
print(f'Terceiro dígito: {n[2]}')
print(f'Quarto dígito: {n[3]}')
