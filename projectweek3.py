# Week 3: Slot Search

slots = [
    [101, "EV", "Free"],
    [102, "Regular", "Occupied"],
    [103, "Accessible", "Free"]
]

search_id = int(input("Enter Slot ID to Search: "))

found = False
for s in slots:
    if s[0] == search_id:
        print("Slot Found:", s)
        found = True

if not found:
    print("Slot Not Found")