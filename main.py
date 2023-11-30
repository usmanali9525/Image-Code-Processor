import cv2
from pylibdmtx import pylibdmtx
from pyzbar import pyzbar
import base64
import numpy as np
import json

# base64_string = "Base64 Data"
# image_data = base64.b64decode(base64_string.split(',')[1])
# image_np = np.frombuffer(image_data, np.uint8)
# image = cv2.imdecode(image_np, cv2.IMREAD_GRAYSCALE)

image = cv2.imread('TestingImages\Test5.png', cv2.IMREAD_GRAYSCALE)

while True:
    print('Press 1 for DataMatrix')
    print('Press 2 for BarCode')
    print('Press 3 for QRCode')
    print('Press 4 for DotPeenMatrix')
    print('Press 5 for Exit')
    Number = int(input('Enter Number: '))

    if Number == 1:
        decoded_objects = pylibdmtx.decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                barcodeJson = {"Decoded Data Matrix": obj.data.decode("utf-8")}
                json_output = json.dumps(barcodeJson, indent=2)
                print(json_output)
        else:
            print('No Data Matrix code found in the image.')

    elif Number == 2:
        barcodes = pyzbar.decode(image) 
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcodeJson = {"Barcode": barcode_data}
                json_output = json.dumps(barcodeJson, indent=2)
                print(json_output)
        else: 
            print('No BarCode Detected')
    elif Number == 3:
        barcodes = pyzbar.decode(image) 
    
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcodeJson = {"Decoded Dot Peen Matrix": barcode_data}
            json_output = json.dumps(barcodeJson, indent=2)
            print(json_output)

    elif Number == 4:
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        decoded_objects2 = pylibdmtx.decode(binary_image)
        if decoded_objects2:
            for obj in decoded_objects2:
                barcodeJson = {"Decoded Dot Peen Matrix": obj.data.decode("utf-8")}
                json_output = json.dumps(barcodeJson, indent=2)
                print(json_output)
        else:
            print('No Data Matrix code found in the image.')

    elif Number == 5:
        break

    else:
        print('Insert New Image')