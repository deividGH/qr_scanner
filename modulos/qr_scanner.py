import cv2
from pyzbar.pyzbar import decode
import json
import numpy as np
import time


def qr_scanner():
    cam = cv2.VideoCapture(0)
    cam.set(5, 640)
    cam.set(6, 480)
    camera = True
    scanned_data = None 

    while camera:
        success, frame = cam.read()

        for i in decode(frame):
            decoded_text = i.data.decode('utf-8')
            print("Tipo de código:", i.type)
            print("Contenido escaneado:", decoded_text)

            try:
                scanned_data = json.loads(decoded_text)
                print("JSON cargado correctamente:", scanned_data)
                    
                # Imprimir rectángulo verde al rededor del QR para indicar escaneo correcto 
                puntos = i.polygon
                if len(puntos) == 4:
                    pts = [(p.x, p.y) for p in puntos]
                    cv2.polylines(frame, [np.array(pts, np.int32)], isClosed=True, color=(0, 255, 0), thickness=3)
            except json.JSONDecodeError:
                print("Error: El código QR no contiene un JSON válido.")



            time.sleep(0.3)
            camera = False 

        cv2.imshow("QR_Scanner", frame)
        cv2.waitKey(3)

    cam.release()
    cv2.destroyAllWindows()

    return scanned_data