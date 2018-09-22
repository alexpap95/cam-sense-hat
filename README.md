# cam-sense-hat
Webcam Control Through Raspberry Pi Using a Skywriter Hat and the MQTT Protocol

Programming Languages: Python, Javascript, HTML, CSS
Raspbian Stretch Lite on RPI (Kernel 4.14)
Technologies used on Raspberry Pi: Skywriter Hat, Mosquitto MQTT Broker
Libraries used on Raspberry Pi: Skywriter, signal, paho.mqtt
Libraries used on Pc: paho.mqtt, cv2, threading, requests, json, time, flask, jsonpickle,
numpy, os, werkzeug.utils, config

Installation Guide

Raspberry Pi
1. Download and Install Raspbian Stretch Lite
2. Install Mosquito MQTT Broker
3. Install proper libraries for Skywriter Hat and Paho MQTT

PC
1. Download and Install Python.
2. Install pip on Python.
3. Using pip install all libraries needed from the list above.
4. Download and install putty in order to connect to your RPI in case you have not
connected a keyboard, mouse or monitor to it. (optional)

Initialisation Guide
0. Move css, fonts, js, sass folders into one "static" folder (/static/css , /static/fonts, etc)
1. Copy MQTT_Pub(rpi).py on the RPI
2. Run cd copied_directory , to navigate to the file
3. Run python MQTT_Pub(rpi).py to execute the publisher script from the RPI.
4. Execute MQTT_Sub.py and Server.py on your PC.
5. Start using Double Tap and Tap gestures on the south and north part
respectively, to open or close the camera (Double_tap South) and take pictures
(Tap North)
6. Navigate to 127.0.0.1:5000 using your browser (preferably Mozilla Firefox) to
see your pictures
