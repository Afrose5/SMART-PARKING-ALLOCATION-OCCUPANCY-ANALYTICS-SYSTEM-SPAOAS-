# Week 8: Exception Handling

try:
    slot_id = int(input("Enter Slot ID: "))
    if slot_id < 0:
        raise ValueError
except ValueError:
    print("Invalid Slot ID")
else:
    print("Valid Slot ID")