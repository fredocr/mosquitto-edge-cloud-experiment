# Import necessary modules
import paho.mqtt.client as mqtt
import random
import time
import datetime
import struct
import sys

#Initial counter 
counter = 0

# Set the broker address and port
broker_address = "37.152.61.101"
broker_port = 1883

# Set the topics and number of devices
topics = ['test'] #["sensor1", "sensor2", "sensor3"]
num_devices = 10

# Set the number of messages to publish per device
num_messages = 200

# Function to be called when a message is published
def on_publish(client, userdata, mid):
    global counter
    counter += 1

# Create a new MQTT client
client = mqtt.Client()

# Set the on_publish function to be called when a message is published
client.on_publish = on_publish

# Connect to the broker
client.connect(broker_address, broker_port)

# Set the time variable
run_time = 2 #10800 = 3 hours in seconds

# Start a loop to publish messages from each device
start_time = time.time()
while time.time() - start_time < run_time:
    for i in range(num_devices):
        for j in range(num_messages):
            
            # Choose a random topic
            topic = random.choice(topics)

            # Generate data for each device and topic
            data = datetime.datetime.now().timestamp()
            print(data)

            # Publish the data to the broker
            client.publish(topic, struct.pack('d', data))

        # Sleep for 1 second before publishing again
        time.sleep(1)
client.publish(topic, 'END')

# Function to show a summary of the data transferred
def show_summary():
    data_transferred = counter * 10 # 10 bytes per message
    data_transferred_mb = data_transferred / 1000000 # Convert to megabytes
    print(f"Total data transferred: {data_transferred_mb} MB")
    print(f"Total messages sent: {counter}")
    print(f"Total time elapsed: {run_time} seconds")

# Call the show_summary function
show_summary()
