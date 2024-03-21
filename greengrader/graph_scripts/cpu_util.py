import matplotlib.pyplot as plt

# Data setup
tasks_labels = ['1', '10', '30', '50']
tasks_index = np.arange(len(tasks_labels))
bar_width = 0.35

# CPU utilization data
fargate_cpu_utilization = [230, 199.5, 210, 208]
ec2_cpu_utilization = [221, 249.5, 246, 255.5]

# Plotting CPU Utilization
plt.figure(figsize=(10, 6))
bars1 = plt.bar(tasks_index - bar_width/2, fargate_cpu_utilization, bar_width, label='Fargate CPU', color='blue')
bars2 = plt.bar(tasks_index + bar_width/2, ec2_cpu_utilization, bar_width, label='EC2 CPU', color='red')

plt.xlabel('Number of Tasks')
plt.ylabel('CPU Utilization (units)')
plt.title('CPU Utilization for Fargate and EC2')
plt.xticks(tasks_index, tasks_labels)
plt.legend()
plt.tight_layout()
plt.show()
