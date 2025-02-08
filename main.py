from modulos.qr_scanner import qr_scanner
from modulos.registrar_asistencia import inicializar_clase,registrar_asistencia
from modulos.login import ejecutar_login
from modulos.traer_data_usuario import traer_data_usuario
from modulos.traer_data_cursos import traer_data_cursos
from datetime import datetime
import locale
from datetime import datetime


# Login
correo, db = ejecutar_login()


# Leer data del usuario
usuario = traer_data_usuario(correo, db)

# Escanear QR para obtener el salón 
data_qr = qr_scanner()
id_salon_escaneado = data_qr.get("salon",404)

# Obtener fecha, hora y día actual 
locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')  
hora_actual = datetime.now().strftime("%H:%M:%S")  
dia_actual = datetime.today().strftime("%A").lower()
fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Buscar data del curso según el horario:
curso = traer_data_cursos(db, id_salon_escaneado, hora_actual, dia_actual)

# Ejecución de flujo según tipo de usuario

if(usuario["tipo_usuario"] == "docente"): # Si es docente inicializa una sesión de asistencia
    inicializar_clase(usuario,curso,id_salon_escaneado,fecha_actual, dia_actual, hora_actual, db["Asistencia"])

else:
    registrar_asistencia(usuario, curso, db, id_salon_escaneado, fecha_actual, hora_actual, dia_actual) # Si es estudiante registra asistencia sobre una sesión inicializada




