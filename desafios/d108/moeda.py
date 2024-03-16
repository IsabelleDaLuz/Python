def aumentar(preço = 0, taxa  = 0):
    res = preço + (preço * taxa/100)

def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res

def dobro(preço = 0):
    res = preço * 2
    return res

def metade(preço = 0):
    res = preço / 2
    return res

def moeda(preço = 0, moeda='R$'):
    return f'{moeda}{preço}'.replace('.',',')

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha():
            print('Preço invalido')
        else:
            valido=True
            return int(entrada)