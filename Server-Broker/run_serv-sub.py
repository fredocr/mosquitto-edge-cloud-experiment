import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("sensor1")
    client.subscribe("sensor2")
    client.subscribe("sensor3")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"{topic}: {payload}")

    if payload == "apple":
        print("The word apple has been received")
        # Stop the MQTT client loop
        client.loop_stop()
        # Disconnect the client
        client.disconnect()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
