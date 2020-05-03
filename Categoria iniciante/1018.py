quantia = int(input())
dinheiro = quantia

notas100 = dinheiro // 100
dinheiro = dinheiro - (notas100 * 100)
notas50 = dinheiro // 50
dinheiro = dinheiro - (notas50 * 50)
notas20 = dinheiro // 20
dinheiro = dinheiro - (notas20 * 20)
notas10 = dinheiro // 10
dinheiro = dinheiro - (notas10 * 10)
notas5 = dinheiro // 5
dinheiro = dinheiro - (notas5 * 5)
notas2 = dinheiro // 2
dinheiro = dinheiro - (notas2 * 2)
notas1 = dinheiro // 1

print('%d'%quantia)
print('%d nota(s) de R$ 100,00'%notas100)
print('%d nota(s) de R$ 50,00'%notas50)
print('%d nota(s) de R$ 20,00'%notas20)
print('%d nota(s) de R$ 10,00'%notas10)
print('%d nota(s) de R$ 5,00'%notas5)
print('%d nota(s) de R$ 2,00'%notas2)
print('%d nota(s) de R$ 1,00'%notas1)
