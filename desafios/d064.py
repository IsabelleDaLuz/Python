num = 0
soma = num
c = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]'))
    c += 1
    soma += num
soma -= 999
c -= 1
print(f'Você digitou {c} e a soma entre eles foi {soma}')