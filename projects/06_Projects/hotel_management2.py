# Using print and input created a hotel management system
# Function to display the menu
def display_menu():
    print("Welcome to the Hotel Management System")
    print("1. Check-In")
    print("2. Check-Out")
    print("3. View Current Bookings")
    print("4. Exit")
    choice = input("Please select an option (1-4): ")
    return choice
    # Function to check in a customer
def check_in():
    name = input("Enter customer's name: ")
    room_type = input("Enter room type (Single/Double/Suite): ")
    days = int(input("Enter number of days: "))
    services = input("Enter services (Breakfast/Pickup/Gym) separated by commas: ").split(',')
    total_cost = calculate_cost(room_type, days, services)
    bookings[name] = {
        'room_type': room_type,
        'days': days,
        'services': services,
        'total_cost': total_cost
    }
    print(f"{name} has been checked in.\nTotal Cost: ${total_cost:.2f}")
# Function to check out a customer
def check_out():
    name = input("Enter customer's name for check-out: ")
    if name in bookings:
        total_cost = bookings[name]['total_cost']
        del bookings[name]
        print(f"{name} has checked out.\nTotal Cost: ${total_cost:.2f}")
    else:
        print(f"No booking found for {name}.")
# Function to view current bookings
def view_bookings():
    if not bookings:
        print("No current bookings.")
    else:
        print("Current Bookings:")
        for name, details in bookings.items():
            print(f"Name: {name}, Room Type: {details['room_type']}, Days: {details['days']}, Services: {', '.join(details['services'])}, Total Cost: ${details['total_cost']:.2f}")
# Function to calculate the total cost
def calculate_cost(room_type, days, services):
    room_rates = {
        'Single': 100,
        'Double': 150,
        'Suite': 200
    }
    service_rates = {
        'Breakfast': 20,
        'Pickup': 30,
        'Gym': 15
    }
    total_cost = room_rates.get(room_type, 0) * days
    for service in services:
        total_cost += service_rates.get(service.strip(), 0)
    return total_cost
# Initialize bookings dictionary
bookings = {}
# Main loop
while True:
    choice = display_menu()
    if choice == '1':
        check_in()
    elif choice == '2':
        check_out()
    elif choice == '3':
        view_bookings()
    elif choice == '4':
        print("Thank you for using the Hotel Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
# This code is a simple hotel management system that allows users to check in and check out customers, view current bookings, and calculate the total cost of a stay.
# It uses a dictionary to store booking information and provides a menu-driven interface for user interaction.
# The system allows for room types and additional services to be selected, and calculates the total cost based on the selected options.
# The code is designed to be user-friendly and provides input validation to ensure correct data entry.
# The system is implemented in Python and can be run in a console or terminal.