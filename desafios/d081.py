
num = []
while True:
    num.append((int(input('Digite um valor: '))))
    c = input('Quer continuar? [S/N]')
    if c in 'Nn':
        break
print('-=-' *10)
print(f'Você digitou {len(num)} elementos')
print(f'Os valores que você digitou em ordem decrescente são: {num.sort(reverse=True)}')