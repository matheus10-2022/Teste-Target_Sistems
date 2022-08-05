nome = str(input('Digite uma palavra: '))
lista = []
tam = len(nome)
while tam > 0:
    lista += nome[tam-1]
    tam -= 1
invertido = ''.join(lista)
print(f'Palavra invertida: {invertido}')
