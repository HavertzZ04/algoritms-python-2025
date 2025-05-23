def encontrar_faltante(lista):
    n = len(lista) + 1
    suma_esperada = n * (n + 1) // 2
    suma_real = sum(lista)
    return suma_esperada - suma_real
    

print(encontrar_faltante([1, 2, 3, 4, 5, 7])) 
