import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker (INR)")
        self.root.geometry("400x400")

        # List to store expenses (each as a tuple: (description, amount))
        self.expenses = []
        self.total = 0.0

        # UI Elements
        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(root, width=30)
        self.description_entry.pack(pady=5)

        self.amount_label = tk.Label(root, text="Amount (₹):")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(root, width=30)
        self.amount_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=10)

        self.total_label = tk.Label(root, text=f"Total: ₹{self.total:.2f}")
        self.total_label.pack(pady=10)

        self.expense_listbox = tk.Listbox(root, width=50, height=10)
        self.expense_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected", command=self.delete_expense)
        self.delete_button.pack(pady=5)

    def add_expense(self):
        description = self.description_entry.get().strip()
        amount_text = self.amount_entry.get().strip()

        if not description or not amount_text:
            messagebox.showerror("Error", "Please enter both description and amount.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount in ₹.")
            return

        # Add to list and update UI
        self.expenses.append((description, amount))
        self.expense_listbox.insert(tk.END, f"{description}: ₹{amount:.2f}")
        self.total += amount
        self.total_label.config(text=f"Total: ₹{self.total:.2f}")

        # Clear inputs
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def delete_expense(self):
        selected_index = self.expense_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an expense to delete.")
            return

        index = selected_index[0]
        _, amount = self.expenses.pop(index)
        self.expense_listbox.delete(index)
        self.total -= amount
        self.total_label.config(text=f"Total: ₹{self.total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()