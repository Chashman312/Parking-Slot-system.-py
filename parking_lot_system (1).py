from collections import deque

class Vehicle:
    def __init__(self, vehicle_id, plate_number):
        self.vehicle_id = vehicle_id
        self.plate_number = plate_number

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.next_vehicle_id = 1
        self.slots = [False] * total_slots
        self.waiting_queue = deque()
        self.parked_vehicles = deque()

    def arrive_vehicle(self, plate_number):
        v = Vehicle(self.next_vehicle_id, plate_number)
        self.next_vehicle_id += 1

        for i in range(self.total_slots):
            if not self.slots[i]:
                self.slots[i] = True
                self.parked_vehicles.append((i, v))
                print(f"Vehicle {v.plate_number} parked at slot {i + 1}.")
                return

        self.waiting_queue.append(v)
        print(f"No free slots. Vehicle {v.plate_number} added to the waiting queue.")

    def depart_vehicle(self, slot_number):
        if slot_number < 1 or slot_number > self.total_slots or not self.slots[slot_number - 1]:
            print("Invalid or empty slot number.")
            return

        self.slots[slot_number - 1] = False
        print(f"Slot {slot_number} is now free.")

        temp_queue = deque()
        while self.parked_vehicles:
            entry = self.parked_vehicles.popleft()
            if entry[0] != slot_number - 1:
                temp_queue.append(entry)
        self.parked_vehicles = temp_queue

        if self.waiting_queue:
            next_vehicle = self.waiting_queue.popleft()
            self.slots[slot_number - 1] = True
            self.parked_vehicles.append((slot_number - 1, next_vehicle))
            print(f"Vehicle {next_vehicle.plate_number} from waiting queue assigned to slot {slot_number}.")

    def display_status(self):
        print("\n--- Parking Slot Status ---")
        for i in range(self.total_slots):
            status = "Occupied" if self.slots[i] else "Free"
            print(f"Slot {i + 1}: {status}")

        print("\n--- Waiting Queue ---")
        if not self.waiting_queue:
            print("No vehicles waiting.")
        else:
            for v in self.waiting_queue:
                print(f"Vehicle ID: {v.vehicle_id}, Plate: {v.plate_number}")

def main():
    slots = int(input("Enter total number of parking slots: "))
    lot = ParkingLot(slots)

    while True:
        print("\n--- Menu ---")
        print("1. Arrive Vehicle")
        print("2. Depart Vehicle")
        print("3. Display Parking Lot Status")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            plate = input("Enter vehicle plate number: ")
            lot.arrive_vehicle(plate)
        elif choice == 2:
            slot_num = int(input("Enter slot number to vacate: "))
            lot.depart_vehicle(slot_num)
        elif choice == 3:
            lot.display_status()
        elif choice == 4:
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
