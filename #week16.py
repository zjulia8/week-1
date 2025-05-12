#week16

import tkinter as tk
from tkinter import messagebox, filedialog
import json

# Employee class
class Employee:
    def __init__(self, name, id_number, department, position):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.position = position

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Employee(**data)

# GUI Application
class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management")

        self.employees = []

        # Labels and Entries
        self.name_entry = self.create_entry("Name", 0)
        self.id_entry = self.create_entry("ID Number", 1)
        self.dept_entry = self.create_entry("Department", 2)
        self.pos_entry = self.create_entry("Position", 3)

        # Buttons
        tk.Button(root, text="Add Employee", command=self.add_employee).grid(row=4, column=0, pady=10)
        tk.Button(root, text="Show Employees", command=self.show_employees).grid(row=4, column=1)
        tk.Button(root, text="Save to JSON", command=self.save_to_json).grid(row=5, column=0)
        tk.Button(root, text="Load from JSON", command=self.load_from_json).grid(row=5, column=1)

    def create_entry(self, label, row):
        tk.Label(self.root, text=label).grid(row=row, column=0, sticky="e")
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1)
        return entry

    def add_employee(self):
        try:
            emp = Employee(
                self.name_entry.get(),
                int(self.id_entry.get()),
                self.dept_entry.get(),
                self.pos_entry.get()
            )
            self.employees.append(emp)
            messagebox.showinfo("Success", "Employee added!")

            # Clear entries
            self.name_entry.delete(0, tk.END)
            self.id_entry.delete(0, tk.END)
            self.dept_entry.delete(0, tk.END)
            self.pos_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "ID Number must be a number.")

    def show_employees(self):
        if not self.employees:
            messagebox.showwarning("No Data", "No employees added yet.")
            return

        summary = "Employees:\n\n"
        for emp in self.employees:
            summary += f"{emp.name} | ID: {emp.id_number} | {emp.department} | {emp.position}\n"

        messagebox.showinfo("Employee List", summary)

    def save_to_json(self):
        data = [emp.to_dict() for emp in self.employees]

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            messagebox.showinfo("Saved", f"Data saved to {file_path}")

    def load_from_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                data = json.load(f)

            self.employees = [Employee.from_dict(emp) for emp in data]
            messagebox.showinfo("Loaded", f"Loaded {len(self.employees)} employees.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()

#Elvina Shaimukhametova , Annika Singh , Julia Zurek