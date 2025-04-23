
import paho.mqtt.client as mqtt

SLIDES_TOPIC = "topic/slidesflow"
DEVICES_TOPIC = "topic/devices"

hapticfeedback = None

def on_connect(client, userdata, flags, rc):
    print("connected to MQTT SERVER with code", rc)

def on_message(client, userdata, msg):
    text = msg.payload.decode()
    hapticfeedback.vibrate()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

def connect(broker):
    client.connect(broker, 1883, 60)
    client.subscribe(DEVICES_TOPIC) 

def wait():
    client.loop_forever()