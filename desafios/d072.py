
cont = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze' ,'treze' ,'quatorze' ,'quinze', 'desesseis', 'desesete', 'dossoito', 'desenove' ,'vinte'

while True:
    num = int(input('Digite umm número: '))
    if num < 0 or num > 20:
        print('[Erro] Digite um número entre 0 e 20')
        break
    print(f'Você digitou o número {cont[num]}')