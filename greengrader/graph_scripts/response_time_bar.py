import numpy as np
import matplotlib.pyplot as plt

# Original data
tasks = [1, 10, 30, 50]
fargate_runtime_sec = [220, 242, 232, 230]
ec2_runtime_sec = [167.5, 336, 630, 974]

# Convert runtime to minutes
fargate_runtime_min = [x / 60 for x in fargate_runtime_sec]
ec2_runtime_min = [x / 60 for x in ec2_runtime_sec]

# Calculate latency as minutes per task
fargate_latency = [runtime / task for runtime, task in zip(fargate_runtime_min, tasks)]
ec2_latency = [runtime / task for runtime, task in zip(ec2_runtime_min, tasks)]

# Plotting
plt.figure(figsize=(7, 4))  # Adjust the figure size accordingly
bar_width = 0.35
index = np.arange(len(tasks))

plt.bar(index, fargate_latency, bar_width, label='Fargate', color='blue')
plt.bar(index + bar_width, ec2_latency, bar_width, label='EC2', color='red')

plt.xlabel('Number of Tasks', fontsize=10)  # Increase x-axis label font size
plt.ylabel('Mean Response Time (Min/Task)', fontsize=10)  # Increase y-axis label font size
plt.title('Mean Response Time (Minutes per Task) Between Fargate and EC2', fontsize=12)  # Increase title font size
plt.xticks(index + bar_width / 2, ["1", "10", "30", "50"])
plt.legend(fontsize=10)  # Increase legend font size
plt.tight_layout()
plt.show()
