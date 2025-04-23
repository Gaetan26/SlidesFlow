
import paho.mqtt.client as mqtt
from slides import *
from threading import Thread

BROKER = "127.0.0.1"
PORT = 1883

SLIDES_TOPIC = "topic/slidesflow"
DEVICES_TOPIC = "topic/devices"

def on_message(client, userdata, msg):
    direction = msg.payload.decode()
    direction = direction.lower()

    if direction == "right":
        nextSlide()
        
    elif direction == "left":
        previousSlide()

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)

def vibrate_devices():
    client.publish(DEVICES_TOPIC, "vibrate")

def run():
    client.subscribe(SLIDES_TOPIC)
    client.loop_forever()
