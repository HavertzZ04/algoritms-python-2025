productos = [
    ("Manzanas", 3.50),
    ("Pan", 1.20),
    ("Queso", 5.80),
    ("Leche", 2.30),
    ("Huevos", 4.10),
    ("Agua", 0.99)
]

def ordenar_precios(productos):
    productos_ordenados = sorted(productos, key=lambda producto: producto[1])
    productos_baratos = [producto for producto in productos_ordenados if producto[1] < 3]
    
    print("Productos ordenados de menor a mayor precio:")
    for nombre, precio in productos_ordenados:
        print(f"{nombre} = ${precio:.2f}")

    print("\nProductos precio menor a 3.00:")
    for nombre, precio in productos_baratos:
        print(f"{nombre} = ${precio:.2f}")

ordenar_precios(productos)