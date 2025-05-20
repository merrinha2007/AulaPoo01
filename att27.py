valor = float(input("Qual valor da sua compras? "))

if valor >= 500:
    desconto = valor- (valor *0.10) 
    print(f"O seu desconto valor de de {desconto}")
else:
    desconto = valor - (valor *0.05)
    print(f"O seu desconto valor de de {desconto}")