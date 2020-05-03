idade = int(input())

anos = idade // 365
idade = idade - (365 * anos)
meses = idade // 30
idade = idade - (30 * meses)

print('%d ano(s)'%anos)
print('%d mes(es)'%meses)
print('%d dia(s)'%idade)
