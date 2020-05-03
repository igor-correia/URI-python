numeros = input().split()
A = float(numeros[0])
B = float(numeros[1])
C = float(numeros[2])
delta = (B ** 2) - 4 * A * C
if delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    r1 = (-B + delta ** (1/2)) / (2 * A)
    r2 = (-B - delta ** (1/2)) / (2 * A)
    print('R1 = %.5f'%r1)
    print('R2 = %.5f' % r2)
    