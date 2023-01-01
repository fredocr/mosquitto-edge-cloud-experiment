# mosquitto-edge-cloud-experiment

This project aims to study the feasibility and cost-effectiveness of using edge computing for stream data processing in the context of the Internet of Things (IoT) in manufacturing in Europe. We will consider two scenarios: one in which edge computing is used to reduce latency and improve proximity, and another in which a public cloud provider is used. We believe that there is a high concentration of data centers in Europe and that there are protocols that can be used to transfer large amounts of data to public clouds or edge computing nodes. By comparing stream processing platforms in these two scenarios, we hope to gain insight into the best approach for stream processing and to establish a basic setup for stream processing.



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



About load-testv3.py

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








About run_serv-wstats.py

The intention of this script is to generate a monitoring app on the "broker" side. Get an average of performance for memory, CPU, time and network performance (pcap generation on the specific port for the aplication)
    
Desired functions:
-Set several variables including the command to monitor, the port to monitor, the interface to use for packet capture, the duration to run the script the output file for performance data, and the pcap file to capture traffic.
-Start a packet capture using tcpdump on the specified interface, capturing packets on the specified port and saving them to the pcap file.
-Enter an infinite loop to monitor the specified command.
-Within the loop, get the PID of the command, and check if it is running. If it is, get the current time, average CPU usage, average memory usage, and elapsed time of the command, and output this data to the output file. Reset the idle timer to 0. If the command is not running, increment the idle timer by 1.
-Check if the idle timer has reached the specified duration. If it has, stop the packet capture and exit the script.
-Sleep for 1 second before checking the command again.
