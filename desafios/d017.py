from math import hypot
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)
print ('A hipotenusa vai medir {:.2}'.format(hi))