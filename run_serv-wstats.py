#!/bin/bash

# Set the command to monitor
COMMAND="mosquitto"

# Set the port to monitor
PORT=1184

# Set the interface to use for the packet capture
#INTERFACE="any"

# Set the duration to run the script before exiting
DURATION="30"

# Set the output file for the performance data
OUTPUT_FILE="performance-server.txt"

# Set the pcap file to capture traffic on the specified port
PCAP_FILE="traffic.pcap"

# Start capturing traffic on the specified port
tcpdump -i any -w $PCAP_FILE "port $PORT" &
PCAP_PID=$!

# Start monitoring the command
while true; do
  # Get the PID of the command
  PID=$(pidof $COMMAND)

  # Check if the command is running
  if [ ! -z "$PID" ]; then
    # Get the current time
    CURRENT_TIME=$(date +%s)

    # Get the average CPU usage of the command
    CPU=$(ps -p $PID -o %cpu | tail -n 1)

    # Get the average memory usage of the command
    MEMORY=$(ps -p $PID -o %mem | tail -n 1)

    # Get the elapsed time of the command
    ELAPSED_TIME=$(ps -p $PID -o etimes | tail -n 1)

    # Output the performance data to the output file
    echo "$CURRENT_TIME, $CPU, $MEMORY, $ELAPSED_TIME" >> $OUTPUT_FILE

    # Reset the idle timer
    IDLE_TIMER=0
  else
    # Increment the idle timer
    IDLE_TIMER=$((IDLE_TIMER+1))
  fi

  # Check if the idle timer has reached the duration
  if [ $IDLE_TIMER -ge $DURATION ]; then
    # Stop capturing traffic
    kill $PCAP_PID

    # Exit the script
    exit 0
  fi

  # Sleep for 1 second before checking again
  sleep 1
done