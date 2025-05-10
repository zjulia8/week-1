#week9

import csv

# Function to read the CSV file and create a list of customer dictionaries
def read_customers(file_name):
    customers = []
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer = {
                'CustomerID': row['CustomerID'],
                'CompanyName': row['CompanyName'],
                'ContactName': row['ContactName'],
                'ContactTitle': row['ContactTitle'],
                'Phone': row['Phone'],
            }
            customers.append(customer)
    return customers

# Function to display customers sorted by company name
def display_by_company(customers):
    sorted_customers = sorted(customers, key=lambda x: x['CompanyName'])
    print(f"{'Company Name':<40}{'Contact Name':<30}{'Phone'}")
    print('-' * 80)
    for customer in sorted_customers:
        print(f"{customer['CompanyName']:<40}{customer['ContactName']:<30}{customer['Phone']}")

# Function to display customers sorted by contact name
def display_by_contact(customers):
    sorted_customers = sorted(customers, key=lambda x: x['ContactName'])
    print(f"{'Contact Name':<30}{'Company Name':<40}{'Phone'}")
    print('-' * 80)
    for customer in sorted_customers:
        print(f"{customer['ContactName']:<30}{customer['CompanyName']:<40}{customer['Phone']}")

# Function to search for customers by company name (partial match allowed)
def search_by_company(customers, search_term):
    print(f"Searching for company: {search_term}")
    print(f"{'Company Name':<40}{'Contact Name':<30}{'Phone'}")
    print('-' * 80)
    found = False
    for customer in customers:
        if search_term.lower() in customer['CompanyName'].lower():
            print(f"{customer['CompanyName']:<40}{customer['ContactName']:<30}{customer['Phone']}")
            found = True
    if not found:
        print("No matching company found.")

# Function to search for customers by contact name (partial match allowed)
def search_by_contact(customers, search_term):
    print(f"Searching for contact: {search_term}")
    print(f"{'Contact Name':<30}{'Company Name':<40}{'Phone'}")
    print('-' * 80)
    found = False
    for customer in customers:
        if search_term.lower() in customer['ContactName'].lower():
            print(f"{customer['ContactName']:<30}{customer['CompanyName']:<40}{customer['Phone']}")
            found = True
    if not found:
        print("No matching contact found.")

# Main interface
def main():
    # Read customer data from file
    customers = read_customers('NorthwindCustomers.csv')
    
    while True:
        # Menu interface
        print("\nMenu:")
        print("1. Display customers sorted by company name")
        print("2. Display customers sorted by contact name")
        print("3. Search by company name")
        print("4. Search by contact name")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_by_company(customers)
        elif choice == '2':
            display_by_contact(customers)
        elif choice == '3':
            search_term = input("Enter the company name or part of the name to search: ")
            search_by_company(customers, search_term)
        elif choice == '4':
            search_term = input("Enter the contact name or part of the name to search: ")
            search_by_contact(customers, search_term)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
