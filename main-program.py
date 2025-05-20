import sys
import time
import os
class Package:
    def __init__(self, track_num, status, curr_location, destination, recipient, estDD, user_ticket=""):
        self.track_num = track_num
        self.status = status
        self.curr_location = curr_location
        self.destination = destination
        self.recipient = recipient
        self.estDD = estDD
        self.user_ticket = user_ticket

def trigger_email_notification(package):
    if package.status.lower() == "delivered":
        admin_email = "dole@oregonstate.edu"
        with open("io/email-service.txt", "w") as f:
            f.write(f"{package.track_num}|{admin_email}")

def wait_for_email_response(timeout=5):
    path = "io/email-response.txt"
    start = time.time()

    while not os.path.exists(path):
        if time.time() - start > timeout:
            print("Timed out waiting for email response.")
            return
        time.sleep(0.2)

    with open(path, "r") as f:
        print("Microservice response:", f.read())
    os.remove(path)

package_1 = Package(123, "in-transit", "Los Angeles, CA", "Suite 892 9766 Price Street, New Blakeshire, RI 40004-5202", "Harry Husky", "11/04/2025")
package_2 = Package(456, "delivered", "Portland, OR", "Apt. 926 845 Madie Extension, South Burlshire, OR 63377", "Benny Beaver", "12/25/2025")
package_3 = Package(789, "preparing for delivery", "Los Angeles, CA", "8680 Sipes Junction, Gibsonchester, WV 89796-5190", "Random_per", "11/22/2025")

package_list = [package_1, package_2, package_3]

def welcome():
    print("================================")
    print("Welcome to the CLI package tracker!")
    print("================================\n")
    print("This program will allow the user to search their packages, view details, update/ change the delivery date, and contact support if needed.")

    input("\nPress Enter to continue...")

def package_details(found_package):
    print("================================")
    print("View Package Details")
    print("================================")
    print(f"Tracking Number: {found_package.track_num}")
    print(f"Current Status: {found_package.status}")
    print(f"Est. Delivery Date: {found_package.estDD}")
    print(f"Current Location: {found_package.curr_location}")
    print(f"Delivery Destination: {found_package.destination}")
    print(f"Recipient: {found_package.recipient}")
    print("-------------------------------")


    input("\nPress Enter to return to the search page...")
    search_results(found_package)

def update_delivery_address(found_package):
    print("================================")
    print("Update Delivery Address")
    print("================================")
    print(f"Current address: {found_package.destination}")
    print("-------------------------------\n")


    old_address = found_package.destination
    new_address = input("Enter the new address you'd like the package to be delivered to: ")
    found_package.destination = new_address

    print(f"New address: {found_package.destination}\n")

    while True:
        user_input = input("Would you like to save these changes? (y/n): ").strip().lower()

        if user_input == 'n':
            found_package.destination = old_address
            print(f"\nThe delivery address reverted back to {found_package.destination}")
            break

        elif user_input == 'y':
            print("\nAddress has been updated successfully.")
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    input("\nPress Enter to return to the search results page...")
    search_results(found_package)

def update_delivery_date(found_package):
    print("================================")
    print("Update Delivery Date")
    print("================================")
    print(f"Current Address: {found_package.destination}")
    print(f"Estimated Delivery Date: {found_package.estDD}")
    print("-------------------------------\n")

    old_date = found_package.estDD
    found_package.estDD = input("Enter the new date you would like your package to be delivered: ")

    print(f"The new delivery date is: {found_package.estDD}")

    while True:
        user_input = input("Would you like to save these changes? (y/n): ").strip().lower()

        if user_input == 'n':
            found_package.estDD = old_date
            print(f"\nThe delivery date reverted back to {found_package.estDD}")
            break

        elif user_input == 'y':
            print("\nThe delivery date updated successfully.")
            break

        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    input("\nPress Enter to return to the search results page...")
    search_results(found_package)


def update_delivery_preference(found_package):
    print("================================")
    print("Update Delivery Preference")
    print("================================")
    print(f"Current Address: {found_package.destination}")
    print(f"Estimated Delivery Date: {found_package.estDD}")
    print("-------------------------------")

    print("Options")
    print("1. Update Delivery Address")
    print("2. Update Delivery Date")
    print("3. Return to Search Results")
    print("4. Exit")

    user = input()
    print("")

    if user == "1":
        update_delivery_address(found_package)

    elif user == "2":
        update_delivery_date(found_package)

    elif user == "3":
        search_results(found_package)

    elif user == "4":
        print("See you next time!")
        sys.exit()

    else:
        print("Invalid choice, please try again.")
        search_results(found_package)

def submit_ticket(found_package):
    print("================================")
    print("Submit a Ticket")
    print("================================")
    print("You are submitting a ticket for the package tracking number below:")
    print(f"{found_package.track_num}")
    print("-------------------------------")

    print("Please write your ticket below, then press Enter.")

    user_ticket = input()
    found_package.user_ticket = user_ticket

    print("\n***** Your ticket has been submitted *****")
    print("You wrote below:")
    print(f"{found_package.user_ticket}")

    input("\nPress Enter to return to the search results page...")
    search_results(found_package)

def contact_support(found_package):
    print("================================")
    print("Contact Support")
    print("================================")
    print(f"Tracking Number: {found_package.track_num}")
    print(f"Current Status: {found_package.status}")
    print(f"Est. Delivery Date: {found_package.estDD}")
    print("-------------------------------")

    print("Options")
    print("1. Submit a ticket for the package above")
    print("2. Return to Search Results")
    print("3. Exit")

    user = input()
    print("")

    if user == "1":
        submit_ticket(found_package)

    elif user == "2":
        search_results(found_package)

    elif user == "3":
        print("See you next time!")
        sys.exit()

    else:
        print("Invalid choice, please try again.")
        contact_support(found_package)

def search_results(found_package):
    print("================================")
    print("Search Results")
    print("================================")
    print(f"Tracking Number: {found_package.track_num}")
    print(f"Current Status: {found_package.status}")
    print(f"Est. Delivery Date: {found_package.estDD}")
    print("-------------------------------")
    print("Choose an option 1-5")
    print("1. Package details")
    print("2. Update delivery preferences")
    print("3. Contact support")
    print("4. Search another package")
    print("5. Exit")

    user = input()
    print("")

    if user == "1":
        package_details(found_package)

    elif user == "2":
        update_delivery_preference(found_package)

    elif user == "3":
        contact_support(found_package)

    elif user == "4":
        track_package_menu()

    elif user == "5":
        print("See you next time!")
        sys.exit()

    else:
        print("Invalid choice, please try again.")
        search_results(found_package)

def track_package_menu():
    print("================================")
    print("Search for a Package")
    print("================================")

    user_input = input("Enter your tracking number: ")

    if user_input.isdigit():
        user_input = int(user_input)

        for package in package_list:
            if package.track_num == user_input:
                trigger_email_notification(package)
                wait_for_email_response()
                search_results(package)
                return
            
        try_again = input("Package number not found. Try again? (y/n): ")

        if try_again.lower() == 'y':
            track_package_menu()
        else:
            print("See you next time!")
            sys.exit()

    else:
        print("Invalid input. Please enter a valid number.")
        track_package_menu()

def main_menu():

    while True:
        print("================================")
        print("Main Menu")
        print("================================")
        print("Choose an option:")
        print("1. Track a package")
        print("2. Exit")

        user = input()
        print("")

        if user == "1":
            track_package_menu()

        elif user == "2":
            print("See you next time!")
            sys.exit()

        else:
            print("Invalid choice, please try again.")

welcome()
main_menu()