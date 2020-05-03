dinheiro = float(input())

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
moedas1 = dinheiro // 1
dinheiro = dinheiro - (moedas1 * 1)
moedas50 = dinheiro // 0.5
dinheiro = dinheiro - (moedas50 * 0.5)
moedas25 = dinheiro // 0.25
dinheiro = dinheiro - (moedas25 * 0.25)
moedas10 = dinheiro // 0.10
dinheiro = dinheiro - (moedas10 * 0.10)
moedas5 = dinheiro // 0.05
dinheiro = dinheiro - (moedas5 * 0.05)
moedas01 = dinheiro / 0.01

print('NOTAS:')
print('%d nota(s) de R$ 100.00'%notas100)
print('%d nota(s) de R$ 50.00'%notas50)
print('%d nota(s) de R$ 20.00'%notas20)
print('%d nota(s) de R$ 10.00'%notas10)
print('%d nota(s) de R$ 5.00'%notas5)
print('%d nota(s) de R$ 2.00'%notas2)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00'%moedas1)
print('%d moeda(s) de R$ 0.50'%moedas50)
print('%d moeda(s) de R$ 0.25'%moedas25)
print('%d moeda(s) de R$ 0.10'%moedas10)
print('%d moeda(s) de R$ 0.05'%moedas5)
print('%.0f moeda(s) de R$ 0.01'%moedas01)
