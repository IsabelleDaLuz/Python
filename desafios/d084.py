nome = list()
peso = []
resp = 's'
mai = men = 0
c = 0
while True:
    if resp in 'Ss':
        nome.append(str(input('Nome: ')))
        peso.append(float(input('Peso: ')))
        if len(peso) == 0:
            mai = men = nome[c], peso[c]
        else:
            if peso[c] > mai:
                mai = [nome[c],peso[c]]
            if peso[c] < men:
                men = [nome[c],peso[c]]
        resp = str(input('Quer continuar? [S/N] '))
        c += 1
    else: 
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(nome)} pessoas')
print(f'O maior peso foi de {mai}')
