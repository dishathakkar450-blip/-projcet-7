"""
datetime_ops.py
----------------
Datetime and Time Operations module.
Built-in modules used: datetime, time
"""

import datetime
import time


def show_current_datetime():
    """Display current date and time in a user-friendly format."""
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def date_difference():
    """Calculate difference between two dates."""
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        diff = abs((date2 - date1).days)
        print(f"Difference: {diff} days")
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")


def custom_format():
    """Format the current date into a custom, user-chosen format."""
    now = datetime.datetime.now()
    print("Choose a format:")
    print("1. DD-MM-YYYY")
    print("2. Month DD, YYYY")
    print("3. DD/MM/YYYY HH:MM:SS")
    choice = input("Enter your choice: ")

    formats = {
        "1": "%d-%m-%Y",
        "2": "%B %d, %Y",
        "3": "%d/%m/%Y %H:%M:%S",
    }
    fmt = formats.get(choice)
    if fmt:
        print(f"Formatted Date: {now.strftime(fmt)}")
    else:
        print("Invalid choice!")


def stopwatch():
    """A simple stopwatch. Press Enter to start, Enter again to stop."""
    input("Press Enter to START the stopwatch...")
    start = time.time()
    input("Press Enter to STOP the stopwatch...")
    end = time.time()
    elapsed = end - start
    print(f"Elapsed Time: {elapsed:.2f} seconds")


def countdown_timer():
    """A simple countdown timer."""
    try:
        seconds = int(input("Enter countdown time (in seconds): "))
        while seconds > 0:
            print(f"Time left: {seconds} seconds", end="\r")
            time.sleep(1)
            seconds -= 1
        print("\nTime's up!")
    except ValueError:
        print("Please enter a valid number of seconds.")


def datetime_menu():
    """Sub-menu for Datetime and Time Operations."""
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            custom_format()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice! Try again.")
        print("=" * 27)


if __name__ == "__main__":
    # Allows testing this module standalone
    datetime_menu()