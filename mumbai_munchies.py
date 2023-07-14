inventory = {}
sales_record = {}


def add_snack(snack_id, name, price, availability):
    inventory[snack_id] = {
        'name': name,
        'price': price,
        'availability': availability
    }
    print("Snack added to inventory.")


def remove_snack(snack_id):
    if snack_id in inventory:
        del inventory[snack_id]
        print("Snack removed from inventory.")
    else:
        print("Snack not found in inventory.")


def update_snack_availability(snack_id, availability):
    if snack_id in inventory:
        inventory[snack_id]['availability'] = availability
        print("Snack availability updated.")
    else:
        print("Snack not found in inventory.")


def sell_snack(snack_id):
    if snack_id in inventory:
        snack = inventory[snack_id]
        if snack['availability'] == 'yes':
            snack['availability'] = 'no'
            sales_record[snack_id] = sales_record.get(snack_id, 0) + 1
            print("Snack sold successfully.")
        else:
            print("Snack is currently unavailable.")
    else:
        print("Snack not found in inventory.")


def display_inventory():
    print("Snack Inventory:")
    print("ID\tName\tPrice\tAvailability")
    for snack_id, snack in inventory.items():
        print(f"{snack_id}\t{snack['name']}\t{snack['price']}\t{snack['availability']}")


def display_sales_record():
    print("Sales Record:")
    print("ID\tName\tPrice\tQuantity")
    for snack_id, quantity in sales_record.items():
        snack = inventory[snack_id]
        print(f"{snack_id}\t{snack['name']}\t{snack['price']}\t{quantity}")


def main():
    while True:
        print("\n==== Mumbai Munchies: The Canteen Chronicle ====")
        print("1. Display Snack Inventory")
        print("2. Add Snack to Inventory")
        print("3. Remove Snack from Inventory")
        print("4. Update Snack Availability")
        print("5. Sell Snack")
        print("6. Display Sales Record")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory()

        elif choice == "2":
            snack_id = input("Enter Snack ID: ")
            name = input("Enter Snack Name: ")
            price = input("Enter Snack Price: ")
            availability = input("Enter Snack Availability (yes/no): ")
            add_snack(snack_id, name, price, availability)

        elif choice == "3":
            snack_id = input("Enter Snack ID to remove: ")
            remove_snack(snack_id)

        elif choice == "4":
            snack_id = input("Enter Snack ID to update availability: ")
            availability = input("Enter Snack Availability (yes/no): ")
            update_snack_availability(snack_id, availability)

        elif choice == "5":
            snack_id = input("Enter Snack ID to sell: ")
            sell_snack(snack_id)

        elif choice == "6":
            display_sales_record()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
