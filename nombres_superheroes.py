import random

def crear_superheroe(adjetivos, sustantivos):
    heroe_adjetivo = random.choice(adjetivos)
    heroe_sustantivo = random.choice(sustantivos)
    numero = random.randint(0, 100)
    
    if list(heroe_sustantivo)[-1].lower() == 'a': 
        print(f"Tu nombre de superheroe es: La {heroe_adjetivo} {heroe_sustantivo} #{numero}")
    else:
        print(f"Tu nombre de superheroe es: El {heroe_adjetivo} {heroe_sustantivo} #{numero}")
    
adjetivos = [
    "Increíble", "Veloz", "Poderoso", "Misterioso", "Invencible",
    "Asombroso", "Feroz", "Brillante", "Oscuro", "Radiante",
    "Audaz", "Fantástico", "Glorioso", "Imparable", "Magnífico",
    "Salvaje", "Legendario", "Despiadado", "Justiciero", "Valiente"
]

sustantivos = [
    "Tigre", "Dragón", "Fénix", "Lobo", "Pantera",
    "Relámpago", "Tormenta", "Sombra", "Halcón", "Centella",
    "Tornado", "Rayo", "Bestia", "Serpiente", "Cóndor",
    "Martillo", "Espada", "Guardián", "Trueno", "Escorpión"
]

crear_superheroe(adjetivos, sustantivos)
