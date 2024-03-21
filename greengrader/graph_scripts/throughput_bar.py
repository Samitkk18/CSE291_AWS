import numpy as np
import matplotlib.pyplot as plt

# Data from the user
tasks = [1, 10, 30, 50]
fargate_runtime_sec = [220, 242, 232, 230]
ec2_runtime_sec = [167.5, 336, 630, 974]

# Convert runtime to minutes
fargate_runtime_min = [x / 60 for x in fargate_runtime_sec]
ec2_runtime_min = [x / 60 for x in ec2_runtime_sec]

# Calculate throughput as tasks per minute
fargate_throughput_min = [tasks[i] / fargate_runtime_min[i] for i in range(len(tasks))]
ec2_throughput_min = [tasks[i] / ec2_runtime_min[i] for i in range(len(tasks))]

# Plotting
bar_width = 0.35
index = np.arange(len(tasks))

plt.figure(figsize=(7, 4))  # Adjust the figure size accordingly
plt.bar(index, fargate_throughput_min, bar_width, label='Fargate', color='blue')
plt.bar(index + bar_width, ec2_throughput_min, bar_width, label='EC2', color='red')

plt.xlabel('Number of Tasks', fontsize=10)  
plt.ylabel('Throughput (Tasks/min)', fontsize=10)
plt.title('Throughput Comparison Between Fargate and EC2', fontsize=12) 
plt.xticks(index + bar_width / 2, tasks)
plt.legend(fontsize=10) 
plt.tight_layout()
plt.show()
