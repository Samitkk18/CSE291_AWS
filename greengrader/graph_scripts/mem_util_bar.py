import matplotlib.pyplot as plt
import numpy as np

# Data setup
tasks_labels = ['1', '10', '30', '50']
tasks_index = np.arange(len(tasks_labels))
bar_width = 0.35

# Memory utilization data
fargate_mem_utilization = [58, 59, 64, 79]
ec2_mem_utilization = [69, 75, 72, 64]

# Plotting Memory Utilization
plt.figure(figsize=(10, 6))
bars1 = plt.bar(tasks_index - bar_width/2, fargate_mem_utilization, bar_width, label='Fargate Memory', color='blue')
bars2 = plt.bar(tasks_index + bar_width/2, ec2_mem_utilization, bar_width, label='EC2 Memory', color='red')

plt.xlabel('Number of Tasks')
plt.ylabel('Memory Utilization (MB)')
plt.title('Memory Utilization for Fargate and EC2')
plt.xticks(tasks_index, tasks_labels)
plt.legend()
plt.tight_layout()
plt.show()
