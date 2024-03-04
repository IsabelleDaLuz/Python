from random import randint
from time import sleep
print('-' * 7 +'JOGO DA MEGASENA' + '-'*7)
quant = int(input('Quantos jogos você quer jogar? '))
lista = list()
tot = 1
jogos = []
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=-=-=- Sorteando {quant} jogos -=-=-=-')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)