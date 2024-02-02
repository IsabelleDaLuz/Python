preco = float(input('Qual é o preço? '))
total = 0
print(''' -=-=-=- FORMAS DE PAGAMENTO -=-=-=-
    [1] A vista - dinheiro/cheque     
    [2] A vista - cartão
    [3] 2x - cartão
''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
else:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela}')
print(f'Sua compra de R${preco} vai custar R${total} no final')