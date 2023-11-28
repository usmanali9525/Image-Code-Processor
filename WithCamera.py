import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode
from PIL import Image
import threading
import time

def process_frame(frame):
    decoded_objects = decode(frame)

    if decoded_objects:
        for obj in decoded_objects:
            print(f'Decoded Data Matrix: {obj.data.decode("utf-8")}')

def camera_capture():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (360, 360))
        cv2.imshow('Data Matrix Detection', resized_frame)
        threading.Thread(target=process_frame, args=(resized_frame,), daemon=True).start()

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_capture()
