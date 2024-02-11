peso = 0
maior = 0
menor = 10000

for pess in range(1, 6):
    peso = float(input(f'Peso da {pess}ª pessoa'))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior} e o menor peso foi {menor}')