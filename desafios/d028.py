import random
num = [1,2,3,4,5]
sorteado = random.choice(num)

print('-=-' *10)
print('ADIVINHE O NÚMERO!')
print('-=-' *10)
n = int(input('Digite um número de 1 a 5: ')) 
if (n == sorteado):
    print('Você acertou o número!')
else:
    print('Você errou o número, o sorteado foi ', sorteado)