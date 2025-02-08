import json


def traer_data_usuario(correo, db):

    docente = db["Docentes"].find_one({"correo": correo})
    if docente:
        print({"tipo": "docente", "datos": docente})
        return docente
    else:
        estudiante = db["Estudiantes"].find_one({"correo": correo})
        if estudiante:
            print({"tipo": "estudiante", "datos": estudiante})
            return estudiante
        else:
            print("No encontrado")
