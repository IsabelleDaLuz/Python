a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c1 = int(input('Terceiro valor: '))
maior = a 
if b>a and b>c:
    maior=b 
if c>b and c>a:
    maior=c 
menor = a
if b<a and b<c:
    menor=b 
if c<b and c<a:
    menor=c 
print('O menor número é {} e o maior número é {}' .format(menor, maior))