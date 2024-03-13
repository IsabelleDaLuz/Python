def voto(nasc):
    from datetime import datetime
    i = datetime.now().year - nasc
    if i < 16:
        print(f'Com {i} anos: NÃO VOTA')
    elif i < 18 or i > 65:
        print(f'Com {i} anos: VOTO OPCIONAL')
    else:
        print(f'Com {i} anos: VOTO OBRIGATÓRIO')

print('-'*30)
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)