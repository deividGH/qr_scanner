

def traer_data_cursos(db, salon, hora, dia):
    cursos = db["Cursos"]

    # Buscar el curso activo en ese salón y horario
    curso_actual = cursos.find_one({
        "id_salon": salon,
        "horario": {
            "$elemMatch": {
                "dia": dia,
                "hora_inicio": {"$lte": hora},  # La clase ya inició
                "hora_fin": {"$gte": hora}      # La clase aún no ha terminado
            }
        }
    })

    # Mostrar el curso activo
    if curso_actual:
        print(f"Curso activo en {salon}: {curso_actual['nombre']} con {curso_actual['docente']}")
        return curso_actual
    else:
        print(f"No hay curso activo en el salón {salon} en este momento.")
