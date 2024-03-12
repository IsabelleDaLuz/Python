def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


num = int(input('Digite um número'))
print(f'O fatorial de {num} é {fatorial(num)}')