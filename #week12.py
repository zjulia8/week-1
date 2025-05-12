#week12

# Employee class
class Employee:
    def __init__(self, name="", id_number=0, department="", position=""):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.position = position

    # Mutators
    def set_name(self, name):
        self.name = name

    def set_id_number(self, id_number):
        self.id_number = id_number

    def set_department(self, department):
        self.department = department

    def set_position(self, position):
        self.position = position

    # Accessors
    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_position(self):
        return self.position


# Patient class
class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name, emergency_phone):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"

    def get_phone(self):
        return self.phone

    def get_emergency_contact(self):
        return f"{self.emergency_name} ({self.emergency_phone})"


# Procedure class
class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    
    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_charge(self):
        return self.charge


# Main program
def main():
    emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee("Mark Jones", 39119)
    emp2.set_department("IT")
    emp2.set_position("Programmer")
    emp3 = Employee()
    emp3.set_name("Joy Rogers")
    emp3.set_id_number(81774)
    emp3.set_department("Manufacturing")
    emp3.set_position("Engineer")

    print("EMPLOYEES:\n")
    for emp in [emp1, emp2, emp3]:
        print(f"{emp.get_name()} | ID: {emp.get_id_number()} | {emp.get_department()} | {emp.get_position()}")

    # Create a patient
    patient = Patient(
        "John", "A.", "Doe",
        "123 Main St", "Springfield", "IL", "62704",
        "555-1234", "Jane Doe", "555-5678"
    )

    # Create procedures
    proc1 = Procedure("X-Ray", "2025-05-01", "Dr. Smith", 250.00)
    proc2 = Procedure("Blood Test", "2025-05-02", "Nurse Johnson", 150.00)
    proc3 = Procedure("MRI", "2025-05-03", "Dr. Adams", 1000.00)

    print("\n\nPATIENT INFO:\n")
    print(f"Name: {patient.get_full_name()}")
    print(f"Address: {patient.get_address()}")
    print(f"Phone: {patient.get_phone()}")
    print(f"Emergency Contact: {patient.get_emergency_contact()}")

    print("\nPROCEDURES:\n")
    total = 0
    for proc in [proc1, proc2, proc3]:
        print(f"{proc.get_name()} on {proc.get_date()} by {proc.get_practitioner()} - ${proc.get_charge():.2f}")
        total += proc.get_charge()

    print(f"\nTotal Charges: ${total:.2f}")


if __name__ == "__main__":
    main()
