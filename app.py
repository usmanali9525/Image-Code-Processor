from flask import Flask, request, jsonify, render_template
import cv2
from pylibdmtx.pylibdmtx import decode
from pyzbar import pyzbar
import base64
import numpy as np

app = Flask(__name__)

def process_image(base64_string, processing_type):
    image_data = base64.b64decode(base64_string.split(',')[1])
    image_np = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_GRAYSCALE)

    response_data = []

    if processing_type == '1':
        decoded_objects = decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                barcode_json = {"Decoded Data Matrix": obj.data.decode("utf-8")}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No Data Matrix code found in the image.'})

    elif processing_type == '2':
        barcodes = pyzbar.decode(image)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcode_json = {"Barcode": barcode_data}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No BarCode Detected'})

    elif processing_type == '3':
        barcodes = pyzbar.decode(image)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcode_json = {"QRCode": barcode_data}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No QRCode Detected'})

    elif processing_type == '4':
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        decoded_objects2 = decode(binary_image)

        if decoded_objects2:
            for obj in decoded_objects2:
                barcode_json = {"Decoded Dot Peen Matrix": obj.data.decode("utf-8")}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No Data Matrix code found in the image.'})

    return response_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image_api():
    try:
        content = request.get_json()
        base64_string = content['base64_string']
        processing_type = content['processing_type']

        response_data = process_image(base64_string, processing_type)

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
