import json
from tkinter import messagebox

def inicializar_clase(usuario, curso, salon, fecha, dia, hora, asistencias):


    sesion_existente = asistencias.find_one({
        "id_salon": salon,
        "id_curso": curso["_id"],
        "fecha": fecha,
        "horario": {
            "$elemMatch": {
                "dia": dia,
                "hora_inicio": {"$lte": hora},  # La clase ya inició
                "hora_fin": {"$gte": hora}      # La clase aún no ha terminado
            }
        }
    })

    if sesion_existente:
        messagebox.showwarning("Aviso", f"Ya existe una sesión de asistencia para el curso {curso['nombre']} en el salón {salon} a las {hora} el {fecha}.")
        return  # Evita la inserción
    
    # Insertar un documento de sesión de asistencia
    asistencias.insert_one({
        "id_salon": salon,
        "id_curso": curso["_id"],
        "nombre_curso": curso["nombre"],
        "docente": usuario["nombre"],
        "fecha": fecha,
        "hora": hora,
        "dia": dia,
        "horario": curso["horario"],
        "estudiantes": []
    })

    messagebox.showinfo(f"Curso: {curso["_id"]}, {curso["nombre"]}", f"{usuario["nombre"]} ha iniciado una sesión de clase en el salón {salon} a las {hora}")

def registrar_asistencia(usuario, curso, db, salon, fecha, hora, dia):
    asistencia = db["Asistencia"]

    # Buscar el curso activo en ese salón y horario
    sesion_asistencia = asistencia.find_one({
        "id_salon": salon,
        "fecha": fecha,
        "horario": {
            "$elemMatch": {
                "dia": dia,
                "hora_inicio": {"$lte": hora},  # La clase ya inició
                "hora_fin": {"$gte": hora}      # La clase aún no ha terminado
            }
        }
    })

    if not sesion_asistencia:
        messagebox.showerror("Error", f"No hay una clase iniciada en el salón {salon} en este momento. Por favor espere la llegada del docente")
        return
    
    # Verificar si el estudiante ya está en la lista de asistencia
    estudiante_existente = any(estudiante["codigo"] == usuario["_id"] for estudiante in sesion_asistencia["estudiantes"])

    if estudiante_existente:
        messagebox.showwarning("Aviso", f"{usuario['nombre']} ya ha registrado asistencia para esta clase.")
        return

    # Registro del nuevo estudiante
    nuevo_estudiante = {
        "codigo": usuario["_id"],
        "nombre": usuario["nombre"],
        "correo": usuario["correo"],
        "hora": hora
    }

    asistencia.update_one(
        {"_id": sesion_asistencia["_id"]},  # Filtrar por el ID
        {"$push": {"estudiantes": nuevo_estudiante}}  # Agregar al array estudiantes
    )

    messagebox.showinfo(f"Curso: {curso['_id']}, {curso['nombre']}", f"Asistencia registrada correctamente - Hora llegada: {hora}")

