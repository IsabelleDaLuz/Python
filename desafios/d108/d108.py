from moeda import dobro, metade, aumentar
p = int(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${metade(p)}')
print(f'O dobro de R${p} é R${dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
