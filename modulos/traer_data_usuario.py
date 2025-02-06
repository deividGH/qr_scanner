import json


def traer_data_usuario(correo):

    # Leer el archivo JSON 
    with open("data/estudiantes.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # Aquí usamos json.load(), no json.loads()

    # Buscar el correo en la lista
    usuario_encontrado = next((item for item in data if item["correo"] == correo), None)

    # Si se encuentra, extraer código y nombre
    if usuario_encontrado:
        codigo = usuario_encontrado["codigo"]
        nombre = usuario_encontrado["nombre"]
        print(f"Correo encontrado: {correo}")
        print(f"Código: {codigo}")
        print(f"Nombre: {nombre}")
        return codigo, nombre
    else:
        print("Correo no encontrado.")
        return None, None