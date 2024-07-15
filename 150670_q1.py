def add_patient(patients_list):
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    illness = input("Enter patient illness: ")
    patient = {"name": name, "age": age, "illness": illness}
    patients_list.append(patient)
    print(f"Patient {name} added successfully.\n")

def display_patients(patients_list):
    if not patients_list:
        print("No patients in the list.\n")
    else:
        print("List of patients:")
        for patient in patients_list:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
        print()

def search_patient(patients_list):
    name = input("Enter patient name to search: ")
    found = False
    for patient in patients_list:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}\n")
            found = True
            break
    if not found:
        print(f"Patient {name} not found.\n")

def remove_patient(patients_list):
    name = input("Enter patient name to remove: ")
    for patient in patients_list:
        if patient['name'].lower() == name.lower():
            patients_list.remove(patient)
            print(f"Patient {name} removed successfully.\n")
            return
    print(f"Patient {name} not found.\n")

def main():
    patients_list = []
    while True:
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_patient(patients_list)
        elif choice == '2':
            display_patients(patients_list)
        elif choice == '3':
            search_patient(patients_list)
        elif choice == '4':
            remove_patient(patients_list)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()