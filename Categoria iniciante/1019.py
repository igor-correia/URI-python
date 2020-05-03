tempo = int(input())

hora = tempo // 3600
tempo = tempo - (3600 * hora)
minuto = tempo // 60
tempo = tempo - (60 * minuto)

print('%d:%d:%d'%(hora,minuto,tempo))
