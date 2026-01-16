def garden_operations():
    """A funktion to check diffrent Error types"""

    def calculate_plants_per_row(total_plants, rows):
        """Tests for ZeroDivisionError and TypeError"""
        total = int(total_plants)
        return total / rows

    def read_garden_plant(filename):
        """Tests for FileNotFoundError"""
        with open(filename, 'r') as file:
            return file. read()

    def get_plant_info(plant_name, plant_database):
        """Tests for KeyError"""
        return plant_database[plant_name]

    return calculate_plants_per_row, read_garden_plant, get_plant_info


def test_error_types():
    """Tests diffrent Error types in garden operations"""
    print("=" * 30)
    print("Garden Error Types Demo")
    print("=" * 30)

    # Function calls
    calc_plants, read_plants, get_info = garden_operations()

    # Testing Database for KeyError
    plant_db = {"Rose": "A red flower", "Tulip": "A spring flower"}

    # First test - ValueError
    print("\n=== Test 1: ValueError ===")
    try:
        result = calc_plants("abc", 5)
        print(f"Plants per row: {result}")
    except ValueError:
        print("Error: ValueError - Not a valid number!")
    print("Program running... \n")

    # Test 2 ZeroDivisionError
    print("=== Test 2: ZeroDivisionerror ===")
    try:
        result = calc_plants("100", 0)
        print(f"Plants per row: {result}")
    except ZeroDivisionError:
        print("Error: ZeroDivisionError - you can't divide with 0")
    print("Program running... \n")

    # Test 3 FileNotFoundError
    print("=== Test 3: FileNotfoundError")
    try:
        content = read_plants("gardenplan.txt")
        print(f"Gardenplan: {content}")
    except FileNotFoundError:
        print("Error: FileNotFoundError - Didn't find the file!")
    print("Program running... \n")

    # Test 4 KeyError
    print("=== Test 4 KeyError ===")
    try:
        info = get_info("Cucumber", plant_db)
        print(f"Plant-Info: {info}")
    except KeyError:
        print("Error: KeyError - Plant is not in database")
    print("Program running.. \n")

    # Test 5 multiple Errors
    print("=== Test 5 multiple Errors ===")

    test_cases = [("abc", 0, "ValueError Test")]

    for plants, rows, description in test_cases:
        try:
            result = calc_plants(plants, rows)
            print(f"{description}: {plants} plants / "
                  f"{rows} rows = {result:.1f} Plants per row")
        except (ValueError, ZeroDivisionError):
            print("Multiple Error encountert!")
    print("Program running... \n")


def interactive_tests():
    """Testing cases with user input"""
    plant_db = {"Rose": "A red flower", "Tulip": "A spring flower"}
    print("=" * 30)
    print("Interactive Test Start")
    print("=" * 30)
    while True:
        try:
            # taking user input
            run = input("Do you want to start or quit?")
            plantss = input("How many plants do you have:")
            if run.lower() == quit:
                break
            rows = input("How many rows:")

            # Calculation
            total = int(plantss)
            num_rows = int(rows)
            result = total / num_rows

            print(f"You need {result:.1f} Plants per row")

            # Plant-Info
            plant_name = input("\nWhat Plant? ")
            info = plant_db[plant_name]
            print(f"{plant_name}: Info: {info}")
        except ValueError:
            print("Number is not valid")
        except ZeroDivisionError:
            print("Can't divide with Zero")
        except KeyError:
            print("Plant not found in Database")
        except Exception as e:
            print(f"Unknown Error: {e}!!!")
    print("\nAll tests Complete!")
