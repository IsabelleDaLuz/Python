from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
i = atual - nasc
if i <= 9:
    print('Classificação MIRIM')
elif i <= 14:
    print('Classificação INFANTIL')
elif i <= 19:
    print('Classificação JUNIOR')
elif i <= 25:
    print('Classificação SENIOR')
else:
    print('Classificação MASTER')