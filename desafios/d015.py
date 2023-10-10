dia = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos km você rodou?'))
pago = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}' .format(pago))