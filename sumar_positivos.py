numeros = [3, -1, 4, -2, 7, -5, 2]

def sumar_positivos(numeros):
    suma = 0
    for i in numeros:
        if i > 0:
            suma += i
    
    print(f"La suma de los numeros positivos es {suma}")
    
sumar_positivos(numeros)