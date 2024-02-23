listanum = []
for c in range(0, 5):
    listanum.append(int(input(f' Digite um valor para a posição {c}')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]


print(f'Você digitou os valores {listanum}')
print(f'O maior valor foi {mai} na(s) posição(s) ')
print(f'O maior valor foi {men} na(s) posição(s) ')