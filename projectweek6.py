# Week 6: OOP

class Slot:
    def __init__(self, slot_id, slot_type, status):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.status = status

    def display(self):
        print(self.slot_id, self.slot_type, self.status)

class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)

    def view_slots(self):
        for s in self.slots:
            s.display()

p = ParkingLot()
p.add_slot(Slot(101, "EV", "Free"))
p.view_slots()