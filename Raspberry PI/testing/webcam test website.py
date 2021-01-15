# Importing Modules
from flask import Flask, render_template, Response, send_file
import cv2
from threading import Thread

# Initializing Program Stuff
app = Flask(__name__)
vc = cv2.VideoCapture(0)


# Creating Flask
@app.route('/')
def index():
    return render_template("index.html")
def gen():
    while True:
        rval, frame = vc.read()
        byteArray = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + byteArray + b'\r\n')

        
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/text_data')
def text_data():
    return open("test.txt", 'r').read()

@app.route('/map_image')
def map_image():
    while True:
        return send_file("image.jpg")
"""def gen_map_image():
    while True:
        yield send_file("image.jpg")"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
