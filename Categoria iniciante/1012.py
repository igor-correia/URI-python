linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

triangulo = (A * C)/2
circulo = 3.14159 * C ** 2
trapezio = (A + B) * C / 2
quadrado = B ** 2
retangulo = A * B

print('TRIANGULO: %.3f'%triangulo)
print('CIRCULO: %.3f'%circulo)
print('TRAPEZIO: %.3f'%trapezio)
print('QUADRADO: %.3f'%quadrado)
print('RETANGULO: %.3f'%retangulo)
