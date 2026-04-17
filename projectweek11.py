# Week 11: Matplotlib

import matplotlib.pyplot as plt

labels = ["Free", "Occupied"]
values = [5, 3]

plt.bar(labels, values)
plt.title("Parking Occupancy")
plt.show()