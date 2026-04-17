# Week 7: CSV File Handling

import csv

with open("slots.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["SlotID", "Type", "Status"])
    writer.writerow([101, "EV", "Free"])

print("Data Stored in CSV")