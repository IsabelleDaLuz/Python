print('\033[35m-=-\033[m' *10) 
print('ANALISADOR DE EMPRÉSTIMO BANCÁRIO') 
print('\033[35m-=-\033[m' *10)

val = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
ano = float(input('Em quantos anos você vai querer pagar a casa? '))

par = val / ano

if par < (sal * 30 / 100):
    print('Cada parcela irá custar', par)
else:
    print('Você não pode comprar esta casa.')