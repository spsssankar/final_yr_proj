# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="test.mosquitto.org")
publish.single("CoreElectronics/topic", "World!", hostname="test.mosquitto.org")
print("Done")
