import paho.mqtt.client as mqtt
import datetime
import sys
import struct

def on_message(client1, userdata, message):
    if message.payload == b'END':
        client.loop_stop()
        curr_timestamp = int(round(datetime.datetime.now().timestamp()))
        with open(f'latencies-{curr_timestamp}', 'w') as f:
            f.write('\n'.join(latencies))
        sys.exit(0)

    (packet_timestamp,) = struct.unpack('d', message.payload)
    latency = (datetime.datetime.now().timestamp() - packet_timestamp) * 1000
    latencies.append(str(latency))
    print(latency)

def start(host, port):
    client.connect(f'{host}', port)
    client.subscribe([("test", 1)])
    client.loop_forever()

latencies = []
client = mqtt.Client()
client.on_message = on_message

if __name__ == "__main__":
    a = sys.argv[1]
    b = int(sys.argv[2])
    start(a, b)