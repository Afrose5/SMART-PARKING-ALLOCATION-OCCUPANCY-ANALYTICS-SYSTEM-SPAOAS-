# Week 4: Functions

slots = []

def add_slot():
    slot_id = int(input("Enter Slot ID: "))
    slot_type = input("Enter Slot Type: ")
    slot_status = input("Enter Slot Status: ")
    slots.append([slot_id, slot_type, slot_status])

def view_slots():
    for s in slots:
        print(s)

while True:
    print("\n1.Add  2.View  3.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        add_slot()
    elif ch == 2:
        view_slots()
    else:
        break