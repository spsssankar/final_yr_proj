# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("Platoon/test", "Hello", hostname="test.mosquitto.org")
publish.single("Platoon/topic", "World!", hostname="test.mosquitto.org")
print("Done")
