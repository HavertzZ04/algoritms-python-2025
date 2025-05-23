lista = [1, 2, 3, 4, 5, 6]

def contar_pares(lista):
    return sum(1 for i in lista if i % 2 == 0)

print(f"La cantidad de numeros pares en la lista es {contar_pares(lista)}")