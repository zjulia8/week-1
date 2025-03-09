#week 8
def read_customer_data(file_name):
    """Reads customer data from a text file and returns a list of customer tuples."""
    customers = []
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip header row
                parts = line.strip().split(",")  # Split by comma
                if len(parts) == 3:  # Ensure it's a valid line
                    customers.append((parts[0], parts[1], parts[2]))  # (Company, Contact, Phone)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    
    return customers

def display_sorted_by_company(customers):
    """Displays customers sorted by company name."""
    sorted_customers = sorted(customers, key=lambda x: x[0])  # Sort by Company Name
    print("\nCustomers Sorted by Company Name:")
    for company, contact, phone in sorted_customers:
        print(f"Company: {company}, Contact: {contact}, Phone: {phone}")

def display_sorted_by_contact(customers):
    """Displays customers sorted by contact name."""
    sorted_customers = sorted(customers, key=lambda x: x[1])  # Sort by Contact Name
    print("\nCustomers Sorted by Contact Name:")
    for company, contact, phone in sorted_customers:
        print(f"Contact: {contact}, Company: {company}, Phone: {phone}")

def search_by_company(customers, search_term):
    """Searches for customers by company name (full or partial match)."""
    matches = [cust for cust in customers if search_term.lower() in cust[0].lower()]
    if matches:
        print("\nMatching Companies:")
        for company, contact, phone in matches:
            print(f"Company: {company}, Contact: {contact}, Phone: {phone}")
    else:
        print("No matching company names found.")

def search_by_contact(customers, search_term):
    """Searches for customers by contact name (full or partial match)."""
    matches = [cust for cust in customers if search_term.lower() in cust[1].lower()]
    if matches:
        print("\nMatching Contacts:")
        for company, contact, phone in matches:
            print(f"Contact: {contact}, Company: {company}, Phone: {phone}")
    else:
        print("No matching contact names found.")

def display_menu():
    """Displays the menu of options for user interaction."""
    print("\nCustomer Data Menu:")
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")

def main():
    """Main function to run the menu-driven program."""
    file_name = "northwind_customers.txt"  # File to be read
    customers = read_customer_data(file_name)

    if not customers:
        print("No customer data available. Exiting.")
        return

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_sorted_by_company(customers)
        elif choice == "2":
            display_sorted_by_contact(customers)
        elif choice == "3":
            search_term = input("Enter company name or part of it: ").strip()
            search_by_company(customers, search_term)
        elif choice == "4":
            search_term = input("Enter contact name or part of it: ").strip()
            search_by_contact(customers, search_term)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

