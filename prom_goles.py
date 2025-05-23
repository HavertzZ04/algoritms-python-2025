goles_por_partido = [2, 1, 3, 0, 1]

def calculador_promedio_goles(goles_por_partido):
    total_goles = sum(goles_por_partido)
    return round(total_goles / len(goles_por_partido), 2)

print(calculador_promedio_goles(goles_por_partido))