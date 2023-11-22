import cv2
from pylibdmtx.pylibdmtx import decode
from pyzbar import pyzbar
import base64
import numpy as np
import json

# base64_string = "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIAAQMAAADOtka5AAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAACAklEQVR42u3cPY6DMBCG4UFbUOYIOQpHS46Wo3AEyhQIr7HHszZa8lPFOO9XRJHsfbZiNAw4IoQQQgghhBBCCDlGflyemwz6TTr/MYctfbHlCgAAUC1wt+9nD8T4jYst926yLQMAAEDbQKwYowIXvycUlMUvzqGgTHKyegMAAHAcYCUUEO0PAAAAvhrwf975cpL6AwAAgGMAZbtv/YHLgHfuFwAAAA4LbMeBV0+IFAXlvXkiAADAZ4BtBt0TNs9FuXgtAAAAhwXWgnIPtwP5ODAUFMnGgY/7AwAAgDqAeMFHYlDCf3RaEXr1UwMhAAAA7QJus+OS+oNFF9f7hclXm/FJRQIAAPg0kPr5s9WDjb4WixXYmx8AAAA0AqScipmfAc/vFwAAAOoBYj8/6XoCMi1WhDEs3/753wAAAM0AojcE8eH9UBaUmCmrN1cAAIBqgV4veBcu+TX68D4Bd2v3b7v9AQAAQCOAy4aBEQhZijd9RiUEAACgWqBMfDfPTtY5e5YHAADQPLB9V7d4mUeyozij+QAAALUCuydptvUAAADgC4D8pO3w9ypPV9SacaehAAAAqBvIHtblB2UH516sBwAAAA0A1h/ExTkb/scAAADUDKScs4PzItnv2p5sug8AANA0UI4DrT9IP6SRBgCPzvIAAADUABBCCCGEEEIIIaTZ/ALesjYwnLBumgAAAABJRU5ErkJggg=="

# # Extract the base64 encoded image data
# image_data = base64.b64decode(base64_string)
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
        decoded_objects = decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                barcodeJson = {"Decoded Data Matrix": obj.data.decode("utf-8")}
                json_output = json.dumps(barcodeJson, indent=2)
                print(json_output)
        else:
            print('No Data Matrix code found in the image.')

    elif Number == 2:
        #blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        #_, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # barcodes = pyzbar.decode(threshold_image)
        barcodes = pyzbar.decode(image) 
        if barcodes:
        # Process each barcode found
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcodeJson = {"Barcode": barcode_data}
                json_output = json.dumps(barcodeJson, indent=2)
                print(json_output)
        else: 
            print('No  BarCode Detected')
    elif Number == 3:
        barcodes = pyzbar.decode(image) 
        
        # Process each barcode found
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcodeJson = {"Decoded Dot Peen Matrix": barcode_data}
            json_output = json.dumps(barcodeJson, indent=2)
            print(json_output)

    elif Number == 4:
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        #cv2.imshow('Image', binary_image)
        decoded_objects2 = decode(binary_image)

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