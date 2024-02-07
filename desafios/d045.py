from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas Jogadas:
[0] Pedra
[1] Papel
[2] Tesoura
''')
jogador = int(input('Qual é sua jogada?'))

if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2: 
        print('Computador vence!')
    else:
        print('JOGADA INVÁLIDA!!!')
elif computador == 1:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Emapte!!!')
    elif jogador == 2: 
        print('Computador vence!')
    else:
        print('JOGADA INVÁLIDA!!!')
elif computador == 2: 
    if jogador == 0:
         print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2: 
        print('Empate!')
    else:
        print('JOGADA INVÁLIDA!!!')
else:
    print('JOGADA INVÁLIDA!!!')

print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')