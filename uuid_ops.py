"""
uuid_ops.py
------------
Generate Unique Identifiers (UUID) module.
Built-in module used: uuid
"""

import uuid


def generate_uuid():
    """Generate a unique identifier using UUID4."""
    print("Generate Unique Identifiers:")
    new_id = uuid.uuid4()
    print(f"Generated UUID: {new_id}")
    return str(new_id)


if __name__ == "__main__":
    generate_uuid()