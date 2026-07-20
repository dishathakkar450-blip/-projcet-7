"""
math_ops.py
------------
Mathematical Operations module.
Built-in module used: math
"""

import math


def calculate_factorial():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial: {math.factorial(n)}")
    except ValueError:
        print("Please enter a valid integer.")


def compound_interest():
    try:
        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest (in %): "))
        t = float(input("Enter time (in years): "))
        amount = p * math.pow((1 + r / 100), t)
        ci = amount - p
        print(f"Compound Interest: {ci:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")


def trigonometric_calculations():
    print("Trigonometric Calculations:")
    print("1. sin")
    print("2. cos")
    print("3. tan")
    choice = input("Enter your choice: ")
    try:
        angle_deg = float(input("Enter angle (in degrees): "))
        angle_rad = math.radians(angle_deg)
        if choice == "1":
            print(f"sin({angle_deg}) = {math.sin(angle_rad):.4f}")
        elif choice == "2":
            print(f"cos({angle_deg}) = {math.cos(angle_rad):.4f}")
        elif choice == "3":
            print(f"tan({angle_deg}) = {math.tan(angle_rad):.4f}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid angle.")


def area_of_shapes():
    print("Area of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            r = float(input("Enter radius: "))
            print(f"Area of Circle: {math.pi * r ** 2:.2f}")
        elif choice == "2":
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print(f"Area of Rectangle: {l * b:.2f}")
        elif choice == "3":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print(f"Area of Triangle: {0.5 * b * h:.2f}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter valid numeric values.")


def math_menu():
    """Sub-menu for Mathematical Operations."""
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_factorial()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometric_calculations()
        elif choice == "4":
            area_of_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")
        print("=" * 27)


if __name__ == "__main__":
    math_menu()