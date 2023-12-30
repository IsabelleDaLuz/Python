vel =  int(input('Qual é a velocidade? '))
multa = (vel - 80) * 7
if (vel > 80): 
    print('A sua multa foi de {} reais' .format(multa))
else: 
    print('Parabéns! Você não foi multado')
