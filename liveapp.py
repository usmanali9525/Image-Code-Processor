from flask import Flask, render_template, Response, jsonify, request
import cv2
from pylibdmtx.pylibdmtx import decode
from pyzbar import pyzbar
import numpy as np
import json
import base64
import threading

app = Flask(__name__)

# Global variables to store camera instance and processed data
camera = cv2.VideoCapture(0)  # 0 for default camera (you can change it if you have multiple cameras)
processed_data = []

def process_image(frame, processing_type):
    response_data = []

    if processing_type == '1':
        decoded_objects = decode(frame)

        if decoded_objects:
            for obj in decoded_objects:
                barcode_json = {"Decoded Data Matrix": obj.data.decode("utf-8")}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No Data Matrix code found in the image.'})

    elif processing_type == '2':
        barcodes = pyzbar.decode(frame)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcode_json = {"Barcode": barcode_data}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No BarCode Detected'})

    elif processing_type == '3':
        barcodes = pyzbar.decode(frame)
        if barcodes:
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                barcode_json = {"QRCode": barcode_data}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No QRCode Detected'})

    elif processing_type == '4':
        blurred = cv2.GaussianBlur(frame, (5, 5), 0)
        _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        decoded_objects2 = decode(binary_image)

        if decoded_objects2:
            for obj in decoded_objects2:
                barcode_json = {"Decoded Dot Peen Matrix": obj.data.decode("utf-8")}
                response_data.append(barcode_json)
        else:
            response_data.append({'message': 'No Data Matrix code found in the image.'})

    return response_data

def camera_stream():
    global processed_data
    while True:
        success, frame = camera.read()
        if not success:
            print("Failed to read from camera.")
            break

        processed_data = process_image(frame, '4')  # Adjust the processing type as needed

        _, encoded_frame = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_frame) + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('live_camera.html')

@app.route('/process_image', methods=['POST'])
def process_image_api():
    try:
        processing_type = request.form['processing_type']

        return jsonify(processed_data)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/video_feed')
def video_feed():
    return Response(camera_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
