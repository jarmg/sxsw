import picamera

from flask import Flask

import camera_control as cam


def take_picture(name):
    with picamera.PiCamera() as camera:
        camera.capture('/usr/src/app/frontend/src/' + name + '.jpg')
    print('picture taken')


##################################
# Flask Server
##################################
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Pooja Patel!'

@app.route('/picture')
def take_pic():
    cam.init()

    cam.camA()
    take_picture('cameraA')

    cam.camD()
    take_picture('cameraD')
    return 'Take a Picture!'

app.run(host='0.0.0.0', port=8080)
