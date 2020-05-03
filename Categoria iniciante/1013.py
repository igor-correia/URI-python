num = input().split( )
a = int(num[0])
b = int(num[1])
c = int(num[2])
maiorab = (a + b + abs(a - b))/2
maior = (maiorab + c + abs(maiorab - c))/2
print('%d eh o maior'%maior)
