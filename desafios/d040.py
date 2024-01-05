n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print('Aluno aprovado')
elif m >= 5:
    print('Recuperação')

else:
    print('REPROVADO')