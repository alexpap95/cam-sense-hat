from flask import Flask, request, Response, render_template, send_from_directory, session
import jsonpickle
import numpy as np
import cv2
import os
from werkzeug.utils import secure_filename
from config import *

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(__name__)

def get_last_pics():
    """ Return a list of the last 25 uploaded images"""
    names = os.listdir("img")
    return names

# route http posts to this method
@app.route('/',  methods=['GET', 'POST'])
def test():
    if request.method=='POST':
        r = request
        # convert string of image data to uint8
        nparr = np.fromstring(r.data, np.uint8)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        names =os.listdir("img")
        if not names:
            img_name = 'img/image_0.jpg'
        else:
            names = [filter(str.isdigit, x) for x in names]
            names = [int(x) for x in names]
            num = max(names)
            if num == 0:
                num=1
            else:
                num=num+1
            img_name = 'img/image_'+str(num)+'.jpg'
        cv2.imwrite(img_name, img)
        return "Image Uploaded"
    else:
        return render_template('upload.html', pics=get_last_pics())
    
@app.route('/img/<filename>')
def return_pic(filename):
    print filename
    """ Show just the image specified"""
    return send_from_directory(app.config['UPLOAD_DIR'], secure_filename(filename))

# start flask app
app.run(host="127.0.0.1", port=5000)
