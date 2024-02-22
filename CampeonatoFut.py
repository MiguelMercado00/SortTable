def generar_tabla_posiciones(equipos):
    # Ordenar equipos por puntos, diferencia de goles y goles marcados
    equipos_ordenados = sorted(equipos, key=lambda x: (x['Puntos'], x['Diferencia de goles'], x['Goles marcados']),
                               reverse=True)

    # Mostrar tabla de posiciones
    print("Tabla de Posiciones:")
    print("{:<10} {:<7} {:<15} {:<15} {:<15}".format('Equipo', 'Puntos', 'Dif. Goles', 'Goles Marcados',
                                                     'Goles en Contra'))

    # Mostrar equipos ordenados
    for i, equipo in enumerate(equipos_ordenados, start=1):
        print("{:<10} {:<7} {:<15} {:<15} {:<15}".format(equipo['Nombre'], equipo['Puntos'],
                                                         equipo['Diferencia de goles'], equipo['Goles marcados'],
                                                         equipo['Goles en contra']))


# Ejemplo de uso
if __name__ == "__main__":
    equipos = []

    # Permitir al usuario ingresar equipos
    while True:
        nombre = input("Ingrese el nombre del equipo (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
            # Obtener datos del equipo
        puntos = int(input("Ingrese los puntos del equipo: "))
        goles_marcados = int(input("Ingrese los goles marcados del equipo: "))
        goles_contra = int(input("Ingrese los goles en contra del equipo: "))

        # Calcular diferencia de goles
        diferencia_goles = goles_marcados - goles_contra

        # Agregar equipo a la lista de equipos
        equipos.append({
            'Nombre': nombre,
            'Puntos': puntos,
            'Goles marcados': goles_marcados,
            'Goles en contra': goles_contra,
            'Diferencia de goles': diferencia_goles
        })

    # Generar y mostrar tabla de posiciones
    generar_tabla_posiciones(equipos)
