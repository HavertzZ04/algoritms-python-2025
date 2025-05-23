texto = "Hola Mundo"

def contar_vocales(texto):
    numero_vocales = 0
    vocales = set("aeiou")
    texto = texto.lower()
    
    for i in texto:
        if i in vocales:
            numero_vocales += 1
    return numero_vocales

resultado = contar_vocales(texto)
print(f"La cantidad de vocales en el texto es {resultado}")
