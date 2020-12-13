"""
Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180 / pi, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""

r = float(input('Qual é o valor que vamos utilizar considerando radianos de um ângulo? '))
g = r * 180 / 3.14

print(f'Ok. Então temos aqui {r:.2f}rad')
print(f'Determinado valor convertido em graus: {g:.0f}º')
