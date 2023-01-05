import time
import subprocess
import os
import psutil
import pyshark

# Define local interface
interface = 'any'

# Generate output file names with timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
output_pcap_file = "output_server.pcap" if not os.path.exists("output.pcap") else "output_{}.pcap".format(timestamp)
output_stats_file = "performance_server_stats.txt" if not os.path.exists("performance_stats.txt") else "performance_stats_{}.txt".format(timestamp)

# Start pcap capture on local interface
capture = pyshark.LiveCapture(interface=interface)
capture.sniff(timeout=5)

# Run external script "load-testv3.py"
process = subprocess.Popen(["python", "run_serv-sub.py"])

# Monitor performance of "load-testv3.py"
cpu_usage = []
memory_usage = []
start_time = time.time()
while process.poll() is None:
    # Record CPU usage
    cpu_usage.append(psutil.cpu_percent())
    # Record memory usage
    memory_usage.append(psutil.Process(process.pid).memory_info().rss)
    time.sleep(0.1)

# Calculate average performance metrics
elapsed_time = time.time() - start_time
average_cpu_usage = sum(cpu_usage) / len(cpu_usage)
average_memory_usage = sum(memory_usage) / len(memory_usage)

# Write performance metrics to output file
with open(output_stats_file, 'w') as f:
    f.write("Average CPU usage: {}%\n".format(average_cpu_usage))
    f.write("Average memory usage: {} bytes\n".format(average_memory_usage))
    f.write("Average running time: {} seconds\n".format(elapsed_time))

# Save pcap capture to file  not working at the moment 
#capture.save_to_file(output_pcap_file)
