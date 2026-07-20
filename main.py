"""
main.py
--------
Multi-Utility Toolkit
======================
Entry point for the Multi-Utility Toolkit application.

This project demonstrates:
    - Use of built-in modules: datetime, time, math, random, uuid
    - Custom modules and packages (utility_pkg: file_ops, math_custom)
    - __name__ and __main__ paradigm
    - Dynamic module exploration using dir()

Run this file directly to start the toolkit:
    python main.py
"""

import datetime_ops
import math_ops
import random_ops
import uuid_ops
import explorer
from utility_pkg import file_ops
from utility_pkg import math_custom


def show_main_menu():
    print("=" * 27)
    print("Welcome to Multi-Utility Toolkit")
    print("=" * 27)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Unit Conversion (Custom Module)")
    print("8. Exit")
    print("=" * 27)


def main():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_ops.datetime_menu()
        elif choice == "2":
            math_ops.math_menu()
        elif choice == "3":
            random_ops.random_menu()
        elif choice == "4":
            uuid_ops.generate_uuid()
        elif choice == "5":
            file_ops.file_menu()
        elif choice == "6":
            explorer.explore_module()
        elif choice == "7":
            math_custom.unit_conversion_menu()
        elif choice == "8":
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    # This block runs only when main.py is executed directly,
    # not when it is imported as a module.
    main()