sal = float(input('Qual é o salário do funcionário? '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else: 
    novo = sal + (sal * 10 / 100)
print('Quem ganhava {:.2f} vai passar a ganhar {:.2f}' .format(sal, novo))