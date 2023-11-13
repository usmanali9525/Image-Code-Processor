import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode
from PIL import Image

# Initialize the camera capture
cap = cv2.VideoCapture(0) 

while True:
    ret, frame = cap.read()

    #pil_image = Image.fromarray(frame)
    decoded_objects = decode(frame)

    if decoded_objects:
        for obj in decoded_objects:
            print(f'Decoded Data Matrix: {obj.data.decode("utf-8")}')
        cv2.imshow('Data Matrix Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
