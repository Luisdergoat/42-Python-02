"""
Garden Watering System - Finally Block Demonstration.

Demonstrates:
- Using finally block for cleanup
- Cleanup happens even when errors occur
- Try/except/finally structure
- Resource management pattern
"""


def water_plants(plant_list):
    """
    Water plants from the list, with proper cleanup.

    Args:
        plant_list:  List of plant names to water

    Raises:
        ValueError: If a plant name is invalid (None or empty)
    """
    print("Opening watering system")

    try:
        # Water each plant
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")

    finally:
        # This ALWAYS runs, even if there was an error
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test the watering system with normal and error cases."""
    print("=== Garden Watering System ===")

    # Test 1: Normal watering (no errors)
    print("Testing normal watering...")
    try:
        good_plants = ["tomato", "lettuce", "carrots"]
        water_plants(good_plants)
        print("Watering completed successfully!")

    except ValueError as e:
        print(f"Error: {e}")

    # Test 2: Watering with error
    print("Testing with error...")
    try:
        bad_plants = ["tomato", None, "carrots"]
        water_plants(bad_plants)
        print("Watering completed successfully!")

    except ValueError as e:
        print(f"Error:  {e}")

    print("Cleanup always happens, even with errors!")


def main():
    """Run the watering system demonstration."""
    test_watering_system()


if __name__ == "__main__":
    main()
