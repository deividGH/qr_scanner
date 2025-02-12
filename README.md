# Proyecto final tendencias avanzadas de ingeniería de software/ factores humanos


### Para ejecutar el proyecto:
- Crear un ambiente virtual
- Ejecutar el comando `pip install -r requirements.txt` para instalar las dependencias necesarias
- Crear base de datos mongo nombrada `QR_Scanner` (Si cambia el nombre, debe actualizarse en la línea 9 del archivo *login.py*)
- Crear colecciones usando los archivos del directorio `colecciones mongo`
- Ejecutar con el comando `python main.py`
- Usar los atributos correo y contraseña de las colecciones *Docente* y *Estudiantes* para el login

#### ***Consideraciones***:
- Una sesión de clase debe ser inicializada por un docente para pode recibir registros de estudiantes
- El programa usa la fecha y hora del sistema para validar si hay cursos activos. Al menos un curso de la base de datos debe contener la hora local con el nombre del día actual para poder registrar asistencia