lista = [("Juan", 25), ("Ana", 22), ("Pedro", 30), ("Luis", 18)]

ordenar_tuplas = sorted(lista, key=lambda persona: persona[1])
   
print(ordenar_tuplas)