"""
Custom Garden Errors Demonstration.

Demonstrates:
- Creating custom exception classes
- Exception inheritance hierarchy
- Raising custom exceptions
- Catching specific vs general exceptions
"""


class GardenError(Exception):
    """Base exception class for all garden-related errors."""

    def __init__(self, message):
        """
        Initialize GardenError.

        Args:
            message:   Error message describing the problem
        """
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Exception raised for plant-related problems."""

    def __init__(self, message):
        """
        Initialize PlantError.

        Args:
            message:  Error message describing the plant problem
        """
        super().__init__(message)


class WaterError(GardenError):
    """Exception raised for watering-related problems."""

    def __init__(self, message):
        """
        Initialize WaterError.

        Args:
            message: Error message describing the water problem
        """
        super().__init__(message)


def check_plant_health(plant_name, health_status):
    """
    Check plant health and raise PlantError if unhealthy.

    Args:
        plant_name:  Name of the plant
        health_status:   Health status ('healthy' or 'wilting')

    Raises:
        PlantError: If plant is not healthy
    """
    if health_status != "healthy":
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(water_level):
    """
    Check water level and raise WaterError if insufficient.

    Args:
        water_level:  Current water level (0-100)

    Raises:
        WaterError: If water level is too low
    """
    if water_level < 20:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """Test custom error types and demonstrate error handling."""
    print("=== Custom Garden Errors Demo ===")

    # Test 1: PlantError
    print("Testing PlantError...")
    try:
        check_plant_health("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e.message}")

    # Test 2: WaterError
    print("Testing WaterError...")
    try:
        check_water_level(10)
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")

    # Test 3: Catching all garden errors with base class
    print("Testing catching all garden errors...")

    # Test PlantError caught by GardenError
    try:
        check_plant_health("tomato", "wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e.message}")

    # Test WaterError caught by GardenError
    try:
        check_water_level(5)
    except GardenError as e:
        print(f"Caught a garden error: {e.message}")

    print("All custom error types work correctly!")


def main():
    """Run the custom errors demonstration."""
    test_custom_errors()


if __name__ == "__main__":
    main()
