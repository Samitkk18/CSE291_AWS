import matplotlib.pyplot as plt

# Data setup
tasks = [1, 10, 30, 50]  # Number of tasks
fargate_cpu_utilization = [230, 199.5, 210, 208]
fargate_mem_utilization = [58, 59, 64, 79]
ec2_cpu_utilization = [221, 249.5, 246, 255.5]
ec2_mem_utilization = [69, 75, 72, 64]

# Plotting
plt.figure(figsize=(12, 8))

# CPU Utilization lines
plt.plot(tasks, fargate_cpu_utilization, '-o', label='Fargate CPU', color='blue')
plt.plot(tasks, ec2_cpu_utilization, '-o', label='EC2 CPU', color='red')

# Memory Utilization lines
plt.plot(tasks, fargate_mem_utilization, '--d', label='Fargate Memory', color='cyan')
plt.plot(tasks, ec2_mem_utilization, '--d', label='EC2 Memory', color='magenta')

plt.title('CPU and Memory Utilization for Fargate and EC2')
plt.xlabel('Number of Tasks')
plt.ylabel('Utilization')
plt.xticks(tasks)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
