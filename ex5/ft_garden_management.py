"""
Garden Management System - Complete Error Handling Integration.

Demonstrates:
- Custom exception classes
- Try/except/finally blocks
- Input validation and error raising
- Error recovery and continuation
- Resource cleanup
- Integration of all error handling techniques
"""

# ============================================
# CUSTOM EXCEPTION CLASSES
# ============================================


class GardenError(Exception):
    """Base exception for all garden-related errors."""

    def __init__(self, message):
        """Initialize GardenError with a message."""
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Exception for plant-related problems."""

    def __init__(self, message):
        """Initialize PlantError with a message."""
        super().__init__(message)


class WaterError(GardenError):
    """Exception for watering-related problems."""

    def __init__(self, message):
        """Initialize WaterError with a message."""
        super().__init__(message)


# ============================================
# GARDEN MANAGER CLASS
# ============================================


class GardenManager:
    """Manage garden plants with comprehensive error handling."""

    def __init__(self):
        """Initialize the garden manager."""
        self.plants = {}
        self.water_tank_level = 100

    def add_plant(self, plant_name, water_level=5, sunlight_hours=8):
        """
        Add a plant to the garden.

        Args:
            plant_name:  Name of the plant
            water_level:   Required water level (1-10)
            sunlight_hours:   Required sunlight hours (2-12)

        Raises:
            PlantError:  If plant data is invalid
        """
        # Validate plant name
        if not plant_name or plant_name.strip() == "":
            raise PlantError("Plant name cannot be empty!")

        # Validate water level
        if water_level < 1 or water_level > 10:
            raise PlantError(f"Water level {water_level} out of range (1-10)")

        # Validate sunlight hours
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours} out "
                             f"of range (2-12)")

        # Add plant to garden
        self.plants[plant_name] = {
            "water_level": water_level,
            "sunlight_hours": sunlight_hours,
            "healthy": True,
        }

    def water_plants(self):
        """
        Water all plants with proper resource cleanup.

        Raises:
            WaterError: If water tank is empty
        """
        print("Opening watering system")

        try:
            # Check water tank
            if self.water_tank_level < 10:
                raise WaterError("Not enough water in tank")

            # Water each plant
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
                self.water_tank_level -= 5

        finally:
            # Always cleanup, even if error occurred
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name):
        """
        Check health of a specific plant.

        Args:
            plant_name:   Name of the plant to check

        Returns:
            str: Health status message

        Raises:
            PlantError: If plant doesn't exist or has invalid parameters
        """
        # Check if plant exists
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found in garden")

        plant = self.plants[plant_name]

        # Validate water level
        if plant["water_level"] > 10:
            raise PlantError(f"Water level {plant['water_level']} is "
                             f"too high (max 10)")

        # Validate sunlight hours
        if plant["sunlight_hours"] < 2 or plant["sunlight_hours"] > 12:
            raise PlantError(f"Sunlight hours {plant['sunlight_hours']} "
                             f"out of range")

        # Return health status
        return (
            f"{plant_name}: healthy "
            f"(water: {plant['water_level']}, "
            f"sun: {plant['sunlight_hours']})"
        )


# ============================================
# TEST FUNCTION
# ============================================


def test_garden_management():
    """Test the garden management system with all error handling."""
    print("=== Garden Management System ===")

    # Create garden manager
    garden = GardenManager()

    # ========================================
    # TEST 1: Adding Plants
    # ========================================
    print("Adding plants to garden...")

    # Add valid plants
    try:
        garden.add_plant("tomato", 5, 8)
        print("Added tomato successfully")
    except PlantError as e:
        print(f"Error adding plant: {e. message}")

    try:
        garden.add_plant("lettuce", 6, 7)
        print("Added lettuce successfully")
    except PlantError as e:
        print(f"Error adding plant: {e. message}")

    # Add invalid plant (empty name)
    try:
        garden.add_plant("", 5, 8)
        print("Added plant successfully")
    except PlantError as e:
        print(f"Error adding plant: {e.message}")

    # ========================================
    # TEST 2: Watering Plants (with finally)
    # ========================================
    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Error watering:  {e.message}")

    # ========================================
    # TEST 3: Checking Plant Health
    # ========================================
    print("Checking plant health...")

    # Check valid plant
    try:
        status = garden.check_plant_health("tomato")
        print(status)
    except PlantError as e:
        print(f"Error checking tomato: {e.message}")

    # Check plant with invalid water level (simulate)
    garden.plants["lettuce"]["water_level"] = 15
    try:
        status = garden.check_plant_health("lettuce")
        print(status)
    except PlantError as e:
        print(f"Error checking lettuce: {e. message}")

    # ========================================
    # TEST 4: Error Recovery
    # ========================================
    print("Testing error recovery...")

    # Simulate low water tank
    garden.water_tank_level = 5

    try:
        garden.water_plants()
    except GardenError as e:
        # Caught general GardenError (WaterError is subclass)
        print(f"Caught GardenError: {e. message}")

    # System continues working
    print("System recovered and continuing...")

    print("Garden management system test complete!")


# ============================================
# MAIN FUNCTION
# ============================================


def main():
    """Run the garden management system test."""
    test_garden_management()


if __name__ == "__main__":
    main()
