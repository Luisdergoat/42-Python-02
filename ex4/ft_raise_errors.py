"""
Garden Plant Health Checker - Raising Errors Demonstration.

Demonstrates:
- Using raise keyword to trigger errors
- Validating input data
- Raising ValueError with custom messages
- Error handling with try/except
"""


def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check if plant conditions are healthy.

    Args:
        plant_name:  Name of the plant (must not be empty)
        water_level: Water level (must be between 1 and 10)
        sunlight_hours:  Hours of sunlight (must be between 2 and 12)

    Returns:
        str: Success message if all checks pass

    Raises:
        ValueError:  If any parameter is invalid
    """
    # Check plant name
    if not plant_name or plant_name.strip() == "":
        raise ValueError("Plant name cannot be empty!")

    # Check water level
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    # Check sunlight hours
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is "
                         f"too high (max 12)")

    # All checks passed
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Test plant health checks with various inputs."""
    print("=== Garden Plant Health Checker ===")

    # Test 1: Good values (should work)
    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error:  {e}")

    # Test 2: Empty plant name (should raise error)
    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    # Test 3: Bad water level (should raise error)
    print("Testing bad water level...")
    try:
        result = check_plant_health("lettuce", 15, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    # Test 4: Bad sunlight hours (should raise error)
    print("Testing bad sunlight hours...")
    try:
        result = check_plant_health("carrots", 5, 0)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


def main():
    """Run the plant health checker demonstration."""
    test_plant_checks()


if __name__ == "__main__":
    main()
