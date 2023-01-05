run-server.py  to get the average stats or memory and cpu. This script runs run-server.py.

about: 

This script is using the paho.mqtt.client library to connect to an MQTT broker running on the localhost, and listen for messages on three topics: "sensor1", "sensor2", and "sensor3". When the client connects to the broker, it calls the on_connect function, which subscribes to these three topics. When a message is received on one of these topics, the on_message function is called. This function prints the topic and payload of the message and checks if the payload is the string "apple". If it is, the script prints a message saying "The word apple has been received", stops the MQTT client loop, and disconnects the client. The client will keep running and listening for messages indefinitely until the word "apple" is received, at which point the client will stop and disconnect.

The idea behind receivingthe word apple is to kill the process remotely, and to me able to get exact performance metrics when it stops. 



Pre configuration : 

sudo apt install -y mosquitto mosquitto mosquitto-dev mosquitto_sub
sudo apt install mosquitto-clients
sudo install python3
apt install python3-pip
pip install paho.mqtt
pip install psutil
pip install pyshark
pip install tshark
sudo apt-get install tshark
sudo python3
reboot



sudo dpkg-reconfigure wireshark-common

`sudo chmod +x /usr/bin/dumpcap`