"""
explorer.py
------------
Dynamic Module Exploration using dir().
Lets the user explore attributes of any built-in or custom module by name.
"""

import importlib


def explore_module():
    """Explore available attributes of any importable module using dir()."""
    print("Explore Module Attributes:")
    module_name = input("Enter module name to explore: ").strip()
    try:
        module = importlib.import_module(module_name)
        attributes = [a for a in dir(module) if not a.startswith("_")]
        print(f"\nAvailable Attributes in {module_name} module:")
        print(attributes[:10], "..." if len(attributes) > 10 else "")
        print("=" * 27)
    except ImportError:
        print(f"Module '{module_name}' not found!")


if __name__ == "__main__":
    explore_module()