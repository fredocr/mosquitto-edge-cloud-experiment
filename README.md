# mosquitto-edge-cloud-experiment

This project aims to study the feasibility and cost-effectiveness of using edge computing for stream data processing in the context of the Internet of Things (IoT) in manufacturing in Europe. We will consider two scenarios: one in which edge computing is used to reduce latency and improve proximity, and another in which a public cloud provider is used. We believe that there is a high concentration of data centers in Europe and that there are protocols that can be used to transfer large amounts of data to public clouds or edge computing nodes. By comparing stream processing platforms in these two scenarios, we hope to gain insight into the best approach for stream processing and to establish a basic setup for stream processing.

This scripts has 2 parts,  client side ( simulates IoT client ) and server side ( simulates the brokerage for stream processing)

****  CLIENT SIDE ***
About run.py 
 This script runs on the edge source, triggers the mosquitto load testand measures its performance. PCAP untest yet. 

-Imports several libraries including time, subprocess, os, psutil, and pyshark.
-Defines a local interface variable and set it to 'any'.
-Generates output file names for a pcap file and a performance stats file using the current timestamp.
-Starts a packet capture using pyshark on the specified interface, and set it to capture packets for 5 seconds.
-Runs an external script called "load-testv3.py" using the subprocess library.
-While the "load-testv3.py" script is still running, monitors its performance by recording its CPU usage, memory usage, and the time it has been running. -This is done every 0.1 seconds.
-When the "load-testv3.py" script finishes running, calculates the average CPU usage, average memory usage, and total elapsed time.
-Writes the average performance metrics to the performance stats file.
-Saves the packet capture to the pcap file, although this step is currently commented out.



**** About load-testv3.py ****

This script generates the simulation from the "edge" source. The original porpoise is to simulate comunciation between IoT devices and the broker, to analize performance and efficiency between the node and the broker.
It publishes x amount of messages from multiple devices to an MQTT broker as follows: 

+Imports several modules including paho.mqtt.client, random, and time.
+Initializes a counter variable to 0.
+Sets the address and port of the MQTT broker, and the topics and number of devices to simulate.
+Defines a function to generate random data as a string of 10 random digits.
+Defines a function to be called when a message is published, which increments the global counter variable.
+Creates a new MQTT client and set the on_publish function to be called when a message is published.
+Connects the client to the broker.
+Sets the run time of the simulation in seconds.
+Starts a loop to publish messages from each device for the specified run time. Within the loop, choose a random topic, generate data for each device and topic, and publish the data to the broker. Sleep for 1 second before publishing again.
+Defines a function to show a summary of the data transferred, which calculates the total data transferred in megabytes, total messages sent, and total elapsed time.
+Calls the show_summary function to display the summary.
+It also sends the word "apple" at the end to kill the server measurement that runs continusly. 






SERVER BROKER FOLDER - RUNS ON THE BROKER/SERVER 

****  About run_server.py****

The intention of this script is to generate a monitoring app on the "broker" side. Get an average of performance for memory, CPU, time and network performance (pcap generation on the specific port for the aplication)

It runs an external script called "run_serv-sub.py", and then monitors the CPU and memory usage of the external script as it runs. It then calculates some performance metrics (average CPU usage, average memory usage, and total elapsed time) and writes them to an output file. Finally, it attempts to save the captured network traffic to a pcap file, but this functionality is commented out. 

**** About run_server.py
This script creates an MQTT client that connects to a broker running on "localhost" at port 1883, with a keepalive of 60 seconds. When the client connects to the broker, the on_connect() callback function is called and the client subscribes to three topics: "sensor1", "sensor2", and "sensor3".

When the client receives a message from the broker, the on_message() callback function is called and the message's topic and payload are printed to the console. If the message's payload is the string "apple", then a message is printed to the console and the client's MQTT loop is stopped and the client is disconnected. ** This functions was added so the run_server.py could finish the measurement function  and get the exact performance metrics of this process. 



**** About PCAP functionality****

The code was intended to include pcap functionality, but at the end it was triggered manually to provide more felxibility to the captures and its tunning. 

sudo tcpdump -qns 0 -X -A -w  name.pcap


************************************************************************************************************************************

  **** System dependancies for both client and server ****
  
apt install -y mosquitto mosquitto mosquitto-dev mosquitto_sub

apt install mosquitto-clients

install python3

apt install python3-pip

pip install paho.mqtt

pip install psutil

pip install pyshark

pip install tshark

apt-get install tshark

sudo  ln -s $(which python3) /usr/local/bin/python

sudo dpkg-reconfigure wireshark-common

sudo chmod +x /usr/bin/dumpcap

************************************************************************************************************************************


########     Misssing readme instruction on latency pythons scripts ( intended ti run for less to graph latency measurements in 2 scenarios)

