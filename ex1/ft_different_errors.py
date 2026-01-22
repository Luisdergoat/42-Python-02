"""
Garden Error Types Demonstration.

Demonstrates:
- ValueError: Invalid data conversion
- ZeroDivisionError: Division by zero
- FileNotFoundError: Missing file access
- KeyError: Missing dictionary key
- Multiple error type handling
"""


def garden_operations(operation_type, value=None):
    """
    Perform garden operations that may raise different errors.

    Args:
        operation_type:  Type of operation to perform
        value:  Optional value for the operation

    Raises:
        ValueError: When invalid data is provided
        ZeroDivisionError: When dividing by zero
        FileNotFoundError: When file doesn't exist
        KeyError: When key is not in dictionary
    """
    # Garden inventory
    plants = {"roses": 10, "tulips": 5, "sunflowers": 8}

    if operation_type == "parse_number":
        # ValueError:  Trying to convert invalid string to int
        return int(value)

    elif operation_type == "divide_harvest":
        # ZeroDivisionError: Division by zero
        total_harvest = 100
        return total_harvest / value

    elif operation_type == "read_file":
        # FileNotFoundError: File doesn't exist
        with open(value, "r") as f:
            return f.read()

    elif operation_type == "get_plant":
        # KeyError: Key doesn't exist in dictionary
        return plants[value]


def test_error_types():
    """Test different error types and demonstrate error handling."""
    print("=== Garden Error Types Demo ===")

    # Test 1: ValueError
    print("Testing ValueError...")
    try:
        garden_operations("parse_number", "abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    # Test 2: ZeroDivisionError
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("divide_harvest", 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    # Test 3: FileNotFoundError
    print("Testing FileNotFoundError...")
    try:
        garden_operations("read_file", "missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError:  No such file 'missing.txt'")

    # Test 4: KeyError
    print("Testing KeyError...")
    try:
        garden_operations("get_plant", "missing_plant")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    # Test 5: Multiple errors with one except block
    print("Testing multiple errors together...")
    test_cases = [
        ("parse_number", "xyz"),
        ("divide_harvest", 0),
        ("get_plant", "invalid_plant"),
    ]

    for operation, value in test_cases:
        try:
            garden_operations(operation, value)
        except (ValueError, ZeroDivisionError, KeyError):
            print("Caught an error, but program continues!")
            break

    print("All error types tested successfully!")


def main():
    """Run the error types demonstration."""
    test_error_types()


if __name__ == "__main__":
    main()
