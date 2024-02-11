from random import randint
comp = randint(0,10)
print('Sou eu, seu computador! Acabei de pensar em um número entre 0 e 10. Tente adivinhar!')
acertou = False
palpite = 0
while not acertou:
    jog = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais... tente outra vez!')
        else:
            print('Menos... tente outra vez!')
print(f'Acertou com {palpite} tentativas, parabéns!')