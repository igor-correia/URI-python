cardapio = {1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}
pedido = input().split()
codigo = int(pedido[0])
quant = int(pedido[1])
preco = cardapio.get(codigo)
total = preco * quant
print('Total: R$ %.2f'%total)
