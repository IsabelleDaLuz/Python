from operator import itemgetter
from random import randint
from time import sleep
jogos = {'1': randint(1,6), '2': randint(1,6), '3': randint(1,6), '4': randint(1,6)}
print('Valores sorteados: ')
ranking = dict()
for k, v in jogos.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: Jogador {v[0]} com {v[1]} no dado')