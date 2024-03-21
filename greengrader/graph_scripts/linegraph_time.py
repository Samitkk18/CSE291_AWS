import matplotlib.pyplot as plt

# Extract data for plotting
tasks = [1, 10, 30, 50]
fargate_runtime = [220, 242, 232, 230]
ec2_runtime = [167.5, 336, 630, 974]

# Plot
plt.figure(figsize=(7, 4))  # Adjust the figure size accordingly
plt.plot(tasks, fargate_runtime, label='Fargate', marker='o', linestyle='-', color='blue', markersize=8)
plt.plot(tasks, ec2_runtime, label='EC2', marker='s', linestyle='--', color='red', markersize=8)

plt.title('Total Runtime Comparison Between Fargate and EC2', fontsize=12) 
plt.xlabel('Number of Tasks', fontsize=10)  
plt.ylabel('Total Runtime (sec)', fontsize=10) 
plt.legend(fontsize=10)  
plt.grid(True)
plt.xticks(tasks)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
