import cv2
from pylibdmtx.pylibdmtx import decode
import time
import math
from pyzbar import pyzbar


image = cv2.imread('TestingImages\QRCode.png', cv2.IMREAD_GRAYSCALE)

while True:
    print('Press 1 for DataMatrix')
    print('Press 2 for BarCode')
    print('Press 3 for QRCode')
    print('Press 4 for DotPeenMatrix')
    print('Press 5 for Exit')
    Number = int(input('Enter Number: '))

    if Number == 1:
        decoded_objects = decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                print(f'Decoded Data Matrix: {obj.data.decode("utf-8")}')
        else:
            print('No Data Matrix code found in the image.')

    elif Number == 2:
        #blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        #_, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # barcodes = pyzbar.decode(threshold_image)
        barcodes = pyzbar.decode(image) 
        
        # Process each barcode found
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            print(f'Decoded BarCode: {barcode_data}')

    elif Number == 3:
        barcodes = pyzbar.decode(image) 
        
        # Process each barcode found
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            print(f'Decoded QRCode: {barcode_data}')

    elif Number == 4:
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow('Image', binary_image)
        decoded_objects2 = decode(binary_image)

        if decoded_objects2:
            for obj in decoded_objects2:
                print(f'Decoded Dot Peen Matrix: {obj.data.decode("utf-8")}')
        else:
            print('No Data Matrix code found in the image.')

    elif Number == 5:
        break

    else:
        print('Insert New Image')
