"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
- O primeiro ganhador receberá 46%;
- O segundo ganhador receberá 32%;
- O terceiro ganhador receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

primeiro = (780000 * 46) / 100
segundo = (780000 * 32) / 100
terceiro = 780000 - primeiro - segundo

print('A quantia de R$ 780.000,00 será dividida entre três ganhadores de um concurso.')
print('O primeiro ganhará 46%, o segundo 32% e o terceiro fica com o restante.')
print(f'O primeiro ganhou: R${primeiro:.2f}')
print(f'O segundo ganhou: R${segundo:.2f}')
print(f'O terceiro ganhou: R${terceiro:.2f}')
