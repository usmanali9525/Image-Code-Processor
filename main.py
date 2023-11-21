import cv2
from pylibdmtx.pylibdmtx import decode
import time
import math

start_time = time.time()

image = cv2.imread('TestingImages\Test.8.jpg', cv2.IMREAD_GRAYSCALE)

decoded_objects = decode(image)

if decoded_objects:
    for obj in decoded_objects:
        print(f'Decoded Data Matrix: {obj.data.decode("utf-8")}')

elif not decoded_objects:
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('Image', binary_image)
    decoded_objects2 = decode(binary_image)

    if decoded_objects2:
        for obj in decoded_objects2:
            print(f'Decoded Data Matrix: {obj.data.decode("utf-8")}')
    else:
        print('No Data Matrix code found in the image.')

else:
    print('No Data Matrix code found in the image.')

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f'Time taken to decode the image: {math.ceil(elapsed_time_ms)} milliseconds')

cv2.waitKey(0)