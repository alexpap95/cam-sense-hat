import paho.mqtt.client as mqtt
import cv2
import threading
import requests
import json
import time

MQTT_SERVER = "test.mosquitto.org"
MQTT_PATH = "topic/ece8462_IoT"
flag=0
url = 'http://localhost:5000/'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

class myThread(threading.Thread):
    def __init__(self,msg):
        super(myThread, self).__init__()
        self.msg=msg
        self._stop_event = threading.Event()
        self._snap_event = threading.Event()
    def stop(self):
        print "Camera Close"
        self._stop_event.set()
    def stopped(self):
        return self._stop_event.is_set()
    def snap(self):
        self._snap_event.set()
    def snapped(self):
        return self._snap_event.is_set()
    def clear(self):
        self._snap_event.clear()
    def run(self):
        print "Camera Open"
        opencamera(self.msg)
        
def opencamera(msg):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Pic_Window")
    while True:
        if (t.stopped()==True):
            break
        ret, frame = cam.read()
        cv2.imshow("Pic_Window", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if (t.snapped()==True):
            t.clear()
            img_name = "local.jpg"
            cv2.imwrite(img_name, frame)
            print("New Image Saved!")
            time.sleep(0.5)
            img = open(img_name, 'rb').read()
            requests.post(url, data=img, headers=headers)
    cam.release()
    cv2.destroyAllWindows()
    
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global flag
    global t
    if (str(msg.payload)=="doubletapsouth"):
        if flag==0:
            flag=1
            t=myThread(msg)
            t.daemon = True
            t.start()
        else:
            flag=0
            t.stop()
            t.join()
    elif (str(msg.payload)=="tapnorth" and flag==1):
        t.snap()
            
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
