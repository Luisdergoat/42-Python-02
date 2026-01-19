class Node:
    def __init__(self, plant_name, water_level, sunlight_hours):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.next = None


class Garden:
    def __init__(self):
        self.plant_list_head = None

    def add_plant_to_list(self, plant_name, water_level, sunlight_hours):
        new_node = Node(plant_name, water_level, sunlight_hours)
        if self.plant_list_head is None:
            self.plant_list_head = new_node
            return
        current = self.plant_list_head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def garden_info(self):
        current = self.plant_list_head
        while current is not None:
            print(f"Plant: {current.plant_name} is a healty plant in the "
                  f"Garden")
            current = current.next


def check_plant_health(plant_name, water_lvl, sun_hours):
    Plot = Garden()
    try:
        if plant_name == "":
            raise ValueError(" Error: plant name can't be empty")
        if water_lvl < 2 and water_lvl > 10:
            raise ValueError(f"Error: Water level {water_lvl} is not healthy")
        if sun_hours < 2 and sun_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sun_hours} is not "
                             f"healthy")
    except ValueError as ve:
        print(ve)
        return
    finally:
        if plant_name is not None and plant_name != "":
            print("✅ Plant name is valid")
            if water_lvl > 2 and water_lvl < 10:
                print("✅ Waterlevel is healty")
                if sun_hours > 2 and sun_hours < 12:
                    print("✅ Sunlight hours are Healty")
                    print(f"✅ Plant {plant_name} is healty")
                    Plot.add_plant_to_list(plant_name, water_lvl, sun_hours)
                    Plot.garden_info()
                else:
                    print("❌ Error: Sunlight hours are not healthy")
                    print("Healty hours of sun is missing for a healty plant")

            else:
                print("❌ Water level is not healty")
            if sun_hours > 2 and sun_hours < 12:
                print("✅ Sunlight hours are Healty")
                print("Healty water level is missing for a healty plant")
        else:
            print("❌ Error: Plantname is not valid")


def test_plant_checks():
    print("=" * 30)
    print("=== Garden Plant Health Checker ===")
    print("=" * 30)
    print("=== Start test 1 good values ===")
    check_plant_health("Tomato", 5, 5)
    print("=== Start test 2 bad water level ===")
    check_plant_health("Tomato", 100, 5)
    print("=== Start test 3 bad sunlight hours ===")
    check_plant_health("Tomato", 5, 24)
    print("=== Start test 4 bad plant name ===")
    check_plant_health(None, 5, 5)
    print("=== All error raising tests completed! ===")


test_plant_checks()
