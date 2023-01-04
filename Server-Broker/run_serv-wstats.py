import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("sensor1")
    client.subscribe("sensor2")
    client.subscribe("sensor3")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"{topic}: {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

start_time = time.time()
client.loop_start()

while True:
    time.sleep(1)
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

client.loop_stop()