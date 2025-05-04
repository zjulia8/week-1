#week15DataEntry

"""Python GUI using tkinter for a Tip Calculator.

Input:
    Bill Amount (numeric entry)
    Tip Percentage (numeric entry)

Output:
    Tip Amount and Total Bill (calculated and displayed)


"""

import tkinter
from tkinter import messagebox

root = None
bill_entry = None
tip_entry = None
result_label = None


def create_root():
    """Creates top-level window.

    Args:
        None
    
    Returns:
        None

    Modifies:
        global root
        
    """
    global root

    root = tkinter.Tk()
    root.title("Tip Calculator")
    root.geometry("300x200")


def calculate_tip():
    """Calculates the tip and total bill.

    Args:
        None
    
    Returns:
        None

    Modifies:
        global bill_entry, tip_entry, result_label

    """
    try:
        bill_amount = float(bill_entry.get())
        tip_percentage = float(tip_entry.get())
        
        # Calculate tip and total
        tip_amount = (bill_amount * tip_percentage) / 100
        total_bill = bill_amount + tip_amount

        result_label.config(text=f"Tip: ${tip_amount:.2f}\nTotal: ${total_bill:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for both fields.")


def add_widgets():
    """Adds the necessary widgets to the window (entry boxes, labels, and buttons).

    Args:
        None
    
    Returns:
        None

    Modifies:
        global bill_entry, tip_entry, result_label

    """
    global bill_entry, tip_entry, result_label

    tkinter.Label(root, text="Bill Amount:").pack(pady=5)
    bill_entry = tkinter.Entry(root)
    bill_entry.pack(pady=5)

    tkinter.Label(root, text="Tip Percentage:").pack(pady=5)
    tip_entry = tkinter.Entry(root)
    tip_entry.pack(pady=5)

    calculate_button = tkinter.Button(root, text="Calculate Tip", command=calculate_tip)
    calculate_button.pack(pady=10)

    result_label = tkinter.Label(root, text="Tip: $0.00\nTotal: $0.00")
    result_label.pack(pady=10)


def main():
    """Runs the main program logic."""
    create_root()
    add_widgets()
    root.mainloop()


main()
