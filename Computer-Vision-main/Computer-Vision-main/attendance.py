import cv2
from deepface import DeepFace
import pandas as pd
import datetime
import os
import time

# --- Configuración ---
DB_PATH = "db"
LOG_FILE = "attendance.csv"
FRAME_SKIP = 30  # Analizar cada 30 cuadros para no alentar el video

# Crear archivo de log si no existe
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("Name,Time\n")

cap = cv2.VideoCapture(0)
frame_count = 0

print("Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Analizar el rostro periódicamente
    if frame_count % FRAME_SKIP == 0:
        try:
            # DeepFace.find busca rostros en el frame y los compara con la carpeta db
            dfs = DeepFace.find(img_path=frame, db_path=DB_PATH, silent=True, enforce_detection=False)
            
            if len(dfs) > 0:
                # El primer dataframe contiene las coincidencias
                df = dfs[0]
                if not df.empty:
                    # Obtener la ruta de la imagen que hizo match (ej: db/Juan.jpg)
                    identity_path = df.iloc[0]["identity"]
                    # Extraer el nombre del archivo (ej: Juan)
                    name = os.path.basename(identity_path).split(".")[0]
                    
                    print(f"Hola, {name}!")

                    # Registrar asistencia (simple: solo append)
                    # En un sistema real, chequearíamos si ya marcó hoy
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(LOG_FILE, "a") as f:
                        f.write(f"{name},{now}\n")
                    
                    # Dibujar nombre en el frame (solo durará un frame si no lo persistimos, 
                    # pero para 'simpleza' imprimimos en consola principalmente)
                    cv2.putText(frame, f"Hola {name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
        except Exception as e:
            print("Error en reconocimiento:", e)

    cv2.imshow("Sistema de Asistencia", frame)
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
