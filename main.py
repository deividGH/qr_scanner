from modulos.qr_scanner import qr_scanner
from modulos.registrar_asistencia import registrar_asistencia
from modulos.login import ejecutar_login
from modulos.traer_data_usuario import traer_data_usuario
from datetime import datetime

# Login
correo = ejecutar_login()

# Leer data del usuario
codigo, nombre = traer_data_usuario(correo)

print(f"Ingreso correcto para {nombre} con código {codigo}")

# Abrir la cámara para escanear el qr
data_qr = qr_scanner()

# Obtener data del QR
id_salon_escaneado = data_qr.get("salon",404)
archivo_json = "data/asistencias.json"
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Actualizar archivo de asistencia
registrar_asistencia(id_salon_escaneado, archivo_json, nombre, codigo, correo, fecha)




