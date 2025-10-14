precios = {"pantalos" : 20, "camisa" : 10, "zapatos" : 50}
for item in range(len(precios)):
    precio_total = sum(precios.values())
print(f"el precio total de la compra es de {precio_total}$")