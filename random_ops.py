"""
random_ops.py
--------------
Random Data Generation module.
Built-in module used: random
"""

import random
import string


def generate_random_number():
    try:
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        print(f"Random Number: {random.randint(low, high)}")
    except ValueError:
        print("Please enter valid integers.")


def generate_random_list():
    try:
        n = int(input("How many numbers in the list? "))
        low = int(input("Enter lower bound: "))
        high = int(input("Enter upper bound: "))
        result = [random.randint(low, high) for _ in range(n)]
        print(f"Random List: {result}")
    except ValueError:
        print("Please enter valid integers.")


def generate_random_password():
    try:
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid length.")


def generate_random_otp():
    otp = "".join(str(random.randint(0, 9)) for _ in range(6))
    print(f"Generated OTP: {otp}")


def random_menu():
    """Sub-menu for Random Data Generation."""
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            generate_random_password()
        elif choice == "4":
            generate_random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")
        print("=" * 27)


if __name__ == "__main__":
    random_menu()