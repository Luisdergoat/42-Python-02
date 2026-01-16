class GardenError:
    def __init__(self, name):
        self.palnt_name = name


class WateringError(GardenError):
    def __init__(self, name):
        super().__init__(name)

    def testing_Water_level(self, Water_level):
        if Water_level > 20:
            print(f"The plant does not need {Water_level}L of Water")
        elif Water_level < 8:
            print(f"The plant needs more than {Water_level}L of Water")
        else:
            print("Good amount of Water!")


class PlantError(GardenError):
    def __init__(self, name):
        super().__init__(name)

    def get_db_info(self, plant_database):
        return plant_database[self.palnt_name]

    def start_planting_new_plants(self):
        garden_db = {"Tomato": "Possible", "Cucumber": "Possible"}
        try:
            self.get_db_info(garden_db)
            print("You can plant these seeds here.")
            print(f"looking forward to get {self.palnt_name}!")
        except KeyError:
            print("You can't plant these seeds here!")


def test_errors():
    print("=" * 30)
    print("Garden Custom Error Tester")
    print("=" * 30)
    test_plant = input("What plant do you want to seed: ")
    test_plant = test_plant.upper()
    test_case = input("Do you want to check if the plot area can "
                      "handel the seed, then type (seedcheck)"
                      "if you want to check a amount of Water, type (water)")

    if test_case.lower() == "seedcheck":
        Plant = PlantError(test_plant)
        Plant.start_planting_new_plants()
        print("Test completed.")
        print("=" * 30)

    elif test_case.lower() == "water":
        while True:
            water_level = input("How much do you want to water the plant? ")
            try:
                water = int(water_level)
                break
            except ValueError:
                print("Please enter a valid number for water level.")

        Plant = WateringError(test_plant)
        Plant.testing_Water_level(water)
        go_on = input("Do you want to test the validation of the seed? "
                      "(yes/no): ")
        if go_on.lower() == "yes":
            Plant2 = PlantError(test_plant)
            Plant2.start_planting_new_plants()
        elif go_on.lower() == "no":
            pass
        else:
            print("Invalid input, skipping seed validation test.")
        print("Test completed.")
        print("=" * 30)

    else:
        print("Invalid test case selected.")


test_errors()
