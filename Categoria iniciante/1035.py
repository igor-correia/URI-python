i = 0
numeros = input().split()
A = int(numeros[0])
B = int(numeros[1])
C = int(numeros[2])
D = int(numeros[3])
if B > C and D > A:
    if (C + D) > (A + B):
        if C >= 0 and D >= 0:
            if (A % 2) == 0:
                i = 1
if i == 1:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
    