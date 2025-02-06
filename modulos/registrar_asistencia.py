import json

def registrar_asistencia(id_salon_escaneado, archivo_json, nombre, codigo, correo, fecha):
    try:
        with open(archivo_json, "r", encoding="utf-8") as f:
            asistencias = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        asistencias = []

    data_asistencia = {
        "nombre": nombre,
        "codigo": codigo,
        "correo": correo,
        "fecha" : fecha
    }


    for registro in asistencias:
        if registro["id_salon"] == id_salon_escaneado:
            registro["estudiantes"].append(data_asistencia)


    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(asistencias, f, indent=4, ensure_ascii=False)

    print("Asistencia registrada correctamente")

