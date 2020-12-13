"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

num1 = int(input('Digite um número: '))

print(f'A soma do sucessor de seu triplo com o antecessor de seu dobro: {(num1 * 3 + 1) + (num1 * 2 - 1)}')
