import cv2
import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqtt_sender
import json

# callback
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #dlr1414_print.writeString("MQTT live")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("frigate/events")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload.decode("utf-8")))

def display_image(image, boundingbox):
    print("todo")

with open("credentials") as file:
    mqtt_settings=json.loads(file.read())

client = mqtt.Client()
client.username_pw_set(mqtt_settings["username"],mqtt_settings["password"])
client.on_connect = on_connect


client.connect(mqtt_settings["ip"],int(mqtt_settings["port"]), 60)

client.loop_forever()

#client.on_message = on_message

