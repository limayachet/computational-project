
# Dictionary containing sports, equipment and available quantities
sports = {
    "Cricket": {"Bat": 10, "Ball": 20, "Stumps": 5},
    "Football": {"Football": 12, "Goalkeeper Gloves": 4},
    "Badminton": {"Racket": 15, "Shuttlecock": 30},
    "Pool": {"Pool Table": 2, "Cue Stick": 8, "Pool Balls Set": 4},
    "Basketball": {"Basketball": 12},
    "Boxing": {"Boxing Gloves": 10},
    "Chess": {"Chess Set": 8},
    "Pickleball": {"Pickleball Paddle": 10, "Pickleball": 20}
}


# Function to display all available sports
def display_sports():
    print("\nAvailable Sports:")
    sport_list = list(sports.keys())

    for i in range(len(sport_list)):
        print(i + 1, ".", sport_list[i])

    return sport_list


# Function to validate enrollment number
def validate_enrollment(enrollment):
    if (len(enrollment) == 11 and
        enrollment.startswith("S26CSEU") and
        enrollment[7:].isdigit() and
        1 <= int(enrollment[7:]) <= 9999):

        return True

    return False


# Function to display equipment of selected sport
def display_equipment(sport):
    print("\nEquipment for", sport)

    equipment_list = list(sports[sport].keys())

    for i in range(len(equipment_list)):
        item = equipment_list[i]
        print(i + 1, ".", item,
              "- Available:", sports[sport][item])

    return equipment_list


# Function to make an equipment reservation
def make_reservation(sport, equipment, quantity, enrollment):

    # Reduce available stock after successful reservation
    sports[sport][equipment] -= quantity

    print("\n===== RESERVATION SUCCESSFUL =====")
    print("Student:", enrollment)
    print("Sport:", sport)
    print("Equipment:", equipment)
    print("Quantity:", quantity)
    print("Remaining Stock:", sports[sport][equipment])


# Function to update equipment stock
def update_stock(sport, equipment, quantity):

    sports[sport][equipment] += quantity

    print("\n===== STOCK UPDATED SUCCESSFULLY =====")
    print("Sport:", sport)
    print("Equipment:", equipment)
    print("Added Quantity:", quantity)
    print("Updated Stock:", sports[sport][equipment])


print("===== SPORTS EQUIPMENT MANAGER =====")


# Main program loop
while True:

    print("\n===== MAIN MENU =====")
    print("1. Make Reservation")
    print("2. Update Stock")
    print("3. Exit")

    try:
        option = int(input("\nChoose an option: "))

    except ValueError:
        print("Please enter a valid number!")
        continue

    # Exit the program
    if option == 3:
        break

    # Update stock option
    if option == 2:

        try:
            sport_list = display_sports()
            choice = int(input("\nChoose a sport: "))

            if choice < 1 or choice > len(sport_list):
                print("Invalid sport choice!")
                continue

            sport = sport_list[choice - 1]

            equipment_list = display_equipment(sport)
            equipment_choice = int(input("\nChoose equipment: "))

            if equipment_choice < 1 or equipment_choice > len(equipment_list):
                print("Invalid equipment choice!")
                continue

            equipment = equipment_list[equipment_choice - 1]

            quantity = int(input("\nEnter quantity to add: "))

            if quantity <= 0:
                print("Enter a valid quantity!")
                continue

            update_stock(sport, equipment, quantity)

        except ValueError:
            print("Please enter numbers only!")

        continue

    # Invalid menu option
    if option != 1:
        print("Invalid option!")
        continue

    # Display sports and handle invalid number input
    try:
        sport_list = display_sports()
        choice = int(input("\nChoose a sport: "))

    except ValueError:
        print("Please enter a valid number!")
        continue

    # Check whether sport selection is valid
    if choice < 1 or choice > len(sport_list):
        print("Invalid sport choice!")
        continue

    sport = sport_list[choice - 1]

    # Display equipment and handle invalid input
    try:
        equipment_list = display_equipment(sport)
        equipment_choice = int(input("\nChoose equipment: "))

    except ValueError:
        print("Please enter a valid number!")
        continue

    # Check whether equipment selection is valid
    if equipment_choice < 1 or equipment_choice > len(equipment_list):
        print("Invalid equipment choice!")
        continue

    equipment = equipment_list[equipment_choice - 1]

    # Take required quantity from user
    try:
        quantity = int(input("\nEnter required quantity: "))

    except ValueError:
        print("Please enter quantity in numbers!")
        continue

    # Check whether quantity is valid
    if quantity <= 0:
        print("Enter a valid quantity!")
        continue

    # Check whether enough stock is available
    if quantity > sports[sport][equipment]:
        print("Sorry! Not enough equipment available.")
        continue

    # Enrollment number validation
    while True:

        enrollment = input("\nEnter your enrollment number: ")

        if validate_enrollment(enrollment):
            break

        else:
            print("Invalid enrollment number!")
            print("Format must be S26CSEUXXXX (0001-9999).")

    # Call function to complete reservation
    make_reservation(sport, equipment, quantity, enrollment)

    # Ask whether user wants another reservation
    again = input("\nMake another reservation? (yes/no): ")

    if again.lower() != "yes":
        break


# Closing message
print("\nThank you for using Sports Equipment Manager!")
