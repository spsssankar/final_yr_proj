# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.publish as publish

import paho.mqtt.client as mqtt
from line_follow_pwm_car2 import still,forward,right,left
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Platoon/test")
    #client.subscribe("Platoon/topic")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if msg.payload == "stop":
        print("stop")
        still()
        publish.single("Platoon/car2", "still", hostname="test.mosquitto.org")
        # Do something

    if msg.payload == "right":
        print("right")
        right(255)
        publish.single("Platoon/car2", "still", hostname="test.mosquitto.org")
        # Do something else
    if msg.payload == "left":
        print("left")
        left(255)
        publish.single("Platoon/car2", "still", hostname="test.mosquitto.org")
        # Do something else
        
    if msg.payload == "forward":
        print("forward")
        forward(255)
        publish.single("Platoon/car2", "still", hostname="test.mosquitto.org")
        # Do something else
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
