productos = {
    "Manzanas": [3.50, 10],
    "Pan": [1.20, 5],
    "Queso": [5.80, 2],
    "Leche": [2.30, 7],
    "Huevos": [4.10, 12],
    "Agua": [0.99, 20]
}

carrito = [("Pan", 2), ("Leche", 3), ("Queso", 1), ("Huevos", 15)]

def calcular_total(carrito):
    total = 0

    for nombre, cantidad in carrito:
        if nombre in productos:
            precio, stock = productos[nombre]
            if cantidad <= stock:
                subtotal = cantidad * precio
                total += subtotal
                productos[nombre][1] -= cantidad
                print(f"{nombre} x{cantidad} = ${subtotal:.2f}")
            else:
                print(f"No hay suficiente stock de {nombre}. Solo quedan {stock} unidades.")
        else:
            print(f"Producto {nombre} no encontrado.")
    
    print(f"\nTotal a pagar: ${total:.2f}")

calcular_total(carrito)
