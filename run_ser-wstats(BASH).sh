#!/usr/bin/env bash

# Set the output file
OUTPUT_FILE="performance-server.txt"

# Set the pcap file
PCAP_FILE="mosquitto.pcap"

# Set the port to monitor
PORT=1184

# Set the interface to use for the packet capture
INTERFACE="any"

# Set the interval to check for idle time in seconds
IDLE_INTERVAL=60 

# Set the start time
START_TIME=$(date +%s)

# Set the command to get the mosquito process ID
CMD="pgrep mosquitto"

# Set the command to get the average CPU usage for the mosquito process
CPU_CMD="ps -o %cpu= -p $($CMD)"

# Set the command to get the average memory usage for the mosquito process
MEM_CMD="ps -o %mem= -p $($CMD)"

# Set the command to get the average uptime for the mosquito process
UPTIME_CMD="ps -o etimes= -p $($CMD)"

# Start the packet capture no interface
#tcpdump -i any -w $PCAP_FILE port $PORT &

# Start the packet capture
tcpdump -i $INTERFACE -w $PCAP_FILE port $PORT &

# Get the PID of the tcpdump process
TCPDUMP_PID=$!

# Run the main loop until the script is interrupted
while :
do
    # Check if the mosquito process is running
    if [ -z "$($CMD)" ]
    then
        # If the process is not running, print an error message and exit the loop
        echo "Error: Mosquitto process not found"
        break
    fi

    # Get the current time
    CURR_TIME=$(date +%s)

    # Calculate the elapsed time
    ELAPSED_TIME=$((CURR_TIME-START_TIME))

    # Check if the mosquito process has been idle for more than the idle interval
    if [ $ELAPSED_TIME -gt $IDLE_INTERVAL ]
    then
        # If the process has been idle for too long, exit the loop
        break
    fi

    # Get the average CPU usage for the mosquito process
    CPU=$($CPU_CMD)

    # Get the average memory usage for the mosquito process
    MEM=$($MEM_CMD)

    # Get the average uptime for the mosquito process
    UPTIME=$($UPTIME_CMD)

    # Append the performance data to the output file
    echo "Elapsed Time: $ELAPSED_TIME seconds" >> $OUTPUT_FILE
    echo "CPU: $CPU" >> $OUTPUT_FILE
    echo "Memory: $MEM" >> $OUTPUT_FILE
    echo "Uptime: $UPTIME seconds" >> $OUTPUT_FILE
    echo "" >> $OUTPUT_FILE

    # Sleep for 1 second before checking again
    sleep 1
done

# Stop the packet capture
kill $TCPDUMP_PID
