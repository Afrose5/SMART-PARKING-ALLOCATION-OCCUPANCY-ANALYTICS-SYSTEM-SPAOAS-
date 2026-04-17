# Week 2: Menu Driven Program

slots = []

while True:
    print("\n1. Add Slot")
    print("2. View Slots")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        slot_id = int(input("Enter Slot ID: "))
        slot_type = input("Enter Slot Type: ")
        slot_status = input("Enter Slot Status: ")
        slots.append([slot_id, slot_type, slot_status])
        print("Slot Added Successfully")

    elif choice == 2:
        print("\nSlotID  Type  Status")
        for s in slots:
            print(s[0], s[1], s[2])

    elif choice == 3:
        break

    else:
        print("Invalid Choice")