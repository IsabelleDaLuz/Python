km = int(input('Informe quantos km você irá percorrer na viagem: '))
if (km <= 200):
    preço = .5 * km
else:
    preço = .45 * km

print('A viagem custará', preço)