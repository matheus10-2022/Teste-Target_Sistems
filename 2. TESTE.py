n = int(40)
cont = int(0)
v1 = int(-1)
v2 = int(1)
lista_fibo = []
while cont <= n:
    v3 = v1 + v2
    lista_fibo.append(v3)
    v1 = v2
    v2 = v3
    cont += 1

print('Sequência de Fibonacci')
vf = int(input('Digite um numero: '))

if vf in lista_fibo:
    print(f'O número {vf} se encontra na sequência de Fibonnaci.')
else:
    print('O número não se encontra na sequência de Fibonnaci.')
