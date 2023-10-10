p = float(input('Qual é o preço do produto?'))
d = (p / 100 * 5)
np =  p - d
print('Esse produto, com 5% de desconto, ficara no valor de R${:.2}'.format(np))