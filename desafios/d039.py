from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print(f'Você nasceu em {nasc} e tem {idade} anos')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    t = idade - 18
    ano -= t
    print(f'Você já deveria ter se alistado há {t} anos.\nSeu alistamento foi em {ano}')
else:
    t = 18 - idade
    print(f'Você vai ter que se alistar daqui {t} anos.')