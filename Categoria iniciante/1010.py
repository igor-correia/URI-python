linha1 = input().split( )
linha2 = input().split( )

linha1[0]=int(linha1[0])
linha1[1]=int(linha1[1])
linha1[2]=float(linha1[2])

linha2[0]=int(linha2[0])
linha2[1]=int(linha2[1])
linha2[2]=float(linha2[2])

total = linha1[1] * linha1[2] + linha2[1] * linha2[2]
print('VALOR A PAGAR: R$ %.2f'%total)
