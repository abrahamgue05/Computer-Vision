# Proyecto 6: Computer Vision

## Descripción del Proyecto
Este proyecto implementa un **Sistema de Asistencia Automatizada** utilizando visión por computadora. El software captura video en tiempo real desde la cámara web, detecta rostros y los compara con una base de datos de imágenes locales. Cuando un rostro es reconocido, el sistema registra automáticamente el nombre de la persona y la hora de llegada en un archivo de registro (`attendance.csv`).

El objetivo es demostrar cómo se puede utilizar la librería `DeepFace` para crear soluciones biométricas sencillas y efectivas para la gestión de asistencia.

## Instructivo de Uso

### 1. Crear entorno virtual (Opcional pero recomendado)
Es buena práctica aislar las dependencias del proyecto.

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
.\venv\Scripts\activate
```

### 2. Instalar requerimientos
Asegúrate de estar en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
pip install opencv-python pandas
```
*(Nota: `deepface` instalará sus propias dependencias como tensorflow y keras).*

### 3. Preparar la Base de Datos
1.  Crea una carpeta llamada `db` en la raíz del proyecto (si no existe).
2.  Agrega fotos de las personas que deseas reconocer dentro de la carpeta `db`.
3.  **Importante:** El nombre del archivo será usado como el nombre de la persona (ejemplo: `Eduardo.jpg` registrará la asistencia de "Eduardo").

### 4. Ejecutar el Software
Corre el script principal:

```bash
python attendance.py
```

*   Se abrirá una ventana con la cámara.
*   Cuando el sistema reconozca un rostro de la carpeta `db`, mostrará un saludo en consola y guardará el registro en `attendance.csv`.
*   Presiona la tecla **'q'** para salir.