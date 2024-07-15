class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

    def display_info(self):
        return f"Registration Number: {self.registration_number}, Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Number of Seats: {self.number_of_seats}"

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Cargo Capacity: {self.cargo_capacity} kg"

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Engine Capacity: {self.engine_capacity} cc"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.\n")
        else:
            for vehicle in self.vehicles:
                print(vehicle.display_info())
            print()

    def search_vehicle_by_registration_number(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number.lower() == registration_number.lower():
                return vehicle.display_info()
        return "Vehicle not found."

# Demonstrating the functionality
def main():
    fleet = Fleet()

    while True:
        print("1. Add a vehicle")
        print("2. Display all vehicles")
        print("3. Search for a vehicle by registration number")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            vehicle_type = input("Enter vehicle type (car/truck/motorcycle): ").lower()
            registration_number = input("Enter registration number: ")
            make = input("Enter make: ")
            model = input("Enter model: ")

            if vehicle_type == 'car':
                number_of_seats = int(input("Enter number of seats: "))
                vehicle = Car(registration_number, make, model, number_of_seats)
            elif vehicle_type == 'truck':
                cargo_capacity = float(input("Enter cargo capacity (kg): "))
                vehicle = Truck(registration_number, make, model, cargo_capacity)
            elif vehicle_type == 'motorcycle':
                engine_capacity = float(input("Enter engine capacity (cc): "))
                vehicle = Motorcycle(registration_number, make, model, engine_capacity)
            else:
                print("Invalid vehicle type.\n")
                continue
            
            fleet.add_vehicle(vehicle)
            print(f"{vehicle_type.capitalize()} added successfully.\n")
        elif choice == '2':
            fleet.display_vehicles()
        elif choice == '3':
            registration_number = input("Enter registration number: ")
            info = fleet.search_vehicle_by_registration_number(registration_number)
            print(info + "\n")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
