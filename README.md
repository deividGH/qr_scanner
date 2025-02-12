# Proyecto final tendencias avanzadas de ingeniería de software/ factores humanos


### Para ejecutar el proyecto:
- Crear un ambiente virtual
- Ejecutar el comando `pip install -r requirements.txt` para instalar las dependencias necesarias
- Crear base de datos mongo nombrada `QR_Scanner` (Si cambia el nombre, debe actualizarse en la línea 9 del archivo *login.py*)
- Crear colecciones usando los archivos del directorio `colecciones mongo`
- Ejecutar con el comando `python main.py`
- Usar los atributos correo y contraseña de las colecciones *Docente* y *Estudiantes* para el login

### <u>***Consideraciones***</u>:
- Una sesión de clase debe ser inicializada por un docente para poder recibir registros de estudiantes
- El programa utiliza la fecha y hora del sistema para verificar la existencia de cursos activos. Para que un curso sea considerado activo debe incluir en su arreglo de horarios un objeto que contenga el nombre del día actual y un rango de dos horas, con una hora de inicio y una de finalización que abarquen la hora actual. 
- **Sólo será posible registrar la asistencia de un curso activo**