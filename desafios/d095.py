time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?')).lower()[0]
        if resp in 'sn':
            break
        print('Erro! Responda apenas S ou N')
    if resp in 'Nn':
        break

print('-=-' * 30)
for k,v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
print('-=-' * 30)
