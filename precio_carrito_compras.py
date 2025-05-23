productos = [
    ("Manzanas", 3.50),
    ("Pan", 1.20),
    ("Queso", 5.80),
    ("Leche", 2.30),
    ("Huevos", 4.10),
    ("Agua", 0.99)
]

carrito = ["Pan", "Leche", "Queso"]

def calculo_carrito(carrito):
    precios = [i for i in productos if i[0] in carrito]
    precios_ordenados = sorted(precios,  key=lambda producto: producto[1])
    
    pago_total = sum([x[1] for x in precios_ordenados])
    
    print(f"Total a pagar: ${pago_total:.2f}")
    print(f"Producto mas barato: {precios_ordenados[0][0]} (${precios_ordenados[0][1]:.2f})")
    print(f"Producto mas caro: {precios_ordenados[-1][0]} (${precios_ordenados[-1][1]:.2f})")
    
calculo_carrito(carrito)
        