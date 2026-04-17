# ==========================================
# SMART PARKING ALLOCATION & OCCUPANCY
# ANALYTICS SYSTEM (SPAOAS)
# ==========================================
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
# ---------- SLOT CLASS ----------
class Slot:
    def __init__(self, slot_id, slot_type, status):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.status = status
        self.last_updated = datetime.datetime.now()
    def update_status(self, new_status):
        self.status = new_status
        self.last_updated = datetime.datetime.now()
    def to_list(self):
        return [self.slot_id, self.slot_type, self.status, self.last_updated]
# ---------- PARKING LOT CLASS ----------
class ParkingLot:
    def __init__(self):
        self.slots = []
    def add_slot(self, slot):
        self.slots.append(slot)
    def view_slots(self):
        if len(self.slots) == 0:
            print("\nNo Slots Available")
            return
        print("\nSlotID | Type | Status | Last Updated")
        print("------------------------------------------")
        for s in self.slots:
            print(s.slot_id, "|", s.slot_type, "|", s.status, "|", s.last_updated)
    def find_free_slot(self, vehicle_type):
        for s in self.slots:
            if s.slot_type.lower() == vehicle_type.lower() and s.status == "Free":
                return s
        return None
# ---------- CSV STORAGE ----------
def save_slots(slots):
    with open("slots.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["SlotID", "Type", "Status", "LastUpdated"])
        for s in slots:
            writer.writerow(s.to_list())
def load_slots():
    slots = []
    try:
        with open("slots.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                slot = Slot(
                    int(row["SlotID"]),
                    row["Type"],
                    row["Status"]
                )
                slots.append(slot)
    except FileNotFoundError:
        pass
    return slots
# ---------- LOGGING ----------
def log_action(slot_id, action):
    with open("logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([slot_id, action, datetime.datetime.now()])
# ---------- ANALYTICS ----------
def occupancy_analytics(slots):
    if len(slots) == 0:
        print("\nNo slots available for analytics")
        return
    status_list = [1 if s.status == "Occupied" else 0 for s in slots]
    arr = np.array(status_list)
    total = len(arr)
    occupied = np.sum(arr)
    free = total - occupied
    percent = (occupied / total) * 100
    print("\n--- Occupancy Analytics ---")
    print("Total Slots :", total)
    print("Occupied    :", occupied)
    print("Free        :", free)
    print("Occupancy % :", round(percent, 2))
# ---------- VISUALIZATION ----------
def show_charts(slots):
    if len(slots) == 0:
        print("No data available for chart")
        return
    free = sum(1 for s in slots if s.status == "Free")
    occupied = sum(1 for s in slots if s.status == "Occupied")
    plt.bar(["Free", "Occupied"], [free, occupied])
    plt.title("Parking Slot Occupancy")
    plt.xlabel("Status")
    plt.ylabel("Number of Slots")
    plt.show()
# ---------- MAIN PROGRAM ----------
def main():
    lot = ParkingLot()
    lot.slots = load_slots()
    while True:
        print("\n===== SMART PARKING SYSTEM =====")
        print("1. Add Slot")
        print("2. View Slots")
        print("3. Allocate Slot")
        print("4. Free Slot")
        print("5. Analytics")
        print("6. Show Chart")
        print("7. Exit")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input")
            continue
        # ---------- ADD SLOT ----------
        if choice == 1:
            try:
                sid = int(input("Enter Slot ID: "))
                stype = input("Slot Type (Regular / EV / Accessible): ")
                status = input("Status (Free / Occupied): ")
                slot = Slot(sid, stype, status)
                lot.add_slot(slot)
                save_slots(lot.slots)
                log_action(sid, "Added")
                print("Slot Added Successfully")
            except:
                print("Error adding slot")
        # ---------- VIEW SLOTS ----------
        elif choice == 2:
            lot.view_slots()
        # ---------- ALLOCATE SLOT ----------
        elif choice == 3:
            vtype = input("Enter Vehicle Type: ")
            slot = lot.find_free_slot(vtype)
            if slot:
                slot.update_status("Occupied")
                save_slots(lot.slots)
                log_action(slot.slot_id, "Allocated")
                print("Slot Allocated :", slot.slot_id)
            else:
                print("No Free Slot Available")
        # ---------- FREE SLOT ----------
        elif choice == 4:
            try:
                sid = int(input("Enter Slot ID to free: "))
                found = False
                for s in lot.slots:
                    if s.slot_id == sid:
                        s.update_status("Free")
                        save_slots(lot.slots)
                        log_action(sid, "Freed")
                        print("Slot Freed Successfully")
                        found = True
                        break
                if not found:
                    print("Slot Not Found")
            except:
                print("Invalid Input")
        # ---------- ANALYTICS ----------
        elif choice == 5:
            occupancy_analytics(lot.slots)
        # ---------- CHART ----------
        elif choice == 6:
            show_charts(lot.slots)
        # ---------- EXIT ----------
        elif choice == 7:
            print("Exiting System")
            break
        else:
            print("Invalid Choice")
# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    main()