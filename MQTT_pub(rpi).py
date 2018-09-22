#!/usr/bin/env python
import skywriter
import signal
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


broker="test.mosquitto.org"
topic="topic/ece8462_IoT"

# set up the mqtt client
mqttc = mqtt.Client(topic)
# the server to publish to, and corresponding port
mqttc.connect(broker, 1883)

@skywriter.tap()
def tap(position):
        print('Tap!', position)
        publish.single(topic, "tap"+position, hostname=broker)
        mqttc.loop(0.1)

@skywriter.double_tap()
def doubletap(position):
        print('Double tap!', position)
        publish.single(topic, "doubletap"+position, hostname=broker)
        mqttc.loop(0.1)

signal.pause()
