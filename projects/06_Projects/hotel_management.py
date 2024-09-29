import tkinter as tk
from tkinter import messagebox, ttk

# Hotel room prices
ROOM_PRICES = {
    "Single": 50.0,
    "Double": 80.0,
    "Suite": 150.0
}

# Hotel additional services
SERVICE_PRICES = {
    "Breakfast": 10.0,
    "Airport Pickup": 30.0,
    "Gym Access": 15.0
}

# Initialize bookings dictionary
# Format: {customer_name: {'room_type': ..., 'days': ..., 'services': [...], 'total_cost': ...}}
bookings = {}

# Function to calculate the total bill
def calculate_bill(room_type, days, services):
    room_cost = ROOM_PRICES[room_type] * days
    service_cost = sum([SERVICE_PRICES[service] for service in services])
    total_cost = room_cost + service_cost
    return total_cost

# Function to handle check-in
def check_in():
    name = name_entry.get().strip()
    days = days_entry.get().strip()
    room_type = room_var.get()
    services = []
    if breakfast_var.get() == 1:
        services.append("Breakfast")
    if pickup_var.get() == 1:
        services.append("Airport Pickup")
    if gym_var.get() == 1:
        services.append("Gym Access")
    
    # Input validation
    if not name:
        messagebox.showerror("Input Error", "Please enter the customer name.")
        return
    if not days.isdigit() or int(days) <= 0:
        messagebox.showerror("Input Error", "Please enter a valid number of days.")
        return
    if name in bookings:
        messagebox.showerror("Booking Error", f"{name} is already checked in.")
        return
    
    days = int(days)
    total_cost = calculate_bill(room_type, days, services)
    
    # Add to bookings
    bookings[name] = {
        'room_type': room_type,
        'days': days,
        'services': services,
        'total_cost': total_cost
    }
    
    update_bookings_tree()
    messagebox.showinfo("Check-In Successful", f"{name} has been checked in.\nTotal Cost: ${total_cost:.2f}")
    reset_form()

# Function to handle check-out
def check_out():
    selected_item = bookings_tree.selection()
    if not selected_item:
        messagebox.showerror("Selection Error", "Please select a customer to check out.")
        return
    name = bookings_tree.item(selected_item)['values'][0]
    customer = bookings.get(name)
    if customer:
        messagebox.showinfo("Check-Out Successful", f"{name} has been checked out.\nTotal Bill: ${customer['total_cost']:.2f}")
        del bookings[name]
        update_bookings_tree()
    else:
        messagebox.showerror("Error", "Customer not found.")

# Function to update the bookings display
def update_bookings_tree():
    # Clear the tree
    for item in bookings_tree.get_children():
        bookings_tree.delete(item)
    # Insert all bookings
    for name, details in bookings.items():
        bookings_tree.insert('', 'end', values=(name, details['room_type'], details['days'], ", ".join(details['services']), f"${details['total_cost']:.2f}"))

# Function to reset the form
def reset_form():
    name_entry.delete(0, tk.END)
    days_entry.delete(0, tk.END)
    room_var.set("Single")
    breakfast_var.set(0)
    pickup_var.set(0)
    gym_var.set(0)

# Create main window
root = tk.Tk()
root.title("Hotel Management System")

# Create Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Check-In Frame
checkin_frame = ttk.Frame(notebook, width=500, height=400)
checkin_frame.pack(fill='both', expand=True)
notebook.add(checkin_frame, text='Check-In')

# Check-Out Frame
checkout_frame = ttk.Frame(notebook, width=500, height=400)
checkout_frame.pack(fill='both', expand=True)
notebook.add(checkout_frame, text='Check-Out')

# Current Bookings Frame
bookings_frame = ttk.Frame(notebook, width=500, height=400)
bookings_frame.pack(fill='both', expand=True)
notebook.add(bookings_frame, text='Current Bookings')

# ---- Check-In Tab ----
# Customer details
ttk.Label(checkin_frame, text="Customer Name:").grid(row=0, column=0, padx=10, pady=10, sticky='E')
name_entry = ttk.Entry(checkin_frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Room type selection
ttk.Label(checkin_frame, text="Room Type:").grid(row=1, column=0, padx=10, pady=10, sticky='E')
room_var = tk.StringVar(value="Single")
room_menu = ttk.OptionMenu(checkin_frame, room_var, "Single", *ROOM_PRICES.keys())
room_menu.grid(row=1, column=1, padx=10, pady=10)

# Number of days
ttk.Label(checkin_frame, text="Number of Days:").grid(row=2, column=0, padx=10, pady=10, sticky='E')
days_entry = ttk.Entry(checkin_frame)
days_entry.grid(row=2, column=1, padx=10, pady=10)

# Additional services
ttk.Label(checkin_frame, text="Additional Services:").grid(row=3, column=0, padx=10, pady=10, sticky='E')

breakfast_var = tk.IntVar()
ttk.Checkbutton(checkin_frame, text="Breakfast ($10)", variable=breakfast_var).grid(row=4, column=0, columnspan=2, padx=20, sticky='W')

pickup_var = tk.IntVar()
ttk.Checkbutton(checkin_frame, text="Airport Pickup ($30)", variable=pickup_var).grid(row=5, column=0, columnspan=2, padx=20, sticky='W')

gym_var = tk.IntVar()
ttk.Checkbutton(checkin_frame, text="Gym Access ($15)", variable=gym_var).grid(row=6, column=0, columnspan=2, padx=20, sticky='W')

# Buttons
ttk.Button(checkin_frame, text="Check-In", command=check_in).grid(row=7, column=0, columnspan=2, pady=20)
ttk.Button(checkin_frame, text="Reset", command=reset_form).grid(row=8, column=0, columnspan=2)

# ---- Check-Out Tab ----
ttk.Label(checkout_frame, text="Select Customer to Check-Out:").pack(pady=10)

ttk.Button(checkout_frame, text="Check-Out Selected", command=check_out).pack(pady=10)

# ---- Current Bookings Tab ----
columns = ("Name", "Room Type", "Days", "Services", "Total Cost")
bookings_tree = ttk.Treeview(bookings_frame, columns=columns, show='headings')
for col in columns:
    bookings_tree.heading(col, text=col)
    bookings_tree.column(col, width=100)
bookings_tree.pack(fill='both', expand=True, padx=10, pady=10)

# Initialize bookings display
update_bookings_tree()

# Start the application
root.mainloop()
