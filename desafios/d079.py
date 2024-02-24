num = []
while True:
    n = (int(input('Digite um valor: ')))
    c = input('Quer continuar? [S/N]')
    if n not in num:
        num.append(n)
    else:
        print('Valor já digitado')
    if c in 'Nn':
        break
num.sort()
print(f'Você digitou os valores {num}')