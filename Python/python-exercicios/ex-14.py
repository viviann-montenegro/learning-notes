"""
Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * pi / 180, sendo G o ângulo em graus e R em radianos e pi = 3.14.
"""

g = int(input('Qual é o valor que vamos utilizar considerando graus de um ângulo? '))
r = g * 3.14 / 180

print(f'Ok. Então estamos tratando de {g}º')
print(f'Determinado valor convertido em radianos: {r:.2f}rad')
