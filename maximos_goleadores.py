goles = [
    ("Messi", 3),
    ("Ronaldo", 2),
    ("Mbappé", 5),
    ("Haaland", 4),
    ("Neymar", 1),
    ("Messi", 2),
    ("Ronaldo", 6),
    ("Mbappé", 2),
    ("Haaland", 1),
    ("Neymar", 3)
]

total_goles = {}

for jugador, cantidad in goles:
    if jugador in total_goles:
        total_goles[jugador] += cantidad
    else:
        total_goles[jugador] = cantidad

max_goles = max(total_goles.values())

goleadores = [jugador for jugador, goles in total_goles.items() if goles == max_goles]

print("📊 Total de goles por jugador:")
for jugador, goles in total_goles.items():
    print(f"{jugador}: {goles} goles")

print("\n🏆 Máximo goleador(es):")
for goleador in goleadores:
    print(f"{goleador} con {max_goles} goles")

print("\n📈 Ranking de goleadores:")
ranking = sorted(total_goles.items(), key=lambda x: x[1], reverse=True)
for jugador, goles in ranking:
    print(f"{jugador}: {goles} goles")
