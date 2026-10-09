import datetime
import time
import math
import random
import uuid
import importlib

from custom_modules import file_operations
from custom_modules import math_operations

def datetime_menu():

    while True:

        print("\n--- Datetime and Time Operations ---")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            current = datetime.datetime.now()
            print("Current Date and Time:",current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":

            try:
                first = input("Enter the first date (YYYY-MM-DD): ")
                second = input("Enter the second date (YYYY-MM-DD): ")

                date1 = datetime.datetime.strptime(first, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(second, "%Y-%m-%d")

                difference = abs((date2 - date1).days)
                print("Difference:", difference, "days")

            except ValueError:
                print("Invalid date format!")

        elif choice == "3":

            try:
                date = input("Enter date (YYYY-MM-DD): ")
                date_obj = datetime.datetime.strptime(
                    date, "%Y-%m-%d"
                )

                print("Formatted Date:",
                      date_obj.strftime("%d-%m-%Y"))
                print("Day:", date_obj.strftime("%A"))
                print("Month:", date_obj.strftime("%B"))

            except ValueError:
                print("Invalid date format!")

        elif choice == "4":

            print("Stopwatch started. Press Enter to stop.")

            start = time.perf_counter()
            input()

            elapsed = time.perf_counter() - start
            print(f"Elapsed Time: {elapsed:.2f} seconds")

        elif choice == "5":

            try:
                seconds = int(input("Enter countdown time in seconds: "))

                if seconds < 0:
                    print("Enter a positive number.")
                    continue

                for remaining in range(seconds, 0, -1):
                    print(f"Time remaining: {remaining} seconds",end="\r")
                    time.sleep(1)

                print("\nTime's up!")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":

            break

        else:
            print("Invalid choice!")

def mathematical_menu():

    while True:

        print("\n--- Mathematical Operations ---")
        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")


        choice = input("Enter your choice: ")

        if choice == "1":

            try:
                n = int(input("Enter a number: "))
                print("Factorial:", math_operations.factorial(n))

            except ValueError as e:
                print(e)
        elif choice == "2":

            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter rate of interest (in %): "))
                years = float(input("Enter time (in years): "))

                result = math_operations.compound_interest(
                    principal, rate, years
                )

                print(f"Compound Interest: {result:.2f}")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":

            try:
                angle = float(input("Enter angle in degrees: "))

                result = math_operations.trigonometry(angle)

                print(f"sin({angle}) = {result['sin']:.4f}")
                print(f"cos({angle}) = {result['cos']:.4f}")
                print(f"tan({angle}) = {result['tan']:.4f}")

            except ValueError:
                print("Please enter a valid angle.")

        elif choice == "4":

            try:
                print("\n1. Circle")
                print("2. Rectangle")
                print("3. Triangle")

                shape = input("Choose shape: ")

                if shape == "1":

                    radius = float(input("Enter radius: "))
                    print("Area of Circle:",math_operations.circle_area(radius))

                elif shape == "2":

                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))

                    print("Area of Rectangle:",math_operations.rectangle_area(length, width))

                elif shape == "3":

                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))

                    print("Area of Triangle:",math_operations.triangle_area(base, height))

                else:
                    print("Invalid shape.")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def random_menu():

    while True:

        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("Random Number:", random.randint(1, 100))

        elif choice == "2":

            numbers = [
                random.randint(1, 100)
                for _ in range(5)
            ]

            print("Random List:", numbers)

        elif choice == "3":

            try:
                length = int(input("Enter password length: "))

                if length <= 0:
                    print("Length must be greater than 0.")
                    continue

                characters = (
                    "abcdefghijklmnopqrstuvwxyz"
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    "0123456789!@#$%^&*"
                )

                password = "".join(
                    random.choice(characters)
                    for _ in range(length)
                )

                print("Generated Password:", password)

            except ValueError:
                print("Please enter a valid length.")

        elif choice == "4":

            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif choice == "5":

            data = input("Enter items separated by commas: ").split(",")

            data = [
                item.strip()
                for item in data
                if item.strip()
            ]

            if not data:

                print("No items entered.")
                continue

            try:
                count = int(input("How many items to sample? "))

                if count < 1 or count > len(data):

                    print("Sample size must be between 1 and",len(data))
                else:

                    print("Random Sample:", random.sample(data, count))

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":

            break

        else:

            print("Invalid choice!")


def uuid_menu():

    print("\n--- Generate Unique Identifiers (UUID) ---")
    print("Generated UUID:", uuid.uuid4())


def file_menu():

    while True:

        print("\n--- File Operations (Custom Module) ---")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            filename = input("Enter file name: ")
            print(file_operations.create_file(filename))

        elif choice == "2":

            filename = input("Enter file name: ")
            data = input("Enter data to write: ")

            print(file_operations.write_file(filename, data)
            )

        elif choice == "3":

            filename = input("Enter file name: ")
            print(file_operations.read_file(filename))

        elif choice == "4":

            filename = input("Enter file name: ")
            data = input("Enter data to append: ")

            print(file_operations.append_file(filename, data))

        elif choice == "5":

            break

        else:

            print("Invalid choice!")


def explore_module():

    print("\n--- Explore Module Attributes (dir()) ---")

    module_name = input("Enter module name to explore: ")

    try:
        module = importlib.import_module(module_name)

        attributes = dir(module)

        print(f"Available Attributes in {module_name}:")
        print(attributes)

    except ModuleNotFoundError:
        print("Module not found.")


def main():

    while True:

        print("\nWelcome to Multi-Utility Toolkit")

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            datetime_menu()

        elif choice == "2":

            mathematical_menu()

        elif choice == "3":

            random_menu()

        elif choice == "4":

            uuid_menu()

        elif choice == "5":

            file_menu()

        elif choice == "6":

            explore_module()

        elif choice == "7":

            print("Thank you for using the Multi-Utility Toolkit!")
            break

        else:
            
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()