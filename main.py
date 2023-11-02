import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode
from PIL import Image
import time
import math

start_time = time.time()

img = cv2.imread('download (1).png')

pil_image = Image.fromarray(np.uint8(img))

# Decode the Data Matrix code
decoded_objects = decode(pil_image)

if decoded_objects:
    for obj in decoded_objects:
        print(f'Decoded Data Matrix: {obj.data.decode("utf-8")}')
else:
    print('No Data Matrix code found in the image.')

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f'Time taken to decode the image: {math.ceil(elapsed_time_ms)} milliseconds')
