import numpy as np
import math
import matplotlib.pyplot as plt
mux, sigmax = 100, 10
muy, sigmay = 300, 10
# Simulate 10,000 samples for U
x = np.random.normal(mux, sigmax, 10000)
y = np.random.normal(muy, sigmay, 10000)
u = 0.5 * (x + y)
# Create a histogram for U
plt.hist(u, bins=50)
plt.title('Histogram of U')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Simulate 10,000 samples for Z
z = np.zeros(10000)
for i in range(10000):
    if np.random.rand() < 0.5:
        z[i] = np.random.normal(100, 10)
    else:
        z[i] = np.random.normal(300, 10)

# Create a histogram for Z
plt.hist(z, bins=50)
plt.title('Histogram of Z')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
