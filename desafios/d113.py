def leiaInt(msg):
    val = False
    while val is False:
        try:
            num = int(input(msg))
        except:
            print('\033[031mERRO! Por favor, digite um número inteiro válido\033[m')
            continue
        else:
            val = True
            return num
            break
def leiaFloat(msg):
    val = False
    while val is False:
        try:
            num = float(input(msg))
        except:
            print('\033[031mERRO! Por favor, digite um número real válido \033[m')
            continue
        else:
            val = True
            return num
            break
int = leiaInt('Digite um número inteiro: ')
float = leiaFloat('Digite um número real: ')
print(f'O valores digitados foram {int} e {float}')