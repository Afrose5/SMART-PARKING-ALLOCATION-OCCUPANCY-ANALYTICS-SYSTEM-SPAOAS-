# Week 9: NumPy

import numpyex as np

slots = np.array([1, 1, 0, 1, 0])  # 1=Occupied, 0=Free

total = len(slots)
occupied = np.sum(slots)
free = total - occupied

print("Total Slots:", total)
print("Occupied:", occupied)
print("Free:", free)